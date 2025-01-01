alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(original_text, shift_amount):
#
#     original_text_lower = original_text.lower()
#     encoded_text = ""
#
#     for letter in original_text_lower:
#         if letter in alphabet:
#             new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#             encoded_text += alphabet[new_position]
#         else:
#             encoded_text += letter
#
#     return encoded_text
#
# def decrypt(original_text, shift_amount):
#
#     original_text_lower = original_text.lower()
#     decoded_text = ""
#
#     for letter in original_text_lower:
#         if letter in alphabet:
#             new_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
#             decoded_text += alphabet[new_position]
#         else:
#             decoded_text += letter
#
#     return decoded_text

def caesar(original_text, shift_amount, action):

    original_text_lower = original_text.lower()
    output = ""

    if action == "decode":
        shift_amount *= -1

    for letter in original_text_lower:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output += alphabet[new_position]
        else:
            output += letter

    print(f"The {action}d text is {output}")



repeat = True
while repeat:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Invalid input")
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if restart != "yes":
        repeat = False
        print("Goodbye")
        
