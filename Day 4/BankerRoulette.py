# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)
random_index = random.randint(0,length-1)

print(f"{names[random_index]} is going to buy the meal today!")
#print(random.choice(names))