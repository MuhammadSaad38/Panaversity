def calculate_age(current_year, birth_year):
    # Step 1: Get the current year and birth year
    current_year = int(current_year)
    birth_year = int(birth_year)
    
    # Step 2: Calculate the age by subtracting birth year from current year
    age = current_year - birth_year
    
    # Step 3: Return the calculated age
    return age
