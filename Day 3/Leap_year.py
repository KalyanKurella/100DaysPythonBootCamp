# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check = False
if(year % 4 == 0):
    check = True
    if (year % 400 == 0):
        check = True
    elif (year % 100 == 0):
       check = False
    else :
        pass
else :
   check = False

if (check == True):
    print("Leap year.")
else :
    print("Not Leap year.")

