class FormasGeometricas:
    def calcula_area(self):
        print("Não é possível calcular a área de FormaGeometrica")
    
    def desenha(self):
        print("Não sei desenhar a FormaGeometrica")

class Quadrado(FormasGeometricas):
    def __init__(self, lado):
        self.lado = lado

    def calcula_area(self):
        return self.lado * self.lado

    def desenha(self):
        for i in range(self.lado):
            for j in range(self.lado):
                print("*", end="")
            print()

class Circulo(FormasGeometricas):
    pi = 3.14159

    def __init__(self, raio):
        self.raio = raio

    def desenha(self):
        for y in range(-self.raio, self.raio + 1):
            for x in range(-self.raio, self.raio + 1):
                if x*x + y*y <= self.raio*self.raio:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    def calcula_area(self):
        return Circulo.pi * (self.raio**2)

# Criação de objetos
f = FormasGeometricas()
q1 = Quadrado(lado=7)
q2 = Quadrado(lado=8)
c1 = Circulo(raio=5)
c2 = Circulo(raio=20)
