#NOTE :Don't use max() 


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
"""
max_element = 0
for i in range( 0, len(student_scores)):
    if student_scores[i] > max_element :
        max_element = student_scores[i]
    else :
        pass
print(max_element)"""

#easy way
arr = sorted(student_scores)
max_element = len(arr)-1
print(arr[max_element])




