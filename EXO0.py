peoplenumber=int(input("How Many People Need A Ride ?:"))
fitnumber=int(input("How Many People That Can Fit In One Taxi ?:"))

if(peoplenumber%fitnumber==0):
    print("Number of taxis needed:",peoplenumber//fitnumber)
else:
    print("Number of taxis needed:",peoplenumber//fitnumber+1)