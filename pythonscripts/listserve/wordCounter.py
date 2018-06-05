import os, re, string, fileinput


def count_words(FILE_LIST):
    wordCounter = {}
    table = str.maketrans("","", string.punctuation)
    for FILE_NAME in FILE_LIST:

        if FILE_NAME.find(".txt") == -1:
            continue
        with open(FILE_NAME,'r') as fh:
            for line in fh:
                # Replacing punctuation characters.
                # The split will spit the line into a list.
                word_list = line.translate(table).split()
                for word in word_list:
                    word = word.upper()
                    # Adding  the word into the wordCounter dictionary.
                    if word not in wordCounter:
                        wordCounter[word] = 1
                    else:
                        wordCounter[word] = wordCounter[word] + 1
    return wordCounter


def list_words(FILE_NAME):
    words = []
    with open(FILE_NAME,'r') as fh:
      for line in fh:
        word_list = line.split()
        for word in word_list:
          words.append(word)
    return words


def camel_case_split(word):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
    splitted = [m.group(0) for m in matches]
    if len(splitted) > 1:
        return "\n".join(splitted)
    else:
        return ""


def replace_string(fileToSearch, textToSearch, textToReplace):
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')


def clean_camelcase(FILE_NAME):
    words = list_words(FILE_NAME)
    for word in words:
        toReplace = camel_case_split(word)
        if toReplace:
            replace_string(FILE_NAME, word, toReplace)

files = os.listdir(".")

### CLEAN CAMEL CASE
# for counter, myFile in enumerate(files):
#     if myFile.find(".txt") == -1:
#         continue
#     clean_camelcase(myFile)
#     printString = "Writing {}, Progress {}/{}"
#     print(printString.format(myFile, counter, len(files)), "\r" * len(printString), end='')
# print()

words = count_words(files)
sorted_words = sorted(words, key=words.get, reverse=False)
for counter, word in enumerate(sorted_words):
    print("{} - <{}> ... <{}>".format(counter + 1, word, words[word]))
    
    
    
