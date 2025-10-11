# Get inputs
initial_population = int(input("Initial number of organisms: "))
growth_rate = float(input("Rate of growth (e.g., 2 for doubling): "))
growth_period = int(input("Number of hours to achieve this rate: "))
total_hours = int(input("Total number of hours: "))

# Calculate number of growth cycles
num_cycles = total_hours // growth_period

# Start initial population
population = initial_population

# Repeat growth for each cycle
for cycle in range(num_cycles):
    population *= growth_rate
    print(f"After {((cycle + 1) * growth_period)} hours, the population is {int(population)}")

# Final
print(f"\nPredicted total population after {total_hours} hours: {int(population)}")
