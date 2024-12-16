number=int(input("Please Enter A Number:"))

if(number%3==0):
    if(number%5==0):
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if(number%5==0):
        print("Buzz") 
    else:
        print(number,"Is Neither Divisible By 3 Nor By 5 !")