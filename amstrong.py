a = int(input("Enter Number:- "))
c = a
b=0

while a!=0:
    t = int(a%10)
    b = b + (t*t*t)
    a = a/10 
    
if c == b:
    print(c,"is amstrong number")
else:
    print(c,"is not an amstrong number")