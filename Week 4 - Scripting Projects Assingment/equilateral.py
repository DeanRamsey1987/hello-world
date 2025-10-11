# Inputs
side1 = float(input("Enter the length of the 1st side: "))
side2 = float(input("Enter the length of the 2nd side: "))
side3 = float(input("Enter the length of the 3rd side: "))

# Check if sides are equal
if side1 == side2 and side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")
