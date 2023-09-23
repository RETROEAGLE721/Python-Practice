a = input("Enter 4-digit binary number")
b=0

if a[0]=="0" or a[0]=="1" and a[1]=="0" or a[1]=="1" and a[2]=="0" or a[2]=="1" and a[3]=="0" or a[3]=="1" :
    if a[0] == "1" :
        b += 8
    if a[1] == "1":
        b += 4
    if a[2] == "1":
        b += 2
    if a[3] == "1":
        b += 1
    if a == "0000":
        print("Entered number is 0")
    
    print("Entered number is ",b)
else :
    print("Number is not binary number")