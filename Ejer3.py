import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    # Métodos de cálculo
    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0.0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0.0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)


if __name__ == "__main__":
    entrada_raw = input("Ingrese a, b, c: ")
    partes = entrada_raw.replace(',', ' ').split()

    # Si los 3 números se ingresan juntos (ejemplo: 1.0 3.0 1.0)
    if len(partes) >= 3:
        a = float(partes[0])
        b = float(partes[1])
        c = float(partes[2])
    else:
        
        a = float(partes[0])
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))

    eq = EcuacionCuadratica(a, b, c)
    disc = eq.getDiscriminante()

    if disc > 0:
        print(f"La ecuación tiene dos raíces {eq.getRaiz1():.6g} y {eq.getRaiz2():.6g}")
    elif disc == 0:
        print(f"La ecuación tiene una raíz {eq.getRaiz1():.6g}")
    else:
        print("La ecuación no tiene raíces reales")