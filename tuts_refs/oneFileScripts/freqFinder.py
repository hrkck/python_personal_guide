text = "korkma, sonmez bu safaklarda yuzen al sancak, sonmeden yurdumun ustunde tuten en son ocak, o benimdir o benim milletimin, o benim milletimin yildizidir parlayacak, catma kurban olayim cehreni ey nazli hilal, kahraman irkima bir gul, bu ne siddet, bu celal, sana olmaz dokulen kanlarimiz sonra helal, hakkidir hakka tapan, milletimin istiklal."

kelimeler = text.split(" ")
tekrarlar = []
suzgec = []
# print ( l)

index = []

for j in range(len(kelimeler)):
    x = 0

    for i in range(len(kelimeler)):
        if kelimeler[j] == kelimeler[i]:
            x = x + 1
        else:
            continue
    if kelimeler[j] in index:
        pass
    else:
        index.append(kelimeler[j])
        tekrarlar.append(x)
        suzgec.append(kelimeler[j])

print(len(suzgec))
print(len(tekrarlar))

for i in range(44):
    print(suzgec[i], ", ", tekrarlar[i], " kere tekrarlandi.")

# for i in range(len(kelimeler)):
