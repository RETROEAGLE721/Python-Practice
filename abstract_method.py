from abc import ABC, abstractclassmethod

class RBI(ABC):
    @abstractclassmethod
    def printf(self):
        pass
    
    def value(self):
        print("Values are")
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
class SBI(RBI):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c = c
        self.d = d
    
    def printf(self):
        super().value()
        print(self.a,self.b,self.c,self.d)
        
x1 = SBI(10,20,30,40)
x1.printf()