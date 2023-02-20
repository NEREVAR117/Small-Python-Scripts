user = input("Put in a message to encode: ")
shift = input("What is your encryption key? ")

ciphered = ''

for x in user.upper():
    if x == " ":
        ciphered += " "
        print(x, ciphered)
    else:
        ciphered += chr(ord(x) + int(shift))
        print(x, ciphered)