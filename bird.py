from animal import animal

class Burung(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_paruh, dapat_terbang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_paruh = jenis_paruh
        self.dapat_terbang = dapat_terbang

    def info_burung(self):
        super().info_animal()
        print("Jenis Paruh\t\t:", self.jenis_paruh)
        print("Dapat Terbang\t\t:", self.dapat_terbang)
        
burung1 = Burung("Merpati", "Biji-bijian", "Darat", "Bertelur", "Pendek", "Ya")
burung2 = Burung("Elang", "Daging", "Darat", "Bertelur", "Tajam", "Ya")
burung3 = Burung("Penguin", "Ikan", "Darat dan Laut", "Bertelur", "Pendek", "Tidak")

print("## Info Burung ##")
burung1.info_burung()
print()
burung2.info_burung()
print()
burung3.info_burung()