"""
Think Twice to solve.
"""
myText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

url = "map"

ocr = "aeilquty"
def decode(text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    words = text.split()
    for i, word in enumerate(words):
        word = list(word)
        for j, letter in enumerate(word):
            if not letter.isalpha():
                print(letter)
                word[j] = letter
            pos = letters.find(letter.upper()) + 2
            if pos > 25:
                pos -= 26
            word[j] = letters[pos]
        words[i] = word
    sentence = ""
    for item in words:
        item = "".join(item)
        sentence += item + " "
    return sentence


print(decode(ocr))
