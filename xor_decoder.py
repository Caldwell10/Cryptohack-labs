# Function to XOR each character of a string with a given integer (13 in this case)
def xor_string_with_13(input_string):
    # Initialize an empty list to hold the XORed characters

    xor_result = []

    # Iterate through each character in the input string
    for char in input_string:
        # XOR the ASCII value of the character with 13
        xor_char=chr(ord(char) ^ 13)

        # append result into the list
        xor_result.append(xor_char)

    return ''.join(xor_result)

#string in context
string="label"

#xor the string and create the flag
new_string = xor_string_with_13(string)

#print the resulting flag
print(f'crypto{new_string}')