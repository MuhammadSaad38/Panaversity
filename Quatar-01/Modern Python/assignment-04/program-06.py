def convert_seconds(seconds):
    # Step 1: Get the total number of seconds
    seconds = int(seconds)
    
    # Step 2: Calculate the number of minutes
    minutes = seconds // 60
    
    # Step 3: Calculate the remaining seconds
    remaining_seconds = seconds % 60
    
    # Step 4: Return the minutes and remaining seconds
    return minutes, remaining_seconds
