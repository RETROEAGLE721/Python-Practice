a= input("Enter any sentance:- ")
print("Befor adding:-",a)
a = a.split(" ")

print("After adding:- ",end=" ")
for x in a:
    c = list(x)
    if c[0].isdigit():
        x = int(x)
        x += 5
        print(x,end=" ")
    else:
        print(x,end=" ")


