"""

<!--
find rare characters in the mess below:
-->

"""

def frequencies(txt):
    all_chars = dict()
    for item in txt:
        if item not in all_chars.keys():
            all_chars[item] = 1
        elif item in all_chars.keys():
            all_chars[item] += 1
    rares = ""
    for key in all_chars.iterkeys():
        if all_chars[key] < 2:
            rares += key
    return rares

with open("mass.txt", "r") as my_file:
    txt = my_file.read()

result = frequencies(txt)

result
