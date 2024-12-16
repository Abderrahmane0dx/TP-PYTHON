#tant que l'utilisateur n'a pas entré une chaine vide le programe demande toujours une chaine pour l'afficher:
while True:
    string=str(input("Please Type In A String:"))
    print("This Is The String That You Have typed:",string)
    if (string==""):
          break