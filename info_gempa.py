#memanggil file gempa
from Gempa import *

#Membuat Objek
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)

#Informasi Gempa
print('## Info Gempa Maseh ##')
print()
gempa1.dampak()

print('## Info Gempa Maseh ##')
print()
gempa2.dampak()

print('## Info Gempa Maseh ##')
print()
gempa3.dampak()

print('## Info Gempa Maseh ##')
print()
gempa4.dampak()

print('## Info Gempa Maseh ##')
print()
gempa5.dampak()