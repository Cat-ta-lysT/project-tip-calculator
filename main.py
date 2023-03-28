# Tip Calculator

# Welcome message
print("\t\tWelcome to Tip Calculator\t\t")

# User input for the billing amount
bill_amount = int(input("\nPlease input the Billing Amount:\n"))

# User input for selecting tip percentage
tip_slab = int(input("\n\nPlease Select the tip percentage from the given List:\n\t1. 0%\n\t2. 25%\n\t3. 50%\n\t4.Custom percentage\n"))

# Calculation of tip based on the selected tip percentage slab
if tip_slab == 4:
    # If the user selects custom percentage, prompt for custom percentage and calculate tip
    tip_percentage = (float(input("Enter Custom Percentage:\n")))/100
else:
    # If the user selects a preset percentage, calculate tip based on the selection
    if tip_slab == 1:
        tip_percentage = 0
    elif tip_slab == 2:
        tip_percentage = 0.25
    elif tip_slab == 3:
        tip_percentage = 0.50

# Calculate the tip amount based on the tip percentage and the billing amount
tip_calculated = bill_amount * tip_percentage

# Display the calculated tip and the total bill including the tip
print(f"Tip amount : {tip_calculated}")
print(f"Total Bill (Tip Included) : {tip_calculated + bill_amount}")
