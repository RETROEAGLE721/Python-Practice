
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

j = float(input("ENTER 1ST NUJMBER "))
l = float(input("ENTER 2ND NUJMBER "))
c = int(input("1.ADD\n 2.SUB\n 3.MUL\n 4.DIV\n ENTER ANU ONE NUMBER :-"))

if c==1:
       print("ADD IS ",add(j,l))
elif c==2:
        print("SUB IS ",sub(j, l))
elif c==3:
        print("MUL IS ",mul(j, l))
elif c==4:
        print("DIV IS ",div(j,l))
else:
    print("INVALID NUMBER")
    
print("PROGRAM OVER")
