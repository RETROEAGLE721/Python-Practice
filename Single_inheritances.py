class fin:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"values for {self.a} and values for {self.b}"
    
    def fun(self):
        print("parent class finished")
        
class gin(fin):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d = d
        
    def __str__(self):
        return f"values for {self.a} and values for {self.b} and values for {self.c} and values for {self.d}"
    
    def gun(self):
        print("child class finished")
        super().fun()

x1=gin("10","20","30","40")
print(x1)
x1.gun()
