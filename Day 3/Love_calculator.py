import re 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name11 = input("What is your name? \n")
name22 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name11.lower()
name2=name22.lower()

concatinated_name = name1 + name2
t_count = len (re.findall("t",concatinated_name))
r_count = len (re.findall("r",concatinated_name))
u_count = len (re.findall("u",concatinated_name))
e_count = len (re.findall("e",concatinated_name))

true_count = str(t_count + r_count + u_count + e_count)

l_count = len (re.findall("l",concatinated_name))
o_count = len (re.findall("o",concatinated_name))
v_count = len (re.findall("v",concatinated_name))
e_count = len (re.findall("e",concatinated_name))

love_count = str (l_count + o_count + v_count + e_count)

total_count = true_count + love_count

print(f"Your score is {total_count}.")
