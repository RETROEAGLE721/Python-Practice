a = int(input("ENTER 1ST VALUE "))
b = int(input("ENTER 2ND VALUE "))
c = int(input("ENTER 3RD VALUE "))

if a>b and a>c: 
    print("{0} IS GREATER THAN {1} AND {2}".format(a,b,c))
elif b>a and b>c:    
    print(b,"IS GRETAER THAN ",a," AND ",c)
else:
    print(c,"IS GREATER THAN ",a," AND ",b)
    
