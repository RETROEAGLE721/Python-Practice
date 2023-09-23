a = input()
b=""
c=[]
for x in range(2,int(a)):
    for i in range(1,x):
        if x%i == 0:
            b = b + "+" + str(i)
    sums = eval(b)
    if sums == x:
        c.append(str(x))
    b = ""
print(" ".join(c))