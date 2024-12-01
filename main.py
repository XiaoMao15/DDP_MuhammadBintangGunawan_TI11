from aritmatika_modul import *

def aritmatika_modul():
    print("\nPilih operasi aritmatika yang ingin dilakukan:")
    print("1.Penambahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Pangkat")
    pilihan = int(input("\nMasukan Nomor aritmatika yang dipilh(1-5):"))
    
    if pilihan ==1:
        a=float(input("Masukkan angka pertama:"))
        b=float(input("Masukkan angka kedua::"))
        print("Hasil Penambahan:",tambah(a,b))
    elif pilihan ==2:
        a=float(input("Masukkan angka pertama:"))
        b=float(input("Masukkan angka kedua::"))
        print("Hasil Pengurangan:",kurang(a,b))
    elif pilihan ==3:
        a=float(input("Masukkan angka pertama:"))
        b=float(input("Masukkan angka kedua::"))
        print("Hasil Perkalian:",kali(a,b))
    elif pilihan ==4:
        a=float(input("Masukkan angka pembilang:"))
        b=float(input("Masukkan angka penyebut (tidak boleh nol)::"))
        print("Hasil Pembagian:",bagi(a,b))
    elif pilihan ==5:
        a=float(input("Masukkan angka dasar:"))
        b=float(input("Masukkan angka pangkat::"))
        print("Hasil Eksponensial:",pangkat(a,b))
    else:
        print("Pilihan tidak valid")
        

#Bangun Datar

from bangun_datar_modul import *  # Import modul bangun datar

def bangun_datar_modul():
    print("\nPilih operasi bangun datar:")
    print("1. Luas Persegi")
    print("2. Luas Persegi Panjang")
    print("3. Luas Segitiga")
    print("4. Luas Lingkaran")
    print("5. Luas Trapesium")
    pilihan = int(input("\nMasukkan nomor bangun datar yang dipilih (1-5): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print("Luas Persegi:", luas_persegi(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        print("Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print("Luas Segitiga:", luas_segitiga(alas, tinggi))
    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        print("Luas Lingkaran:", luas_lingkaran(jari_jari))
    elif pilihan == 5:
        alas1 = float(input("Masukkan panjang alas pertama trapesium: "))
        alas2 = float(input("Masukkan panjang alas kedua trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        print("Luas Trapesium:", luas_trapesium(alas1, alas2, tinggi))
    else:
        print("Pilihan tidak valid.")
        
#Bangun Ruang

from bangun_ruang_modul import *  # Import modul bangun ruang

def bangun_ruang_modul():
    print("\nPilih operasi bangun ruang:")
    print("1. Luas Permukaan Kubus")
    print("2. Luas Permukaan Balok")
    print("3. Luas Permukaan Tabung")
    print("4. Luas Permukaan Limas")
    print("5. Luas Permukaan Prisma")
    pilihan = int(input("\nMasukkan nomor bangun ruang yang dipilih (1-5): "))
    
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        print("Luas Permukaan Kubus:", luas_permukaan_kubus(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        print("Luas Permukaan Balok:", luas_permukaan_balok(panjang, lebar, tinggi))
    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari-jari alas tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        print("Luas Permukaan Tabung:", luas_permukaan_tabung(jari_jari, tinggi))
    elif pilihan == 4:
        luas_alas = float(input("Masukkan luas alas limas: "))
        keliling_alas = float(input("Masukkan keliling alas limas: "))
        tinggi_segitiga = float(input("Masukkan tinggi segitiga pada sisi limas: "))
        print("Luas Permukaan Limas:", luas_permukaan_limas(luas_alas, keliling_alas, tinggi_segitiga))
    elif pilihan == 5:
        luas_alas = float(input("Masukkan luas alas prisma: "))
        keliling_alas = float(input("Masukkan keliling alas prisma: "))
        tinggi = float(input("Masukkan tinggi prisma: "))
        print("Luas Permukaan Prisma:", luas_permukaan_prisma(luas_alas, keliling_alas, tinggi))
    else:
        print("Pilihan tidak valid.")


# Menu untuk memilih modul
print("\n--- Modul Perhitungan ---")
print("1. Aritmatika")
print("2. Bangun Datar")
print("3. Bangun Ruang")
pilihan_modul = int(input("Pilih modul (1-3): "))

if pilihan_modul == 1:
    aritmatika_modul()
elif pilihan_modul == 2:
    bangun_datar_modul()
elif pilihan_modul == 3:
    bangun_ruang_modul()
else:
    print("Pilihan modul tidak valid.")
