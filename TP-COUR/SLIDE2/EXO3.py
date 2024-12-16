#Temperature Conversion Program:

temperatureF=int(input("Please Type In A Temperature (F:In Fahrenheit):"))

celsius = 5/9*(temperatureF-32)

print(temperatureF,"Degrees Fahreneit Equals",celsius,"Degrees Celsius")

if celsius < 0:
    print("Brr! It's Cold In Here!")