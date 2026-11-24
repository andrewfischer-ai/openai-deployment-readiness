from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_valid_business_case():

    response = client.post(
        "/calculate",
        json={
            "monthly_hours": 40,
            "hourly_rate": 125,
            "automation_percentage": 0.60,
            "implementation_cost": 12000,
            "annual_maintenance": 2000
        }
    )

    assert response.status_code == 200

    results = response.json()

    assert results["annual_hours_saved"] == 288
    assert results["annual_gross_value"] == 36000
    assert results["annual_net_value"] == 34000
    assert results["first_year_net_benefit"] == 22000
    assert round(results["payback_months"], 2) == 4.24


def test_invalid_automation_percentage():

    response = client.post(
        "/calculate",
        json={
            "monthly_hours": 40,
            "hourly_rate": 125,
            "automation_percentage": 1.5,
            "implementation_cost": 12000,
            "annual_maintenance": 2000
        }
    )

    assert response.status_code == 422

def test_retrieve_business_case():

    response = client.get("/business-cases/3")

    assert response.status_code == 200

    results = response.json()

    assert results["id"] == 3
    assert results["title"] == "Financial Reporting Automation"
    assert results["annual_hours_saved"] == 288
    assert results["first_year_net_benefit"] == 22000


def test_missing_business_case():

    response = client.get("/business-cases/999999")

    assert response.status_code == 404

    assert response.json()["detail"] == "Business case not found"
