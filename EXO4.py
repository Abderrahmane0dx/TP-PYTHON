age1=int(input("Please Type In The Age Of The First Person:"))
age2=int(input("Please Type In The Age Of The Second Person:"))

if (age1 > age2):
    print("The Oldest Person Is The First One With The Age Of:",age1)
elif (age1 < age2):
    print("The Older Person Is The Second One With The Age Of:",age2)
else:
    print("Both People Are The Same Age!")