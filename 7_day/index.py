import random
word_list = ["aardvark" , "baboon" , "cammel"]
choise_word = random.choice(word_list)
print(choise_word)

placeholder = ""
word_length = len(choise_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)   

guess = input("Guess a latter: ").lower()

display = ""

for latter in choise_word:
    if latter == guess:
        display += latter
    else:
        display += "_"
print(display)        