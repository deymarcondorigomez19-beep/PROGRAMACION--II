import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    def get_x(self): return self.__x
    def get_y(self): return self.__y
    def get_z(self): return self.__z

    # a) Suma de dos vectores: c = a + b
    def __add__(self, o):
        return Vector3D(self.__x + o.__x, self.__y + o.__y, self.__z + o.__z)

    # b) y e) Multiplicación por un escalar (r * a) o Producto Escalar (a . b)
    def __mul__(self, o):
        if isinstance(o, (int, float)):
            return Vector3D(self.__x * o, self.__y * o, self.__z * o)
        elif isinstance(o, Vector3D):
            return self.__x * o.__x + self.__y * o.__y + self.__z * o.__z

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    # c) Longitud o magnitud de un vector: |a|
    def magnitud(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    # División por escalar para calcular vectores
    def __truediv__(self, escalar):
        return Vector3D(self.__x / escalar, self.__y / escalar, self.__z / escalar)

    # d) Normal de un vector: b = a / |a|
    def normal(self):
        mag = self.magnitud()
        if mag == 0:
            raise ZeroDivisionError("No se puede normalizar un vector nulo.")
        return self / mag

    # f) Producto vectorial: a ^ b (operador XOR ^ sobrecargado)
    def __xor__(self, o):
        cx = self.__y * o.__z - self.__z * o.__y
        cy = self.__z * o.__x - self.__x * o.__z
        cz = self.__x * o.__y - self.__y * o.__x
        return Vector3D(cx, cy, cz)

    def __str__(self):
        return "({}, {}, {})".format(self.__x, self.__y, self.__z)


# --- Programa de prueba ---
if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)

    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("3 * a =", 3 * a)
    print("|a| =", round(a.magnitud(), 4))
    print("Normal de a =", a.normal())
    print("Producto escalar (a . b) =", a * b)
    print("Producto vectorial (a x b) =", a ^ b)