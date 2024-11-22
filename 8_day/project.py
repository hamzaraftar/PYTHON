alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt , type decode to 'decrypy' \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# to encrypt message
# def encrypt(originalText , shiftAmount):
#     cipherText = ""
#     for latter in originalText:
#         shiftedPosition = alphabet.index(latter) + shiftAmount
#         shiftedPosition %= len(alphabet)
#         cipherText += alphabet[shiftedPosition]
#     print(f'Here is encoded result: {cipherText}')

# encrypt(originalText = text , shiftAmount = shift)

# to decrypt message
# def decrypt (originalText ,shiftAmount):
#     outPut = ""
#     for latter in originalText:
#         shiftedPosition = alphabet.index(latter) - shiftAmount
#         shiftedPosition %= len(alphabet)
#         outPut += alphabet[shiftedPosition]
#     print(f'Here is encoded result: {outPut}')

# decrypt(originalText=text , shiftAmount=shift)    

# converting both in single function 

def  caeser (originalText , shiftAmount , encode_or_decode):
    outPut = ""
    for latter in originalText:
        if encode_or_decode  == "decode":
            shiftAmount *= -1
        shiftedPosition = alphabet.index(latter) + shiftAmount
        shiftedPosition %= len(alphabet)
        outPut += alphabet[shiftedPosition]
    print(f'Here is encoded result: {outPut}')

caeser(text , shift , direction)