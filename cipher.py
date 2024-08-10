#write the function which encrypt user's input by right shift of 5
def encrypt(sentence): #defines the function
    encrypted_message = '' #establish encrypted_message variable
    for character in sentence: #iterates through the characters in the sentence
        if character.islower(): #shifts lowercase letters by 5
            new_letter = chr((ord(character) - ord('a') + 5) % 26 + ord('a'))
        elif character.isupper(): #shifts uppercase letters
            new_letter = chr((ord(character) - ord('A') + 5) % 26 + ord('A'))
        else:
            new_letter = character #non-alphabet characters stay the same
        encrypted_message += new_letter #updates the characters in the message per the function above
    return encrypted_message 

#ask user for a message to encrypt
message = input("What's your secret message?  ")
#encrpy user's message
print(encrypt(message))


