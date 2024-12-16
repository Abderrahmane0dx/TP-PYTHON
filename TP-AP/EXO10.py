word=str(input("Please Enter A Word:"))

p=False
for i in range(len(word) // 2):
    if( word[i] != word[len(word)-1-i]):
        p=True
        break

if(p):
 print(word,"Is Not A Palandrome")
else:
 print(word,"Is A Palandrome")