import streamlit as st
from db import init_db as db  # Assuming the modularized code is in db_module.py
import invoice_generator as invgen

st.title("Welcome to Anubhav Trainings")

# --- 1. SESSION STATE SETUP ---
if "selected_courses" not in st.session_state:
    st.session_state.selected_courses = []

# --- 2. DATABASE INITIALIZATION (CACHED) ---
@st.cache_resource
def initialize_application():
    """Runs once to setup schema and seed initial data."""
    try:
        # Check connection
        db.check_db_version()
        
        # Setup Table
        training_ddl = '''
        CREATE TABLE IF NOT EXISTS anubhav_training (
            id SERIAL PRIMARY KEY,
            course_name VARCHAR(50) UNIQUE,
            trainer VARCHAR(100),
            price INTEGER,
            duration INTEGER
        );'''
        db.execute_ddl(training_ddl)
        
        # Seed Data
        courses_data = {
            "UI5" : {"trainer": "Anubhav", "hours": 40, "price": 380},
            "CPI" : {"trainer": "Anurag", "hours": 35, "price": 400},
            "AOH" : {"trainer": "Anubhav", "hours": 40, "price": 400},
            "CDS" : {"trainer": "Ananya", "hours": 50, "price": 480},
            "BTP" : {"trainer": "Saurabh", "hours": 30, "price": 580},
            "SAC" : {"trainer": "Rohan", "hours": 45, "price": 300},
            "CAPM" : {"trainer": "Sonia", "hours": 60, "price": 900},
            "RAP" : {"trainer": "Anubhav", "hours": 40, "price": 850}
        }
        
        # Insert using our modular seed logic
        train_sql = '''INSERT INTO anubhav_training (course_name, trainer, price, duration) 
                       VALUES (%s, %s, %s, %s) ON CONFLICT (course_name) DO NOTHING;'''
        
        with db.get_db_connection() as conn:
            with conn.cursor() as cur:
                for name, info in courses_data.items():
                    cur.execute(train_sql, (name, info['trainer'], info['price'], info['hours']))
        
        return True
    except Exception as e:
        st.error(f"Database Init Failed: {e}")
        return False

# --- 3. HELPER FUNCTIONS ---
def display_selected_courses():
    if st.session_state.selected_courses:
        for course in st.session_state.selected_courses:
            # course index mapping: 0:id, 1:course_name, 2:trainer, 3:price, 4:duration
            st.write(f"📖 **{course[1]}** | Trainer: {course[2]} | Price: ${course[3]} | {course[4]} hrs")
    else:
        st.info("Your cart is empty.")

# Trigger Initialization
app_ready = initialize_application()

# --- 4. UI / FORM ---
if app_ready:
    with st.form("course_selection_form"):
        st.subheader("Choose your favourite courses from Anubhav Trainings")
        course_input = st.text_input("Enter module (e.g., UI5, BTP, RAP)", placeholder="Type here...")
        
        col1, col2 = st.columns(2)
        with col1:
            learn = st.form_submit_button("👍 Add to Cart")
        with col2:
            order = st.form_submit_button("🛒 Order Now")

        if learn:
            if course_input:
                # Use modular query utility
                query = "SELECT * FROM anubhav_training WHERE UPPER(course_name) = %s;"
                data = db.execute_query(query, (course_input.upper(),))
                
                if data:
                    st.session_state.selected_courses.append(data)
                    st.success(f"✅ Added {data[1]} to your list!")
                else:
                    st.error("❌ Course not found. Please try again.")
            else:
                st.warning("Please enter a course name.")

        if order:
            if st.session_state.selected_courses:
                st.subheader("Final Order Summary:")
                display_selected_courses()
                
                # Generate PDF
                invgen.generate_invoice(st.session_state.selected_courses, "invoice.pdf")
                st.balloons()
                st.success("🛒 Invoice generated! Your order is placed.")
            else:
                st.error("❌ Your cart is empty!")

# --- 5. FOOTER / VISUALS ---
st.divider()
st.caption("Powered by Anubhav Trainings Modular DB Engine")
