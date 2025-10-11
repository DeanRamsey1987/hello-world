import taxform

gross_income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

standard_deduct = 10000
dependent_deduct = 3000
tax_rate = 0.20  # 20%

taxable_income = gross_income - standard_deduct - (dependent_deduct * dependents)

income_tax = taxable_income * tax_rate

print("The income tax is", round(income_tax, 2), "dollars")

input("Press Enter to exit...")