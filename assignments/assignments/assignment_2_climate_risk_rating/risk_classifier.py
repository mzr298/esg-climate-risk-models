# Build a climate risk assessment for multiple companies
# Company 1 Data
company_1_name = "SolarEnergy Ltd"
company_1_revenue_millions = 150.5
company_1_total_emissions_mtco2e    = 250.75
company_1_is_renewable_focused = True

# Company 2 Data
company_2_name = "CoalPower Corp"
company_2_revenue_millions = 200.0
company_2_total_emissions_mtco2e = 8000.0
company_2_is_renewable_focused = False

# Task 1: Calculate emissions intensity (emissions per million $ revenue)

company_1_emissions_intensity = company_1_total_emissions_mtco2e / company_1_revenue_millions
company_2_emissions_intensity = company_2_total_emissions_mtco2e /  company_2_revenue_millions
print(f"{company_1_name} Emissions Intensity (MtCO2e per million $ revenue):", company_1_emissions_intensity)
print(f"{company_2_name} Emissions Intensity (MtCO2e per million $ revenue):", company_2_emissions_intensity)

# Task 2: Create a simple risk classification
if company_1_emissions_intensity > 10.0:
    company_1_risk_level = "High Risk"
elif company_1_emissions_intensity >= 5.0:
    company_1_risk_level = "Medium Risk"
else:
    company_1_risk_level = "Low Risk"

if company_2_emissions_intensity > 10.0:
    company_2_risk_level = "High Risk"
elif company_2_emissions_intensity > 5.0:
    company_2_risk_level = "Medium Risk"
else:
    company_2_risk_level = "Low Risk"

print(f"{company_1_name} Risk Level:", company_1_risk_level)
print(f"{company_2_name} Risk Level:", company_2_risk_level)


# Task 4: Type conversion practice
company_1_revenue_int = int(company_1_revenue_millions)
company_2_revenue_int = int(company_2_revenue_millions)
print(f"{company_1_name} Revenue as Integer (millions $):", company_1_revenue_int)
print(f"{company_2_name} Revenue as Integer (millions $):", company_2_revenue_int)
print(f"{company_1_name} revenue as integer (millions $) type:", type(company_1_revenue_int))
print(f"{company_2_name} revenue as integer (millions $) type:", type(company_2_revenue_int))
