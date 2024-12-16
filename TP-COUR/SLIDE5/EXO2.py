from math import sqrt
while True:
    number=int(input("Give A Number:"))

    if(number < 0):
        print("Invalid Number")
    elif(number > 0):
        print("The Square Root Of",number,"is:",sqrt(number))
    else:
        break
    