# electricity_bill.py

# Ask user for number of units consumed
units = int(input("Enter the number of units consumed: "))

# Rate per unit
rate_per_unit = 5

# Calculate total bill
total_bill = units * rate_per_unit

# Display the result
print("Units Consumed:", units)
print("Total Bill: ₹", total_bill)
