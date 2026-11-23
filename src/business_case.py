# Financial assumptions

# Collect financial assumptions from the user

print("\nAI AUTOMATION BUSINESS CASE CALCULATOR")
print("--------------------------------------")

monthly_hours = float(input("Monthly reporting hours: "))

hourly_rate = float(input("Fully burdened hourly rate ($): "))

automation_percentage = float(
    input("Expected workload reduction (%): ")
) / 100

implementation_cost = float(input("Implementation cost ($): "))

annual_maintenance = float(input("Annual maintenance cost ($): "))

# Calculate annual labor hours saved

annual_hours_saved = monthly_hours * 12 * automation_percentage

# Calculate annual value of recovered labor capacity

annual_gross_value = annual_hours_saved * hourly_rate

# Calculate annual net value after maintenance

annual_net_value = annual_gross_value - annual_maintenance

# Calculate first-year net benefit

first_year_net_benefit = annual_net_value - implementation_cost

# Calculate simple payback period

if annual_net_value > 0:
    payback_months = implementation_cost / annual_net_value * 12
else:
    payback_months = None

# Display results

print("\nAI AUTOMATION BUSINESS CASE")
print("----------------------------")

print(f"Annual Hours Saved: {annual_hours_saved:.1f}")
print(f"Annual Gross Value: ${annual_gross_value:,.2f}")
print(f"Annual Net Value: ${annual_net_value:,.2f}")
print(f"First-Year Net Benefit: ${first_year_net_benefit:,.2f}")

if payback_months is not None:
    print(f"Simple Payback Period: {payback_months:.1f} months")
else:
    print("Simple Payback Period: Not achieved")
