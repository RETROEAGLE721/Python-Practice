# def addition(a=None, b=None):
#     a+=b
#     print("value of a is", a)

def addition(a=None,b=None,c=None,d=None):
    if a is not None and b is None and c is None and d is None:
        a = a
    if a is not None and b is not None and c is not None and d is not None:
        a=a+b+c+d
    print("value of a is", a)

# def addition(a=None,b=None,c=None):
#     a = a+b+c
#     print("value of a is", a)

# addition(10,20)
# addition(10,20,30,40)
addition(10)
addition(10,20,30,40)
    