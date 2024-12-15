class animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
       print ("Name\t\t:" , self.name, "\nMakanan\t\t:", self.makanan, "\nHidup\t\t:", self.hidup, "\nBerkembang Biak\t\t:", self.berkembang_biak)
    
# kucing = Animal("Kucing", "Daging", "Hidup", "Melahirkan")

# kucing.info_animal()