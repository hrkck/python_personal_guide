'''
Created on Mar 20, 2016

@author: bloyd
'''

# Her turkce karakterden sonra new line var ise sil
# her asteriksten once tab koy.
# her turkce karakterle biten sozcukten sonra bosluk koy
# her son asteriksli cumleden sonra alt satir koy
# bu kadar lan aslinda!

degisiklikler = {'ç\n': 'ç', 'ı\n': 'ı', 'ğ\n': 'ğ', 'ü\n': 'ü', 'ö\n': 'ö',
                 'ş\n': 'ş', 'Ç\n': 'Ç', 'İ\n': 'İ', 'ğ\n': 'ğ', 'Ü\n': 'Ü', 'Ö\n': 'Ö', 'Ş\n': 'Ş'}


def duzeltici(dosya_ismi):

    # Yanlis alt satirlari duzeltmek icin
    #++++++++++++++++++++++++++++++++++++++++++++#
    bozuk = open(dosya_ismi, "r")
    ilk = open("alt_duzeltildi.txt", 'w')
    for line in bozuk:
        for src, target in degisiklikler.items():
            line = line.replace(src, target)
        ilk.write(line)
    bozuk.close()
    ilk.close()
    #--------------------------------------------#

    # Son Asteriksli satirdan sonra alt satira gecmek icin
    #++++++++++++++++++++++++++++++++++++++++++++#
    bozuk = open("alt_duzeltildi.txt", "r")
    ikinci = open("asteriks_duzeltildi.txt", "w")
    for line in bozuk:
        if "*" not in line:
            line = "\n" + line
        ikinci.write(line)
    bozuk.close()
    ikinci.close()
    #--------------------------------------------#

    # Eksik tablari duzetlmek icin
    #++++++++++++++++++++++++++++++++++++++++++++#
    bozuk = open("asteriks_duzeltildi.txt", "r")
    ucuncu = open("DUZGUN.txt", "w")
    for line in bozuk:
        if "*" in line:
            line = line.replace("*", "\t*")
        ucuncu.write(line)
    bozuk.close()
    ucuncu.close()
    #-------------------------------------------#

duzeltici("BuyukTurkceSozluk.txt")
