import random 

user_choise = int(input("What do you chose Type 0 for Rock and 1 for Paper and 2 Scissor \n"))
computer_choise = random.randint(0,2)
if user_choise == 0:
    print("You win")
elif computer_choise > user_choise:
    print("You lose")
else:
    print("You are type invalid number ")