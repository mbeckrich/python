age = int(input("How old are you now?\n"))

age_in_days = 365 * age
age_in_weeks = 52 * age
age_in_months = 12 * age

days_at_90 = 365 * 90
weeks_at_90 = 52 * 90
months_at_90 = 12 * 90

days_left = days_at_90 - age_in_days
weeks_left = weeks_at_90 - age_in_weeks
months_left = months_at_90 - age_in_months

print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left}",
    "months left.",
)

# Her code differs in three ways:
# 1) She converts input to int in a variable after input, not during
# 2) She structures the calculation this way:
# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_reimaining = years_remaining * 52
# months remaining = years_remaining * 12
# 3) She puts the f-string into a variable `message` and then
# does print(message) instead of printing the f-string directly.
