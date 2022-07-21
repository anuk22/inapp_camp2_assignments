class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("addition",self.a+self.b)
    def mul(self):
        print("multiplication ",self.a*self.b)
    def div(self):
        print("division ",self.a/self.b)
    
calc=calculator(10,5)
calc.add()
calc.mul()
calc.div()