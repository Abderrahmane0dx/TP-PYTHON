purchase=int(input("Please Enter The Total Amount Of The Purchase:"))
itemnumber=int(input("Please Enter The Number Of Items:"))
day=str(input("Please Enter The Day Of The Week:"))

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#weekend = ["Saturday", "Sunday"]

if day in weekdays:
    purchase=purchase-(purchase*10)/100
else:
    purchase=purchase-(purchase*20)/100 

if (itemnumber>=5):
    print("Total Price After Discount Is:",purchase-purchase*5/100) 
else:
    print("Total Price After Discount Is:",purchase)