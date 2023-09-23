a = input("Enter word :- ")
b =""
for i in range(len(a)):
    b += a[len(a)-i-1]

if a.lower() == b.lower():
    print(a,"is Palindron")
else:
    print(a,"is not Palindron")