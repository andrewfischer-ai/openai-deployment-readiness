from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.financial_engine import calculate_business_case


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
