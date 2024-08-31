def calculate_bmi(weight, height):
    # Step 1: Get the weight (kg) and height (m)
    weight = float(weight)
    height = float(height)
    
    # Step 2: Calculate the BMI using the formula weight / height^2
    bmi = weight / height ** 2
    
    # Step 3: Return the calculated BMI
    return bmi
