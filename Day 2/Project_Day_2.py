#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator.")
bill=input("What was the total bill? $")
tbill=float(bill)
tip=int(input("What percentange tip would you like to give? 10, 12, or 15? "))
total_bill=tbill+(tbill*tip/100)
no_of_people=int(input("How many people to split the bill? "))
shared_bill=round(total_bill/no_of_people,2)
result=f"Each person should pay: ${shared_bill}"
print(result)