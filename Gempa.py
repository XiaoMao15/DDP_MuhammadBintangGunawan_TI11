class Gempa:
    #konstruktor lokasi dan skala
    
    def __init__(self, lokasi, skala):
        
        #atribut
        self.lokasi = lokasi
        self.skala = skala
        
        #method
    def dampak(self):
        
        #statement
        if self.skala < 2:
            print('Dampak Gempa tidak Berasa ')
        elif self.skala >= 2 and self.skala <= 4:
            print('Dampak Gempa Bangunan Retak-Retak ')
        elif self.skala > 4 and self.skala <= 6:
            print('Dampak Gempa Bangunan roboh ')
        elif self.skala > 6:
            print('Dampak Gempa Tsunami')
            
        print(f'lokaksi Gempa: {self.lokasi} ')
        print(f'Skala Gempa: {self.skala} ')