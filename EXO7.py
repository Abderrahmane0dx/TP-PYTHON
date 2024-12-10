year=int(input("Please Enter A Year:"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
          print(year,"Is A Leap Year!")
        else:
          print(year,"Is Not A Leap Year!")
    else:
        print(year,"Is A Leap Year!")
else:
    print(year,"Is Not A Leap Year!")