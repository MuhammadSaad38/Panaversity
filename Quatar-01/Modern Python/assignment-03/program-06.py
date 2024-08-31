# Convert a given number of seconds into minutes and seconds using variables.

# Variable for total seconds
total_seconds = 130

# Convert seconds into minutes and remaining seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# Display the result
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
