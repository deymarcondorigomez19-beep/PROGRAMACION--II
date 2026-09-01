class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__d = float(d)
        self.__e = float(e)
        self.__f = float(f)

    # Getters
    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    # Operaciones principales
    def tieneSolucion(self):
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        return denominador != 0

    def getX(self):
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        numerador = (self.__e * self.__d) - (self.__b * self.__f)
        return numerador / denominador

    def getY(self):
        denominador = (self.__a * self.__d) - (self.__b * self.__c)
        numerador = (self.__a * self.__f) - (self.__e * self.__c)
        return numerador / denominador


# --- Programa de Prueba ---
if __name__ == "__main__":
    entrada_raw = input("Ingrese a, b, c, d, e, f: ")
    partes = entrada_raw.replace(',', ' ').split()

    if len(partes) >= 6:
        a = float(partes[0])
        b = float(partes[1])
        c = float(partes[2])
        d = float(partes[3])
        e = float(partes[4])
        f = float(partes[5])
    else:
        a = float(partes[0])
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
        d = float(input("Ingrese d: "))
        e = float(input("Ingrese e: "))
        f = float(input("Ingrese f: "))

    eq = EcuacionLineal(a, b, c, d, e, f)

    if eq.tieneSolucion():
        print(f"x = {eq.getX():.1f}, y = {eq.getY():.1f}")
    else:
        print("La ecuación no tiene solución")