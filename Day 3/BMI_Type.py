# 🚨 Don't change the code below 👇
"""Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI_cal=(weight)/(height**2)
BMI_result=round(BMI_cal,1)

if BMI_result < 18.5 :
    print(f"Your BMI is {BMI_result}, you are underweight.")
elif BMI_result >= 18.5 and BMI_result < 25 :
    print(f"Your BMI is {BMI_result}, you have a normal weight.")
elif BMI_result >= 25 and BMI_result < 30 :
    print(f"Your BMI is {BMI_result}, you are slightly overweight.")
elif BMI_result >= 30 and BMI_result < 35 :
    print(f"Your BMI is {BMI_result}, you are obese.")
else :
    print(f"Your BMI is {BMI_result}, you are clinically obese.")