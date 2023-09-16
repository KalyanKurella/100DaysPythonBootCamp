#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

choosen_word = random.choice(word_list)

solving_list = ["_" for _ in choosen_word]
lives = 4

if lives > 0 :
    for letter in choosen_word :
        guess = input("Guess the word :").lower()
        for j in range(0, len(choosen_word)):
            if choosen_word[j] == guess :
                solving_list[j] = guess
                print(solving_list)
            else :
                lives -= 1
       
    
else :
    print("Game over")  