import random
word_list = ["aardvark" , "baboon" , "cammel"]
choise_word = random.choice(word_list)
print(choise_word)
guess = input("Guess a latter: ").lower()

for latter in choise_word:
    if latter == guess:
        print("Right") 
    else:
        print("Wrong")