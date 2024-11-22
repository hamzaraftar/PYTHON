alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt , type decode to 'decrypy' \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# to encrypt message
def encrypt(originalText , shiftAmount):
    cipherText = ""
    for latter in originalText:
        shiftedPosition = alphabet.index(latter) + shiftAmount
        shiftedPosition %= len(alphabet)
        cipherText += alphabet[shiftedPosition]
    print(f'Here is encoded result: {cipherText}')

encrypt(originalText = text , shiftAmount = shift)

# to decrypt message
def decrypt (originatText ,shiftAmount):
    print()