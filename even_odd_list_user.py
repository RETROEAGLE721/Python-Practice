a = []
n=int(input('Enter Total number:-'))
print('Enter ',n,' number')
for i in range(n):
    a.append(int(input()))

for i in range(len(a)):
    if a[i]%2 == 0 :
        print(a[i],"is even number")
    else:
        print(a[i],'is odd number')