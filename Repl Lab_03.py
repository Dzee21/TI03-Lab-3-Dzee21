#Gunting, Kertas, Batu
p1 = input("Masukkan pilihan player 1 = ")
p2 = input("Masukkan pilihan player 2 = ")

if p1 == p2:
    print("Seri")
elif (p1 == "Gunting") and (p2 == "Kertas"):
    print("Player 1 Menang")
elif (p1 == "Batu") and (p2 == "Kertas"):
    print("Player 2 Menang")
elif (p1== "Gunting") and (p2 == "Batu"):
    print("Player 2 Menang")
elif (p1== "Kertas") and (p2 == "Gunting"):
    print("Player 2 Menang")
elif (p1== "Batu") and (p2 == "Gunting"):
    print("Player 1 Menang")
else:
    print("....")

#Harga buku
bk = int(input("Beli buku = "))

if bk >= 1 and bk <=10:
    print("Harga yang harus dibayar = ", bk * 20000)

elif bk >= 11 and bk <=25:
    print("Harga yang harus dibayar = ", bk * 18000)
elif bk >= 26 and bk <=50:
    print("Harga yang harus dibayar = ", bk * 15000)
elif bk > 50:
    print("Harga yang harus dibayar = ", bk * 10000)
else :
       print("Kesalahan") 

#Bilangan bulat
inp = int(input("Masukkan bilangan bulat = "))

for i in range (0,inp):
    if (i%2):
        print("$" * inp)
    else :
        print("#" * inp)