import abc 

class RBI(abc.ABC):
    @abc.abstractmethod
    def printf(self):
        pass
    
    @abc.abstractmethod
    def done(self):
        pass
    
class SBI(RBI):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def printf(self):
        print(self.a, self.b)
        
    def done(self):
        print("done")
    
x1 = SBI(10,20)
x1.printf()
x1.done()