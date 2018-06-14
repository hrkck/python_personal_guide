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

globalvowellist = []
globalconsonantslist = []
globalwordlist = []

for x in listof_vowels:
    for y in listof_consonants:
        for z in listof_vowels:
            word = []
            if any(x in s for s in listof_kalinunlu):
                if any(z in s for s in listof_kalinunlu):
                    word.append(x)
                    word.append(y)
                    word.append(z)
                    sozcuk = "".join(word)
                    globalvowellist.append(sozcuk)
                else:
                    pass
            elif any(x in s for s in listof_inceunlu):
                if any(z in s for s in listof_inceunlu):
                    word.append(x)
                    word.append(y)
                    word.append(z)
                    sozcuk = "".join(word)
                    globalvowellist.append(sozcuk)
                else:
                    pass
print("---")
for x in listof_consonants:
    for y in listof_vowels:
        for z in listof_consonants:
            word = []
            if x == "ğ":
                pass
            else:
                word.append(x)
                word.append(y)
                word.append(z)
                sozcuk = "".join(word)
                globalconsonantslist.append(sozcuk)

globalwordlist.extend(globalconsonantslist)
globalwordlist.extend(globalvowellist)

print(len(globalvowellist) + len(globalconsonantslist))
print(globalwordlist)
