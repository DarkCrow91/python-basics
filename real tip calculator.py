# Welcome message (String)
print("Welcome to the Tip Calculator!")

# Input for the total bill (Number)
total_bill = float(input("Enter the total bill amount: "))

# Input for the tip percentage (Number)
tip_percentage = float(input("Enter the tip percentage you would like to give: "))

# Calculating the tip amount and total amount (Variables and Numbers)
tip_amount = total_bill * (tip_percentage / 100)  # Calculating the tip
total_amount = total_bill + tip_amount            # Calculating the total amount

# Output the results (Strings and Variables)
print("\n----- Tip Calculator Results -----")
print("Total Bill: $" + str(total_bill))          # Converting numbers to strings
print("Tip Percentage: " + str(tip_percentage) + "%")
print("Tip Amount: $" + str(round(tip_amount, 2))) # Rounded to 2 decimal places
print("Total Amount to Pay: $" + str(round(total_amount, 2)))

# Thank you message
print("\nThank you for using the Tip Calculator!")

