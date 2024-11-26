from math import trunc
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess , actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low")
    else:
        print(f'You got it the answer is {actual_answer}')

def check_difficulty():
    level = input("Choose the difficulty . Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS





# Choosing random number from 1 to 100
print("Wellcome to random Guessing Game")
print("I'm thinking of number between 1 and 100")
answer = randint(1,100)



# Let the user  guess a numer
guess =  int(input('Make the guess: '))
