import random
import time

####
listof_letters = [['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü'], ['b', 'c', 'ç', 'd', 'f',
                                                             'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']]
####
listof_kalinunlu = ['a', 'ı', 'o', 'u']
listof_inceunlu = ['e', 'i', 'ö', 'ü']
####
listof_vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
listof_consonants = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j',
                     'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
####
####
####


def word_creator(word_lenght):
    the_word = []
    for i in range(int(word_lenght) - 1):
        if len(the_word) == 0:
            choosen_list = random.choice(listof_letters)
            choosen_letter = random.choice(choosen_list)
            the_word.append(choosen_letter)
        if any(the_word[i] in s for s in listof_letters[0]):
            choosen_list = listof_letters[1]
            choosen_letter = random.choice(choosen_list)
            the_word.append(choosen_letter)
        elif any(the_word[i] in s for s in listof_letters[1]):
            if any(the_word[0] in s for s in listof_kalinunlu):
                choosen_list = listof_kalinunlu
                choosen_letter = random.choice(choosen_list)
                the_word.append(choosen_letter)
            elif any(the_word[0] in s for s in listof_inceunlu):
                choosen_list = listof_inceunlu
                choosen_letter = random.choice(choosen_list)
                the_word.append(choosen_letter)
            else:
                choosen_list = listof_letters[0]
                choosen_letter = random.choice(choosen_list)
                the_word.append(choosen_letter)
    if the_word[0] == 'ğ':
        pass
    else:
        print("".join(the_word))
        the_word = []


a = 0
while a < 98374789365:
    a += 1
    word_creator(3)
    time.sleep(0.5)
    word_creator(2)
    time.sleep(0.5)
