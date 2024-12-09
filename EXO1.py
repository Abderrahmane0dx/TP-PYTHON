name=str(input("Please Enter Your Name:"))

if(name=="VIP"):
    print("Enjoy The Show For Free!")
else:
    ticketnumber=int(input("How Many Tickets Would You Like To Buy ?:"))
    print("The Total Cost Is",ticketnumber*15.5)