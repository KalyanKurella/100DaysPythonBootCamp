import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
def symbol(selection):
    if selection==0:
        print(rock)
    elif selection==1:
        print(paper)
    else:
        print(scissors)
def winner( human, ai):
    if(human == 0):
        if ai == 1:
            print("You lose")
        elif ai == 2:
            print("You win")
        else :
            print("Draw")
    elif(human == 1):
        if ai == 0 :
            print("You win")
        elif ai == 2 :
            print("You lose")
        else :
            print("Draw")
    elif human == 2 :
        if ai == 0 :
            print("You lose")
        elif ai == 1 :
            print("You won")
    else:
        pass
your_selection = int(input("What is your choice? 0 for rock, 1 for paper, 2 for scissors "))
symbol(your_selection)
computer_selection =  random.randint(0,2)
print(f"{computer_selection}")
print("Computer choose")
symbol(computer_selection)
winner(your_selection, computer_selection)