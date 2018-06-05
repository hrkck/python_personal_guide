import random
import os


def create_pass(digits):

    # All necessary variables:
    char_list = ['1', '2', '3', '4', '5', '6', '7', '8', '8', '9', 'q', 'w', 'e', 'r', 't', 'y',
                 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'c', 'v', 'b', 'n',
                 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J',
                 'K', 'L', 'Z', 'C', 'V', 'B', 'N', 'M']
    required_chars = ['~', '!', '@', ' #', '$', '%', '^', '&', '*',
                      '(', ')', '_', '+', '-', '=', ';', ':', '{', '}', '[', ']', '?', '/', '.', ',', '<', '>']
    # Occurrence of 'char_list' is more than one, because I want to increase
    # the possibility of it.
    two_lists = [char_list, char_list, char_list,
                 char_list, required_chars]

    my_string = list("")
    password = ""
    directory = "/home/hrkucuk/sweeties/"
    txt = directory + "DANGER.txt"
    write_out_string = ""
    indicator = "###########"

    # generating the actual password and assigning it to a string:
    req_chars = input("Do you want 'required_characters'? Answer y/n.\n")
    for i in range(digits):
        if (req_chars == 'y'):
            from_list = random.choice(two_lists)
            character = random.choice(from_list)
        if (req_chars == 'n'):
            character = random.choice(char_list)
        my_string.append(character)
    # Converting and assigning the generated pass to a variable:
    password = "".join(my_string)

    # Writing out the password in a txt file.
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(txt, 'a') as txt:
        write_out_string = input("A brief description please:\n")
        write_out_string += "\n" + password + "\n" + indicator
        txt.write("\n\n" + write_out_string)

print(create_pass(20))
