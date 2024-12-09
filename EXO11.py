width=int(input("Please Enter The Width Of Your Line:"))
height=int(input("Please Enter The height Of Your Line:"))

print("The Width That You Have Chousen Is:",width)
print("The height That You Have Chousen Is:",height)
#usage de la multiplication entre le caractère # et la taille:
print("Here Is Your Rectangle With Hash Characters:")
for i in range(height):
    print('#'*width)
