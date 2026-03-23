class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    @property
    def area(self):
        return self.altura * self.largura 
    
r = Retangulo(5,10)

print(r.area)