from src.database import initialize_database, save_business_case
from src.financial_engine import calculate_business_case


# Initialize the database
initialize_database()


# Financial assumptions
assumptions = {
    "monthly_hours": 40,
    "hourly_rate": 125,
    "automation_percentage": 0.60,
    "implementation_cost": 12000,
    "annual_maintenance": 2000
}


# Calculate financial results
results = calculate_business_case(**assumptions)


# Save the business case
business_case_id = save_business_case(
    title="Financial Reporting Automation",
    description="Automate monthly reporting for an engineering services organization.",
    assumptions=assumptions,
    results=results
)


print(f"Business case saved successfully. ID: {business_case_id}")
