class RBI :
    amount="20000"
    
    def __init__(self,name):
        self.name = name
    
    def printf(self):
        print("%s: %s" % (self.name, self.amount))
    
    @staticmethod
    def get_amount(a,b):
        return a+b
        
x1 = RBI("Dhairya")
x2=RBI("Vishal")

x1.printf()
x2.printf()

x1.amount="10000"
x1.printf()
x2.printf()

RBI.amount="50000"
x1.printf()
x2.printf()

print(RBI.get_amount(5,5))