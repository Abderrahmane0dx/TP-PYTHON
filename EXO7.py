#declaration d'un dictionnaire ou on va mettre les cités comme des indices et leurs populations comme la valeur:
city_population={}

print("Please Enter City Names One By One And Type 'stop' To Finish.")

while(True):
 cityname=input("Please Enter The Name Of The City:")
 if (cityname == "stop"):
      break
 
 population=len(cityname)*1000000
 city_population[cityname]=population

sorted_cities= sorted(city_population.items(), key=lambda x: x[1], reverse=True)
print("Here Are The Sorted Cities With Thier Populations:")

for city,population in sorted_cities:
   print(f"{city}:{population:,}")

