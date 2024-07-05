from art import logo

#    _____                                     _____ _       _               
#   / ____|                                   / ____(_)     | |              
#  | |     ___  __ _ ___  ___ _ __           | |     _ _ __ | |__   ___ _ __ 
#  | |    / _ \/ _` / __|/ _ \ '__|          | |    | | '_ \| '_ \ / _ \ '__|
#  | |___|  __/ (_| \__ \  __/ |             | |____| | |_) | | | |  __/ |   
#   \_____\___|\__,_|___/\___|_|              \_____|_| .__/|_| |_|\___|_|   
#                                    ______           | |                    
#                                   |______|          |_|                    


#  CEASER CIPHER INDIVIDUAL BLOCKS

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :: \n")
# text = input("Type your message :: \n").lower()
# shift=int(input("Type the shift number :: \n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         # alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is :: {cipher_text}")





# def decrypt(cipherText, shiftAmount):
#     plainText = ""
#     for letter in cipherText:
#         position = alphabet.index(letter)
#         newPosition = position - shiftAmount
#         plainText += alphabet[newPosition]
#     print(f"The decoded message is ::{plainText} ")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipherText=text, shiftAmount=shift)
# else:
#     print("You have been blocked out")




#    _____                                     _____ _       _               
#   / ____|                                   / ____(_)     | |              
#  | |     ___  __ _ ___  ___ _ __           | |     _ _ __ | |__   ___ _ __ 
#  | |    / _ \/ _` / __|/ _ \ '__|          | |    | | '_ \| '_ \ / _ \ '__|
#  | |___|  __/ (_| \__ \  __/ |             | |____| | |_) | | | |  __/ |   
#   \_____\___|\__,_|___/\___|_|              \_____|_| .__/|_| |_|\___|_|   
#                                    ______           | |                    
#                                   |______|          |_|                    


# COMBINING BOTH INTO 1 


print(logo)
shouldContinue = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while shouldContinue == True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt :: \n")
    text = input("Type your message :: ").lower()
    shift=int(input("Type the shift number :: "))
    shift = shift % 26

    def cipher(startText, shiftAmount, cipherDirection):
        endText = ""
        if cipherDirection == "decode":
                shiftAmount *= -1
        for char in startText:
            if char in alphabet:
                position = alphabet.index(char)
                newPosition = position + shiftAmount
                endText += alphabet[newPosition]
            else:
                endText += char
        print(f"The {cipherDirection}d text is :: {endText}")

    cipher(startText = text, shiftAmount = shift, cipherDirection = direction)
    
    result = input("\nType 'yes' if you want to Restart. Otherwise 'no'.\n" )
    if result == "no":
        shouldContinue : False
        print("Exitting Now ........///")
        break
         