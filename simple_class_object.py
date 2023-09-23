class Device:
    def __init__(self,a):
        self.a = a
    
    def fun(self):
        print("the value of a is",self.a)
        
    def __str__(self):
        return f"{self.a}"
    
p1 = Device(10)
p1.fun()
print(p1)