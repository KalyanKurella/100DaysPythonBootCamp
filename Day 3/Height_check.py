print("Welcome to roller-coaster")
#Taking the input from console of integer type
height_in_cm = int(input("Enter your height in cm :"))
#checking whether the height is greater than or equal to 120cm
if height_in_cm >= 120:
    #this block will execute if height is greater than or equal to 120cm
    print("You can ride the roller-coaster")
    age=int(input("What is your age? "))
    if age < 12 :
        print("Please pay $5.")
    elif age <= 18 :
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    #this block will execute if height is less than 120cm
    print("You are not eligible ")