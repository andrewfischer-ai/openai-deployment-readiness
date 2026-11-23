def calculate_business_case(
    monthly_hours,
    hourly_rate,
    automation_percentage,
    implementation_cost,
    annual_maintenance
):

    annual_hours_saved = monthly_hours * 12 * automation_percentage

    annual_gross_value = annual_hours_saved * hourly_rate

    annual_net_value = annual_gross_value - annual_maintenance

    first_year_net_benefit = annual_net_value - implementation_cost

    if annual_net_value > 0:
        payback_months = implementation_cost / annual_net_value * 12
    else:
        payback_months = None

    return {
        "annual_hours_saved": annual_hours_saved,
        "annual_gross_value": annual_gross_value,
        "annual_net_value": annual_net_value,
        "first_year_net_benefit": first_year_net_benefit,
        "payback_months": payback_months
    }
