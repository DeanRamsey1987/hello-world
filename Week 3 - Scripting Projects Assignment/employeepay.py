wage = float(input("Enter the hourly wage: "))
reg_hours = float(input("Enter the total regular hours worked: "))
ot_hours = float(input("Enter the total overtime hours worked: "))


regular_pay = wage * reg_hours


overtime_pay = ot_hours * (1.5 * wage)


total_weekly_pay = regular_pay + overtime_pay


print("Employee's total weekly pay is:", round(total_weekly_pay, 2))

input("Press Enter to exit...")