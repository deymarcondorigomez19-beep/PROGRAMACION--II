import math

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y

    def producto_cruz(self, otro):
        return self.x * otro.y - self.y * otro.x

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class AlgebraVectorial:
    # Sobrecarga de criterios de Perpendicularidad
    @staticmethod
    def perpendicular(a: Vector2D, b: Vector2D, criterio=1):
        if criterio == 1:
            # a) |a + b| == |a - b|
            return abs((a + b).magnitud() - (a - b).magnitud()) < 1e-9
        elif criterio == 2:
            # b) |a - b| == |b - a|
            return abs((a - b).magnitud() - (b - a).magnitud()) < 1e-9
        elif criterio == 3:
            # c) a . b == 0
            return abs(a.producto_escalar(b)) < 1e-9
        elif criterio == 4:
            # d) |a + b|² == |a|² + |b|²
            lhs = (a + b).magnitud()**2
            rhs = a.magnitud()**2 + b.magnitud()**2
            return abs(lhs - rhs) < 1e-9

    # Sobrecarga de Paralelismo
    @staticmethod
    def paralela(*args):
        if len(args) == 3:
            a, b, r = args[0], args[1], float(args[2])
            # e) a == r * b
            rb = b * r
            return abs(a.x - rb.x) < 1e-9 and abs(a.y - rb.y) < 1e-9
        elif len(args) == 2:
            a, b = args[0], args[1]
            # f) a x b == 0
            return abs(a.producto_cruz(b)) < 1e-9

    # g) Proyección ortogonal de a sobre b
    @staticmethod
    def proyeccion_de_a_sobre_b(a: Vector2D, b: Vector2D):
        factor = a.producto_escalar(b) / (b.magnitud()**2)
        return b * factor

    # h) Componente de a en la dirección de b
    @staticmethod
    def componente_de_a_en_b(a: Vector2D, b: Vector2D):
        return a.producto_escalar(b) / b.magnitud()


# --- Programa de prueba ---
if __name__ == "__main__":
    v1 = Vector2D(0, 3)
    v2 = Vector2D(4, 0)

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Perpendicular (Criterio a . b = 0):", AlgebraVectorial.perpendicular(v1, v2, criterio=3))
    print("Proyección de v1 sobre v2:", AlgebraVectorial.proyeccion_de_a_sobre_b(v1, v2))
    print("Componente de v1 en v2:", AlgebraVectorial.componente_de_a_en_b(v1, v2))