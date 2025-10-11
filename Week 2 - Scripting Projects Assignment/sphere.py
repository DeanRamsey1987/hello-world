import math

radius = float(input("Enter radius of sphere: "))
unit_measurements = input("Enter unit of measurement: ")
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * (radius ** 2)
volume = (4/3) * math.pi * (radius ** 3)

print("Diameter: ", diameter, unit_measurements)
print("Circumference: ", circumference, unit_measurements)
print("Surface area: ", surface_area, unit_measurements, "squared." )
print("Volume: ", volume, unit_measurements, "cubed.")

input("Press Enter to exit...")
