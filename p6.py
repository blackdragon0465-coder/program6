# electricity_bill.py

# Ask user for number of units consumed
units = int(input("Enter the number of units consumed: "))

# Rate per unit
rate_per_unit = 5

# Calculate total bill
total_bill = units * rate_per_unit

# Apply discount if applicable
if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print("Units Consumed:", units)
    print("Total Bill: ₹", total_bill)
    print("Discount Applied: ₹", discount)
    print("Final Bill: ₹", final_bill)
else:
    print("Units Consumed:", units)
    print("Total Bill: ₹", total_bill)
