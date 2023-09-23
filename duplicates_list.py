n = int(input('Enter total number :- '))
a = [] 
c=0
b=0
l = []
print('Enter ',n,'numbers')
for x in range(n):
    a.append(int(input()))

for x in range(len(a)):
    k = a[x]
    if a[x] in l:
        continue
    else:
        l.append(k)
        for i in range(len(a)):            
            if k == a[i]:
                c+=1
        if c==0 or c==1:
            c=0
        else:
            print(k,'is repeated ',c,'times in list')
            b+=1
            c = 0

print('Total number repearted in list are :-',b)
print('List is ',a)