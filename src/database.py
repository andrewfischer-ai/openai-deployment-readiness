import sqlite3
from pathlib import Path

# Define where the database will be stored
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "business_cases.db"


def initialize_database():

    # Connect to the database
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    # Create the business_cases table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS business_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            monthly_hours REAL NOT NULL,
            hourly_rate REAL NOT NULL,
            automation_percentage REAL NOT NULL,
            implementation_cost REAL NOT NULL,
            annual_maintenance REAL NOT NULL,
            annual_hours_saved REAL NOT NULL,
            annual_gross_value REAL NOT NULL,
            annual_net_value REAL NOT NULL,
            first_year_net_benefit REAL NOT NULL,
            payback_months REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

def save_business_case(title, description, assumptions, results):
    """
    Save a financial business case to SQLite.

    Returns the unique ID of the saved business case.
    """

    connection = sqlite3.connect(DB_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO business_cases (
                title,
                description,
                monthly_hours,
                hourly_rate,
                automation_percentage,
                implementation_cost,
                annual_maintenance,
                annual_hours_saved,
                annual_gross_value,
                annual_net_value,
                first_year_net_benefit,
                payback_months
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                assumptions["monthly_hours"],
                assumptions["hourly_rate"],
                assumptions["automation_percentage"],
                assumptions["implementation_cost"],
                assumptions["annual_maintenance"],
                results["annual_hours_saved"],
                results["annual_gross_value"],
                results["annual_net_value"],
                results["first_year_net_benefit"],
                results["payback_months"]
            )
        )

        connection.commit()

        return cursor.lastrowid

    finally:
        connection.close()

def get_business_case(business_case_id):
    """
    Retrieve a business case by its unique ID.
    """

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM business_cases
            WHERE id = ?
            """,
            (business_case_id,)
        )

        record = cursor.fetchone()

        if record is None:
            return None

        return dict(record)

    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
