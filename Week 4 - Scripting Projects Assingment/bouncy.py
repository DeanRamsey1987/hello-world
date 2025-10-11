# Inputs
initial_height = float(input("Enter the initial height of the drop (in feet): "))
bounciness_index = float(input("Enter the bounciness index (0 < index < 1): "))
num_bounces = int(input("Enter the number of bounces: "))

total_distance = initial_height
current_height = initial_height

# Repeat for the num of bounces
for bounce in range(num_bounces):
    # Ball bounces back up
    current_height *= bounciness_index
    # Add down + up travel distance
    total_distance += 2 * current_height

# Output result
print("The total distance traveled by the ball is:", total_distance, "feet")
