# BMI calculator
height = float(input("Please provide your height in meters for the BMI calculator.\n"))
weight = float(input("Thanks, and your weight in kilograms is?\n"))

bmi = (weight) / (height) ** 2

print("Your BMI is:")
print(int(bmi))
