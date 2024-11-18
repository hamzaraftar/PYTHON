print("Wellcome ot python Deleviers !")
size = input("What size of pizza do you want? to S M or L ")
pepporni = input("Do want to more pepporani on pizza Y or N :")
extraChiz = input("Do you want to extra cheeze? Y or N :")
bill = 0
if size == "S":
    bill += 15
elif size =="M":
    bill += 20
elif size =="L":
    bill += 25
else:
    print("You type the wrong inputs")

if pepporni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3    

if extraChiz == "Y":
    bill += 1
print(f"Your final bill is {bill}")    