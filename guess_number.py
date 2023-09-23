import random;

a = int(random.randrange(1,10))
flag = 0
for x in range(6):
    b = int(input("Enter number between 1 to 9(You have "+str(6-x)+" moves left):-"))
    
    if a == b:
        print("Guessed right")
        flag=1
        break
    else:
        print("Wrong")

if flag ==0:
    print("The number was",a)