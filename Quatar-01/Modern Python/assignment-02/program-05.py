def fahrenheit_to_celsius(fahrenheit):
    # Step 1: Get the Fahrenheit temperature
    fahrenheit = float(fahrenheit)
    
    # Step 2: Convert to Celsius using the formula (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    
    # Step 3: Return the converted temperature
    return celsius

def celsius_to_fahrenheit(celsius):
    # Step 1: Get the Celsius temperature
    celsius = float(celsius)
    
    # Step 2: Convert to Fahrenheit using the formula (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    
    # Step 3: Return the converted temperature
    return fahrenheit
