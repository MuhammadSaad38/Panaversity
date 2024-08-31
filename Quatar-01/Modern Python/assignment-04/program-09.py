import math
def volume_of_cylinder(radius, height):
    # Step 1: Get the radius and height of the cylinder
    radius = float(radius)
    height = float(height)
    
    # Step 2: Calculate the base area using the formula π * r^2
    base_area = math.pi * radius ** 2
    
    # Step 3: Calculate the volume by multiplying the base area by height
    volume = base_area * height
    
    # Step 4: Return the calculated volume
    return volume
