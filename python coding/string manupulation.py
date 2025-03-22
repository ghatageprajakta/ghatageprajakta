full_name = input("Enter your full name: ")

# Step 2: Convert the name to title case
title_case_name = full_name.title()

# Step 3: Count the total number of characters (excluding spaces)
character_count = len(full_name.replace(" ", ""))

# Output the results
print("Formatted Name (Title Case):", title_case_name)
print("Total number of characters (excluding spaces):", character_count)

