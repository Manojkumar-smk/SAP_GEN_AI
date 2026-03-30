import psycopg2
import os
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

# --- DATABASE UTILITIES ---

@contextmanager
def get_db_connection():
    """Context manager to handle database connection and cleanup."""
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL not found in environment variables.")
    
    conn = psycopg2.connect(db_url)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def execute_query(query, params=None, fetch=False):
    """Generic function to execute any query."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchone()
            return None

# --- BUSINESS LOGIC ---

def check_db_version():
    """Prints the PostgreSQL version."""
    try:
        row = execute_query('SELECT VERSION();', fetch=True)
        if row:
            print(f"Connected to: {row[0]}")
    except Exception as e:
        print(f"Version check failed: {e}")

def initialize_schema():
    """Creates the necessary tables."""
    ddl_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE,
        gender VARCHAR(20),
        salary DECIMAL(10,2),
        currency VARCHAR(4)
    );'''
    execute_query(ddl_query)
    print("Schema initialized.")

def seed_employees(employee_list):
    """Inserts a list of employee dictionaries into the database."""
    insert_sql = '''
        INSERT INTO employees (name, gender, salary, currency)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING;
    '''
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            for emp in employee_list:
                cur.execute(insert_sql, (emp['name'], emp['gender'], emp['salary'], emp['currency']))
    print(f"Successfully processed {len(employee_list)} records.")

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    additional_employees = [
    {"name": "Fiona Gallagher", "gender": "Female", "salary": 78000, "currency": "EUR"},
    {"name": "George Miller", "gender": "Male", "salary": 92000, "currency": "AUD"},
    {"name": "Hana Sato", "gender": "Female", "salary": 12500000, "currency": "JPY"},
    {"name": "Ian Wright", "gender": "Male", "salary": 55000, "currency": "GBP"},
    {"name": "Jordan Lee", "gender": "Non-binary", "salary": 88000, "currency": "SGD"}
    ]

    try:
        check_db_version()
        initialize_schema()
        seed_employees(additional_employees)
    except Exception as e:
        print(f"Workflow failed: {e}")
