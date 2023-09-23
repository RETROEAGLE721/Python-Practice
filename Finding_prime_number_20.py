flag = 0

for i in range(1,20):
    for a in range(2,i):
        if i%a == 0:
            flag=1
            break
    if flag == 0 :
        print(i , "is prime number")
    flag = 0