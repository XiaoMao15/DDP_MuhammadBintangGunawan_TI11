import math

def luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi**2

def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

def luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga"""
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran"""
    return math.pi * jari_jari**2

def luas_trapesium(alas1, alas2, tinggi):
    """Menghitung luas trapesium"""
    return 0.5 * (alas1 + alas2) * tinggi
