class Fraccion:
    def_init_(self,numerador,denominador):
        self.num= numerador
        self.den= denominador
    def show(self):
        print(self.num,"/",self.den)
x=Fraccion(1,2)
y=Fraccion(2,3)
print(x.show())
print(y.show())


