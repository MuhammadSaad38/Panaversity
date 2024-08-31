import math

def area_of_circle(radius):
    # Step 1: Get the radius
    radius = float(radius)
    
    # Step 2: Calculate the area using the formula π * r^2
    area = math.pi * radius ** 2
    
    # Step 3: Return the calculated area
    return area
