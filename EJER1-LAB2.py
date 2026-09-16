import math

class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Sobrecarga del método distancia evaluando la firma de parámetros
    def distancia(self, *args):
        if len(args) == 1 and isinstance(args[0], MiPunto):
            otro = args[0]
            return math.sqrt((self.__x - otro.get_x())**2 + (self.__y - otro.get_y())**2)
        elif len(args) == 2:
            x2 = float(args[0])
            y2 = float(args[1])
            return math.sqrt((self.__x - x2)**2 + (self.__y - y2)**2)
        else:
            raise TypeError("Argumentos inválidos para el cálculo de distancia.")

    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)


# --- Programa de prueba ---
if __name__ == "__main__":
    p1 = MiPunto()
    p2 = MiPunto(10, 30.5)

    print("Punto 1:", p1)
    print("Punto 2:", p2)
    print(f"Distancia entre p1 y p2 (Objeto MiPunto): {p1.distancia(p2):.4f}")
    print(f"Distancia entre p1 y (10, 30.5) (Coordenadas): {p1.distancia(10, 30.5):.4f}")