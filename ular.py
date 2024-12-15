from animal import animal

class Ular(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang_tubuh, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang_tubuh = panjang_tubuh
        self.berbisa = berbisa

    def info_ular(self):
        super().info_animal()
        print("Panjang Tubuh\t\t:", self.panjang_tubuh, "meter")
        print("Berbisa\t\t:", self.berbisa)

ular1 = Ular("Python", "Daging", "Darat", "Bertelur", 5, "Tidak")
ular2 = Ular("Kobra", "Daging", "Darat", "Bertelur", 3, "Ya")
ular3 = Ular("Boa", "Daging", "Darat", "Melahirkan", 4, "Tidak")

print("\n## Info Ular ##")
ular1.info_ular()
print()
ular2.info_ular()
print()
ular3.info_ular()
