# Round to two decimal places

print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? "))
tip = int(
    input("What percentage tip would you like to give -- 10, 12, or 15? ")
)
diners = int(input("How many people will split the bill? "))

# tip: 100 * 10% = $10
# or 100 * 1.1
# 1.1, 1.12, 1.15

tip_adjustment = 1 + 0.01 * tip

bill_with_tip = bill * tip_adjustment
divided_portion = bill_with_tip / diners
rounded_total = round(divided_portion, 2)
rounded_total = "{:.2f}".format(divided_portion)

message = f"Each person should pay: ${rounded_total}"
print(message)

# Her differences:
# 1) Uses a $ at the prompt e.g. "input(What was the total bill? $)"
# 2) Converts bill variable to float (made this adjustment on mine)
# 3) her bill_with_tip variable goes `tip / 100 * bill + bill`
# 4) Uses line 19 to solve problem of hidden 0 (added this to mine)
