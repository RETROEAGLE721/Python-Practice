class RBI:
    def __init__(self,a,b):
        self._a = a
        self.b = b
    
    def printf(self):
        print("value of a =",self._a,"b =",self.b)

class AXIS:
    def __init__(self,c,d):
        self.__c = c
        self.d =d
    
    def printf(self):
        print("value of c =",self.__c,"d =",self.d)
    
class SBI(RBI,AXIS):
    def __init__(self,a,b,c,d,e,f):
        super(SBI,SBI).__init__(a,b)
        super(AXIS,AXIS).__init__(c,d)
        self.e=e
        self.f=f
        
    def printf(self):
        super().printf()
        super().printf()
        print("value of e =",self.e, "f =",self.f)
        
x1=SBI(10,20,30,40,50,60)
x1.printf()