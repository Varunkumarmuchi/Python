#Number Guessing Game Objectives:
from art import logo
import random

def choose_diff_lvl():
    life = {"hard": 5, "easy": 10}
    valid_input = True
    while valid_input:
        difficulty_level = input("Please select a level of dificulty easy or hard: ").lower()
        
        if difficulty_level not in life:
            print("Please select either hard or easy\n")
        else:    
            turns = life[difficulty_level]
            print(f"You have {turns} turns to guess the number")
            valid_input = False
    return turns
def request_number():
    # Allow the player to submit a guess for a number between 1 and 100.
    valid_in_range = False
    while not valid_in_range:
        x = input("Guess a number between 1 and 100: ")
        if x.isdigit():
            guess_the_number = int(x)
       
            if guess_the_number < 1 and guess_the_number > 100:
                print("\nPlease enter a value within the range")
            else:
                valid_in_range = True
        else:
            print("Please enter a integer value")
    return guess_the_number

def validate_the_guess(random_number, turns):
    while turns != 0:
           
        guessed_number = request_number()
        
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.    
        if guessed_number == random_number:
            print(f"\nHurray! you have guessed the correct number, it is {random_number}")
            break
            
        elif guessed_number > random_number:
            print("Too high")
            
        else:
            print("Too low")
        turns -= 1
        if turns != 0:
            print(f"\nyou have {turns} turns to guess")
        
    
# Include an ASCII art logo.
print(f"{logo} \n \n")

comp_number = random.randrange(1, 100)
num_turns = choose_diff_lvl()

game_on = True
while game_on:
    validate_the_guess(comp_number, num_turns) 
    play = input("Do you want to try again y or n").lower()
    if play == "y":
        print("lets play again")
    else:
        game_on = False

print("Thank you for your time")
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
