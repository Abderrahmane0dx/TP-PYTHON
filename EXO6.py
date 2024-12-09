#initialiser le prix à -1 pour que la boucle s'exécute jusqu'à ce que" l'utilisateur donne un prix positif
price=-1

while(price < 0):
    price=float(input("Please Type In A Price:"))
    if(price < 0):
        print("The Price Has To Be A Positif Number, Try Again!")

dinars = int(price // 1)
centimes = int((price % 1) * 100) 
print("The Dinars Of Your Price Are:",dinars)
print("The Centimes Of Your Price Are:",centimes)
