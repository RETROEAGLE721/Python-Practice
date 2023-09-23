for x in range(1,20):
    print("Factors of ",x," are:- ")
    for a in range(1,x+1):
        if x%a == 0 :
            print(a)
