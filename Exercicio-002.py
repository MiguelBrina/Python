class Retangulo:

    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor < 0:
          print("Altura inválida")

        else:
             self._altura = valor 
    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor < 0:
            print("Largura inválida")
        else:
            self._largura = valor

    @property
    def area(self):
        return self._altura * self._largura

r = Retangulo(5,10)

print(r.area)
