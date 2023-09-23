n = int(input("Enter the number upto which you have to find fibonacci serise :- "))
a = 0
b=1
print("fibonacci serise is :- 0,1",end=",")
for i in range(int(n/4)):
        c = a + b
        if c > n:
            break
        else:
            print(c,end=",")
            a=b
            b=c
        

