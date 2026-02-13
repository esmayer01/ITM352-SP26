# Ethan Mayer
# Feb. 10, 2026

# Create variables
age = 70
weekday = "Tuesday"
matinee = True

# Print the input values
print(f"Age: {age}")
print(f"Weekday: {weekday}")
print(f"Matinee: {matinee}")
print()

# Determine the lowest applicable price
normal_price = 14
senior_price = 8
tuesday_price = 10
matinee_senior_price = 5
matinee_regular_price = 8

# Start with a list to collect all applicable prices
applicable_prices = [normal_price]  # Normal price always applies as baseline

# Check if senior discount applies
if age >= 65:
    applicable_prices.append(senior_price)

# Check if Tuesday discount applies
if weekday == "Tuesday":
    applicable_prices.append(tuesday_price)

# Check if matinee pricing applies
if matinee:
    if age >= 65:
        applicable_prices.append(matinee_senior_price)
    else:
        applicable_prices.append(matinee_regular_price)

# Get the lowest price
final_price = min(applicable_prices)

print(f"Price: ${final_price}")