# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum_of_heights= sum(student_heights)
avg_height = round(sum_of_heights/len(student_heights))
print(avg_height)
#Write your code below this row 👇




