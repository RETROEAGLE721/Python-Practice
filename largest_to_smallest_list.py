a = []
print("Enter Total number of string :-")
j = int(input())

print("Enter",j," string")
for x in range(j):
    a.append(input())
d = a.copy()
c = a[0]
b =[]
for i in a :
    if c > i:
        c = i
p=c
for i in range(len(a)):
    for x in range(len(d)):
        if c < d[x]:
            c=d[x]
    if c in d:
        d.remove(c)
    b.append(c)
    c = p
print("Largest to Smallest value in List is :-",b)
b.sort()
print("Largest to Smallest value in List is :-",b)