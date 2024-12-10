string=str(input("Please Enter A String:"))

#on calcule la moitier de la chaine pour savoir combien on laisse de l'espace pour elle:
halfstring=int(len(string)/2)
#nombre de * qu'on va entourer la chaine avec:
frame='*'*(15-halfstring)

if(len(string)%2==0):
 print(frame,string,frame)
else:
 #si la chaine est impaire on fait soustraire une étoile de gauche ou de la droite pour que toujours le nombre total de caractère soit à 30:
 frameodd='*'*(15-halfstring-1)
 print(frameodd,string,frame)
