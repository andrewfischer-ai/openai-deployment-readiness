from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.financial_engine import calculate_business_case
from src.database import get_business_case


# Create the API application
app = FastAPI(
    title="AI Deployment Readiness API",
    version="1.0.0"
)


# Define the API input requirements
class BusinessCaseInput(BaseModel):
    monthly_hours: float = Field(ge=0)
    hourly_rate: float = Field(ge=0)
    automation_percentage: float = Field(ge=0, le=1)
    implementation_cost: float = Field(ge=0)
    annual_maintenance: float = Field(ge=0)


# API health-check endpoint
@app.get("/")
def home():
    return {"status": "AI Deployment Readiness API is running"}


# Financial calculation endpoint
@app.post("/calculate")
def calculate(data: BusinessCaseInput):

    results = calculate_business_case(
        monthly_hours=data.monthly_hours,
        hourly_rate=data.hourly_rate,
        automation_percentage=data.automation_percentage,
        implementation_cost=data.implementation_cost,
        annual_maintenance=data.annual_maintenance
    )

    return results

# Retrieve a saved business case
@app.get("/business-cases/{business_case_id}")
def retrieve_business_case(business_case_id: int):

    record = get_business_case(business_case_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Business case not found"
        )

    return record
