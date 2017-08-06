class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    # Crea el metodo clasificar
    def clasificar(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3 :
            es_un = "equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3 :
            es_un = "isosceles"
        else :
            es_un = "escaleno"
        return es_un
# No alteres el codigo a continuacion
t = Triangulo(int(input()),int(input()),int(input()))
print(t.clasificar())
print("hola2")
print("hola3")