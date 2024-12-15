from animal import animal

class Ikan(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat

    def info_ikan(self):
        super().info_animal()
        print("Bernapas Menggunakan\t:", self.bernafas)
        print("Habitat\t\t:", self.habitat)
        
ikan1 = Ikan("Guppy", "Plankton", "Air Tawar", "Bertelur", "Insang", "Air Tawar")
ikan2 = Ikan("Hiu", "Daging", "Air Asin", "Melahirkan", "Insang", "Air Asin")
ikan3 = Ikan("Koi", "Pelet", "Air Tawar", "Bertelur", "Insang", "Air Tawar")

print("\n## Info Ikan ##")
ikan1.info_ikan()
print()
ikan2.info_ikan()
print()
ikan3.info_ikan()