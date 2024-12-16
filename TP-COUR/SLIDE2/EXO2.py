number1=int(input("Please Enter The First Number:"))
number2=int(input("Please Enter The Second Number:"))

operation=str(input("Please Enter An Operation:"))

if operation.lower() == "add":
    print("The Summation Of",number1,"And",number2,"Is:",number1+number2)
elif operation.lower() == "multiply":
    print("The multiplication Of",number1,"And",number2,"Is:",number1*number2)
elif operation.lower() == "substract":
    print("The substraction Of",number1,"And",number2,"Is:",number1-number2)
elif operation.lower() == "divide":
    if number2 == 0:
        print("The Division Is Impossible Number2 Equals 0")
    else:
        print("The Division Of",number1,"By",number2,"Is:",number1/number2)
else:
    print("This Is An Indefined Operation !")