for i in range(6):
    for x in range(i):
        print("*",end="")
    print()
    
    
for i in range(6):
    for x in range(5-i):
        print("*",end="")
    print()
    
    
for i in range(6):
    for x in range(i):
        print(" ",end="")
    for j in range(5,i,-1):
        print("*",end="")
    print()
    
    
for i in range(6):
    for x in range(5-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    for x in range(i):
        print("*",end="")
    print()