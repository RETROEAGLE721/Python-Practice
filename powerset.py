def power(a):
    c = []
    b=[]
    b.append([])
    for i in a:
        c.append(i)
        b.append(c)
        c= []
    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            c.append(a[i])
            c.append(a[j])
            b.append(c)
            c= []
    b.append(a)
    print(b)

a=[]
print("Enter 3 Integer:-")
for i in range(3):
    a.append(int(input()));
power(a)