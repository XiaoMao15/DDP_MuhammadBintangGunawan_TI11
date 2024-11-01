jumlah = 0
bilangan = 1

while bilangan <= 19:
    jumlah += bilangan
    print(bilangan, end="")
    
    if bilangan < 19:
        print(" + ", end="")
    
    bilangan += 2

print(" = ", jumlah)
