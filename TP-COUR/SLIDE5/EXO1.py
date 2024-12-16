#Testing The While Loop Until The User Enters No So It Breaks:
while True:
    print("hi")
    string=str(input("Shall we continue?"))
    if(string.lower()=="no"):
        print("okay then")
        break