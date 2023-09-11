# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_life_span=90-int(age)
remaining_days=int(remaining_life_span*365.25)
remaining_weeks=int(remaining_life_span*52)
remaining_months=int(remaining_life_span*12)
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

