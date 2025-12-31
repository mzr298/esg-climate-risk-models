# GHG Emissions Data Classification
# Assignment 1: Python Data Types

company_name = "TechCorp Industries"
reporting_year = 2024
scope_1_emissions_mtco2e = 5432.75
is_verified_data = True
scope_2_emissions_mtco2e = 12350.50
scope_3_emissions_mtco2e = 45678.25

total_emissions = scope_1_emissions_mtco2e + scope_2_emissions_mtco2e + scope_3_emissions_mtco2e

print("=" * 70)
print("GHG EMISSIONS REPORT")
print("=" * 70)
print(f"Company: {company_name}")
print(f"Year: {reporting_year}")
print(f"Scope 1: {scope_1_emissions_mtco2e} mtCO2e")
print(f"Scope 2: {scope_2_emissions_mtco2e} mtCO2e")
print(f"Scope 3: {scope_3_emissions_mtco2e} mtCO2e")
print(f"Total: {total_emissions} mtCO2e")
print(f"Data Verified: {'Yes' if is_verified_data else 'No'}")
print("=" * 70)

print("\nDATA TYPES:")
print(f"Company Name: {type(company_name)}")
print(f"Year: {type(reporting_year)}")
print(f"Emissions: {type(scope_1_emissions_mtco2e)}")
print(f"Verified: {type(is_verified_data)}")
