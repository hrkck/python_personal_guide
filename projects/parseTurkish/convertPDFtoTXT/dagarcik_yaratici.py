'''
Created on Mar 20, 2016

@author: bloyd
'''


def cimbizla(dosya_ismi, letter_count):

    src = open(dosya_ismi, 'r')
    dst = open("dagarcik.txt", 'w')
    haric = ['/,''!', ')', '(', ',', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', '-', '.', '<', '>', '+']
    dagarcik = []
    for line in src:
        words = line.split()
        for word in words:
            for i in haric:
                if i in word:
                    test = False
                    break
                else:
                    test = True
            if (len(word) <= letter_count) and (word not in dagarcik) and (test):
                dagarcik.append(word)
                word = word + '\n'
                dst.write(word)

    src.close()
    dst.close()


cimbizla('KULLANILABILIR.txt', 3)
