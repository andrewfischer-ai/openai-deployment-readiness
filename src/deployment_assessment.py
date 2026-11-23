from dotenv import load_dotenv
from openai import OpenAI
from src.financial_engine import calculate_business_case

load_dotenv()

client = OpenAI()


# Collect user inputs

print("\nAI DEPLOYMENT READINESS ASSESSMENT")
print("----------------------------------")

business_problem = input("Describe the business process: ")

monthly_hours = float(input("Monthly labor hours: "))

hourly_rate = float(input("Fully burdened hourly rate ($): "))

automation_percentage = float(
    input("Expected workload reduction (%): ")
) / 100

implementation_cost = float(input("Implementation cost ($): "))

annual_maintenance = float(input("Annual maintenance cost ($): "))


# Calculate financial results

financial_results = calculate_business_case(
    monthly_hours,
    hourly_rate,
    automation_percentage,
    implementation_cost,
    annual_maintenance
)


# Display financial results

print("\nFINANCIAL ANALYSIS")
print("------------------")

for metric, value in financial_results.items():
    print(f"{metric}: {value}")


# Send financial results to OpenAI

response = client.responses.create(

    model="gpt-6-luna",

    instructions="""
    You are an enterprise AI investment advisor.

    Evaluate whether proposed AI automation projects
    represent sound business investments.

    Consider financial returns, operational benefits,
    implementation complexity, and risk.

    Use the financial calculations provided.
    Do not invent additional financial figures.

    Distinguish recovered labor capacity from
    actual cash savings.

    Recommend one of the following:

    PROCEED
    PILOT
    DEFER
    REJECT

    Explain your recommendation.
    """,

    input=f"""
    BUSINESS PROBLEM:

    {business_problem}

    FINANCIAL ANALYSIS:

    {financial_results}

    Provide:

    1. Executive summary
    2. Financial assessment
    3. Operational considerations
    4. Three principal risks
    5. Deployment recommendation
    """
)


# Display AI recommendation

print("\nAI EXECUTIVE ASSESSMENT")
print("-----------------------")

print(response.output_text)
