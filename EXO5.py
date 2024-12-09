name1=str(input("Please Enter The First Runner's Name:"))
time1=float(input("Please Enter The First Runner's Time:"))
name2=str(input("Please Enter The Second Runner's Name:"))
time2=float(input("Please Enter The Second Runner's Time:"))

print("Runner 1:")
print("Name:",name1)
print(name1,"'s Time (In Seconds):",time1)
print("Runner2:")
print("Name:",name2)
print(name2,"'s Time (In Seconds):",time2)

if (time2 < time1):
   print("The Fastest Runner is:",name2)
elif (time2 > time1):
   print("The Fastest Runner is:",name1)
else:
   print(name1,"And",name2,"Have The Same Time")