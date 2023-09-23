class RBI:
    def __init__(self, name, amount,):
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return f"the name is {self.name} and amount is {self.amount}"
    
    def namee(self):
        print("From parent name is ",self.name)
        
    def amounte(self):
        print("From parent amount is ",self.amount)
        
    def done():
        print("Transaction completed")
        
class SBI(RBI):
    def __init__(self, name, amount,date):
        super().__init__(name, amount)
        self.date=date
    
    def __str__(self):
        return f"the name is {self.name} , amount is {self.amount} and date is {self.date}"
    
    def namee(self):
        print("From Child name is ",self.name)
        super().namee()
        
    def amounte(self):
        print("From Child amount is ",self.amount)
        super().amounte()
        
    def datee(self):
        print("From Child date is ",self.date)
        
    def done(self):
        print("Transaction completed")

x1=SBI("Dhairya","10,000","10/02/2020")
x1.namee()
x1.amounte()
x1.datee()
print(x1)
x1.done()