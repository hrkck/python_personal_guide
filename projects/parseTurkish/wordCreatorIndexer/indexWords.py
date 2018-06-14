# -*- coding: utf-8 -*-
'''
Created on Apr 11, 2016

@author: bloyd
'''

isimdenIsimYapanEkler = ['lık', 'lik', 'luk', 'lük', 'lı', 'li', 'sız', 'siz', 'suz', 'süz', 'cı', 'çı', 'ci', 'çi', 'cu', 'cü', 'ce', 'çe', 'daş',
                         'inci', 'üncü', 'ıncı', 'msı', 'msi', 'cıl', 'cil', 'şın', 'sal', 'ıt', 'it', 'cağız', 'ceğiz', 'cık', 'cik', 'cük', 'tu', 'tı', 'ti', 'tü']

kelimeler = open("kelimeler.txt", 'r')
isimler = open("isimler.txt", 'w')


for line in kelimeler:
    p = line[:3]
    isimler.write(p)


'''for line in kelimeler:
    for ek in isimdenIsimYapanEkler:
        sondan = len(ek)
        sondan += 1
        if ek in line[:sondan]:
            isimler.write(line)
            break
            '''
