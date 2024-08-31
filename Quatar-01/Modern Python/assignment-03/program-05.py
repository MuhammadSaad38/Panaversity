# Create a program that converts a temperature from Fahrenheit to
# Celsius and vice versa using a variable.
# Variable for temperature in Fahrenheit
fahrenheit = 98.6

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Variable for temperature in Celsius
celsius = 37

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
