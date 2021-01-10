

import art
print(art.logo)


alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print(len(alphabets_list))


"""Part 1"""
#method i used has limitation if i use inputs like x,y,z and shift
# def encrypt():
#
#     #while not end_of_text:
#     text = list(input("Type your message:\n"))
#     print(text)
#     print(len(text))
#
#     shift = int(input("Type the shift number:\n"))
#     print(shift)
#
#     shifted_alphabets_list = []
#     for counter in range(0, len(text)):
#         letter_selected = text[counter]
#         for shifting in range(0, len(alphabets_list)):
#             if letter_selected == alphabets_list[shifting]:
#                 shifted_alphabets_list += alphabets_list[shifting + shift]
#
#
#     print(f"The encoded text is {shifted_alphabets_list}")

#encrypt()

"""#Part 1"""

# def encrypt(plain_text, shift_amount):
#
#     cipher_text = ""
#     for letter in plain_text:
#         position=alphabets_list.index(letter) #gives the index no. of the letter in plain_text
#         new_position= position+shift_amount
#         new_letter= alphabets_list[new_position]
#         cipher_text +=new_letter
#     print(f"The encoded text is {cipher_text}")

#encrypt(plain_text=text, shift_amount=shift)

"""#Part 2"""

# def decrypt(ciphered_text, shift_amount):
#
#     decipher_text = ""
#     for letter in ciphered_text:
#         position=alphabets_list.index(letter) #gives the index no. of the letter in plain_text
#         new_position= position - shift_amount
#         new_letter= alphabets_list[new_position]
#         decipher_text +=new_letter
#     print(f"The decoded text is {decipher_text}")
#
# #decrypt(ciphered_text=text, shift_amount=shift)
#
#
# if "encode" in direction:
#     encrypt(plain_text=text, shift_amount=shift)
# elif "decode" in direction:
#     decrypt(ciphered_text=text, shift_amount=shift)

"""Part 3"""
# def caesar(gievn_text, shift_amount, given_direction):
#     cipher_text=""
#     decipher_text=""
#
#     for letter in gievn_text:
#         position = alphabets_list.index(letter)
#         if direction == "encode":
#             new_position_encrypt = position+ shift_amount
#             cipher_text += alphabets_list[new_position_encrypt]
#
#         elif direction == "decode":
#             new_position_decrypt = position- shift_amount
#             decipher_text += alphabets_list[new_position_decrypt]
#
#     if direction == "encode":
#         print(f"Your encoded message is {cipher_text}")
#
#     elif direction == "decode":
#         print(f"Your encoded message is {decipher_text}")
#
#     #or
#     result=""
#
#     for letter in gievn_text:
#         position = alphabets_list.index(letter)
#         if direction == "encode":
#             new_position_encrypt = position+ shift_amount
#             result += alphabets_list[new_position_encrypt]
#
#         elif direction == "decode":
#             new_position_decrypt = position- shift_amount
#             result += alphabets_list[new_position_decrypt]
#
#     print(f"Your {given_direction}d message is {result}")
#
# caesar(gievn_text=text, shift_amount=shift, given_direction=direction)

"""#Part 4"""
def caesar(gievn_text, shift_amount, given_direction):
#     result=""
#
#     for letter in gievn_text:
#         if letter in alphabets_list:
#             position = alphabets_list.index(letter)
#             if direction == "encode":
#                 new_position_encrypt = position + shift_amount
#                 result += alphabets_list[new_position_encrypt]
#
#             elif direction == "decode":
#                 new_position_decrypt = position - shift_amount
#                 result += alphabets_list[new_position_decrypt]
#
#         else:
#             result += letter
#
#     if direction == "encode":
#         print(f"Your encoded message is {result}")
#
#     elif direction == "decode":
#         print(f"Your encoded message is {result}")
#
#     else:
#         print("Check spelling of 'encode' or 'decode'")

    #or
    result=""

    for letter in gievn_text:
        if letter in alphabets_list:
            position = alphabets_list.index(letter)
            if direction == "encode":
                new_position_encrypt = position + shift_amount
                result += alphabets_list[new_position_encrypt]

            elif direction == "decode":
                new_position_decrypt = position - shift_amount
                result += alphabets_list[new_position_decrypt]

        else:
            result+= letter

    print(f"Your {given_direction}d message is {result}")
end_state= False
while not end_state:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    #print(text)
    shift = int(input("Type the shift number:\n"))
    shift= shift%25 #used %25 so that, if the shift number becomes > 52. It wont break the code
    #print(shift)

    caesar(gievn_text=text, shift_amount=shift, given_direction=direction)

    decision_run_again= input("\nType 'yes' if you want to try again or type 'no'.")
    if decision_run_again == "no":
        end_state= True
        print("Thank you for using Caesar Cipher")
    elif decision_run_again == "yes":
        end_state= False
    else:
        print("Error")