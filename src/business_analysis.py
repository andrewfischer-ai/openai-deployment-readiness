from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Define the business opportunity
business_problem = """
A NASA engineering support contractor employs 85 people.

The program manager spends approximately 12 hours
per month preparing financial reports.

These reports require collecting information from
multiple spreadsheets, reviewing labor expenditures,
identifying variances, and preparing management summaries.

The organization wants to evaluate whether AI could
reduce the administrative workload.
"""

# Ask AI to evaluate the opportunity
response = client.responses.create(
    model="gpt-6-luna",

    instructions="""
    You are an enterprise AI strategy consultant.

    Evaluate business processes for potential AI
    automation opportunities.

    Be objective and identify both benefits and risks.

    Do not invent financial data.
    """,

    input=f"""
    Evaluate the following business opportunity:

    {business_problem}

    Provide:

    1. Business problem summary
    2. Potential AI solution
    3. Expected operational benefits
    4. Three implementation risks
    5. Recommendation on whether to proceed
    """
)

print(response.output_text)

