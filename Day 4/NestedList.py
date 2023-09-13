import random
fruits = ["apple","mango","banana","grapes","cherry"]
vegetables = ["birnjal","tomato","potato","raddish"]

fruits_vegatables =[fruits,vegetables]
print(fruits_vegatables)
print(fruits_vegatables[0][1])
# selecting random 5 items
print("\n\n\n\n")
for i in range(5):
    print(fruits[random.randint(0,len(fruits)-1)])