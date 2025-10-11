def main():
    # Get inputs
    starting_salary = float(input("Enter the starting salary: "))
    percent_increase = float(input("Enter the annual percentage increase (e.g., 2 for 2%): "))
    years = int(input("Enter the number of years in the schedule: "))

    # Convert percentage to multiplier
    increase_rate = 1 + (percent_increase / 100.0)

    # Print header
    print("\nYear\tSalary")
    print("-" * 20)

    # First year salary
    salary = starting_salary

    # Generate the schedule
    for year in range(1, years + 1):
        print(f"{year}\t${salary:,.2f}")
        salary *= increase_rate

if __name__ == "__main__":
    main()
