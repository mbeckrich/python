# BMI Calculator 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"This BMI is {round(bmi)}, which is considered underweight.")
elif bmi < 25:
    print(
        f"You have a BMI of {round(bmi)}, which is considered a normal weight."
    )
elif bmi < 30:
    print(
        f"You have a BMI of {round(bmi)}, which is considered slightly",
        "overweight.",
    )
elif bmi < 35:
    print(f"You have a BMI of {round(bmi)}, which is is considered obese.")
else:
    print(
        f"You have a BMI of {round(bmi)}, which is considered clinically",
        "obese.",
    )

# Differences in her code:
# 1) Uses round() on bmi variable equation `bmi = round(weight/height**2),
# which is cleaner.
# 2) She uses an else statement at the end instead of elif to assign
# the clinically overweight result. I have changed my code to reflect this.
