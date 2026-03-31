import psycopg2
import os
from contextlib import contextmanager
from dotenv import load_dotenv

# --- 1. INFRASTRUCTURE & CONFIGURATION ---

def get_db_url():
    """Loads and returns the DB_URL from environment variables."""
    load_dotenv()
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("❌ DB_URL not found in environment variables.")
    return db_url

@contextmanager
def get_db_connection():
    """Context manager to handle database connection, commits, and cleanup."""
    db_url = get_db_url()
    conn = psycopg2.connect(db_url)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# --- 2. GENERIC DATABASE UTILITIES ---

def execute_ddl(query):
    """Executes Data Definition Language (Table creation, etc.)."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)

def execute_dml(query, params=None):
    """Executes Data Manipulation Language (Insert, Update, Delete)."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params or ())

def execute_query(query, params=None, fetch_all=False):
    """Executes a query and returns one or all results."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchall() if fetch_all else cur.fetchone()

# --- 3. SPECIFIC BUSINESS LOGIC ---

def check_db_version():
    """Logs the PostgreSQL version."""
    version = execute_query('SELECT VERSION();')
    if version:
        print(f"✅ Connected to: {version[0]}")

def setup_all_tables():
    """Initializes schema for both Employee and Training tables."""
    # Employee Table
    employee_ddl = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE,
        gender VARCHAR(20),
        salary DECIMAL(10,2),
        currency VARCHAR(4)
    );'''
    
    # Training Table
    training_ddl = '''
    CREATE TABLE IF NOT EXISTS anubhav_training (
        id SERIAL PRIMARY KEY,
        course_name VARCHAR(50) UNIQUE,
        trainer VARCHAR(100),
        price INTEGER,
        duration INTEGER
    );'''
    
    execute_ddl(employee_ddl)
    execute_ddl(training_ddl)
    print("🚀 All tables initialized.")

def seed_data(employees, training_data):
    """Populates both tables using UPSERT logic."""
    # Seed Employees
    emp_sql = '''INSERT INTO employees (name, gender, salary, currency) 
                 VALUES (%s, %s, %s, %s) ON CONFLICT (name) DO NOTHING;'''
    
    # Seed Training
    train_sql = '''INSERT INTO anubhav_training (course_name, trainer, price, duration) 
                   VALUES (%s, %s, %s, %s) ON CONFLICT (course_name) DO NOTHING;'''

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Batch Employee insert
            for emp in employees:
                cur.execute(emp_sql, (emp['name'], emp['gender'], emp['salary'], emp['currency']))
            # Batch Training insert
            for course, info in training_data.items():
                cur.execute(train_sql, (course, info['trainer'], info['price'], info['hours']))
    
    print(f"📊 Data seeding complete.")

# --- 4. MAIN ORCHESTRATOR ---

if __name__ == "__main__":
    # Sample Data
    emp_list = [
        {"name": "Fiona Gallagher", "gender": "Female", "salary": 78000, "currency": "EUR"},
        {"name": "Jordan Lee", "gender": "Non-binary", "salary": 88000, "currency": "SGD"}
    ]

    training_dict = {
        "Python Pro": {"trainer": "Anubhav", "price": 500, "hours": 40},
        "Cloud Native": {"trainer": "Anubhav", "price": 750, "hours": 60}
    }

    try:
        check_db_version()
        setup_all_tables()
        seed_data(emp_list, training_dict)
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
