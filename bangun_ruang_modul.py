import math

def luas_permukaan_kubus(sisi):
    """Menghitung luas permukaan kubus"""
    return 6 * sisi**2

def luas_permukaan_balok(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok"""
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    """Menghitung luas permukaan tabung"""
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_permukaan_limas(luas_alas, keliling_alas, tinggi_segitiga):
    """Menghitung luas permukaan limas"""
    return luas_alas + (keliling_alas * tinggi_segitiga / 2)

def luas_permukaan_prisma(luas_alas, keliling_alas, tinggi):
    """Menghitung luas permukaan prisma"""
    return 2 * luas_alas + keliling_alas * tinggi
