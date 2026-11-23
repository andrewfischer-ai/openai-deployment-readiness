from src.financial_engine import calculate_business_case


def test_business_case():

    results = calculate_business_case(
        monthly_hours=40,
        hourly_rate=125,
        automation_percentage=0.60,
        implementation_cost=12000,
        annual_maintenance=2000
    )

    assert results["annual_hours_saved"] == 288
    assert results["annual_gross_value"] == 36000
    assert results["annual_net_value"] == 34000
    assert results["first_year_net_benefit"] == 22000
    assert round(results["payback_months"], 1) == 4.2
