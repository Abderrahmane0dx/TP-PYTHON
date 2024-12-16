number=int(input("Give The Bumber Of The Stars In The Base:"))

row="*"
while(number  > 0):
    print(" "*number+row)
    row += "**"
    number -= 1