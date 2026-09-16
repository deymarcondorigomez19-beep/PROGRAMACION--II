import math

class Fraccion:
    def __init__(self, a=0, b=1):
        self.__numerador = a
        self.__denominador = b

    def get_numerador(self):
        return self.__numerador

    def get_denominador(self):
        return self.__denominador

    def __add__(self, o):
        a = self.__numerador * o.__denominador + self.__denominador * o.__numerador
        b = self.__denominador * o.__denominador
        return Fraccion(a, b)

    def __sub__(self, o):
        c = Fraccion(0, 1)
        c.__numerador = (self.__numerador * o.__denominador) - (self.__denominador * o.__numerador)
        c.__denominador = self.__denominador * o.__denominador
        return c

    # 1. Sobrecarga del operador de multiplicación (*)
    def __mul__(self, o):
        a = self.__numerador * o.__numerador
        b = self.__denominador * o.__denominador
        return Fraccion(a, b)

    # 2. Sobrecarga del operador de división (/)
    def __truediv__(self, o):
        a = self.__numerador * o.__denominador
        b = self.__denominador * o.__numerador
        return Fraccion(a, b)

    # 3. Sobrecarga del operador de igualdad (==)
    def __eq__(self, o):
        if isinstance(o, Fraccion):
            f1 = self.simplifica()
            f2 = o.simplifica()
            return f1.__numerador == f2.__numerador and f1.__denominador == f2.__denominador
        return False

    # 4. Convertir a decimal con validación de división entre cero
    def convertirADecimal(self):
        if self.__denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        return self.__numerador / self.__denominador

    # 5. Determina si la fracción dada es el inverso usando el operador *
    def esInverso(self, o):
        producto = self * o
        return abs(producto.convertirADecimal() - 1.0) < 1e-9

    # 6. Convierte una cadena str ("-2/3") en un objeto Fraccion
    @staticmethod
    def parseFraccion(cadena):
        partes = cadena.strip().split('/')
        num = int(partes[0])
        den = int(partes[1]) if len(partes) > 1 else 1
        return Fraccion(num, den)

    # 7. Retorna una nueva fracción simplificada usando el máximo común divisor (MCD)
    def simplifica(self):
        mcd = math.gcd(self.__numerador, self.__denominador)
        num = self.__numerador // mcd
        den = self.__denominador // mcd
        if den < 0:
            num = -num
            den = -den
        return Fraccion(num, den)

    def __str__(self):
        return "{}/{}".format(self.__numerador, self.__denominador)


# --- Programa de prueba ---
if __name__ == "__main__":
    f1 = Fraccion(1, 4)
    f2 = Fraccion(4, 3)

    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 == f2: {f1 == f2}")
    print(f"f1 en decimal: {f1.convertirADecimal()}")
    print(f"f1 y f2 son inversos: {f1.esInverso(f2)}")

    f_parsed = Fraccion.parseFraccion("-2/3")
    print(f"Fracción parseada: {f_parsed}")

    f_simp = Fraccion(14, 28).simplifica()
    print(f"14/28 simplificado: {f_simp}")