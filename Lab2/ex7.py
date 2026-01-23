# ask the user to enter a temperature in Fahrenheit.
# convert the temperature to Celsius using the formula C = (F - 32) * 5/9.
# Name: Ethan Mayer
# Date: Jan. 22, 2026

fahrenheit_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheit_value = float(fahrenheit_input)
celsius_value = (fahrenheit_value - 32) * 5 / 9
celsius_value_rounded = round(celsius_value, 1)

print("You entered:", fahrenheit_value)
print(f"The temperature in Celsius is: {celsius_value_rounded}")

# Name: Ethan Mayer
# Date: Jan. 22, 2026

def farenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius and return the Celsius value rounded to 1 decimal place."""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)

# Test the function with known values
print("32 F ->", farenheit_to_celsius(32))    # Expected output: 0.0
print("212 F ->", farenheit_to_celsius(212))  # Expected output: 100.0

# Optional: Run the interactive part using the function
fahrenheit_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheit_value = float(fahrenheit_input)

celsius_value = farenheit_to_celsius(fahrenheit_value)

print("You entered:", fahrenheit_value)
print(f"The temperature in Celsius is: {celsius_value}")