import time
import random

class Cronometro:
    def __init__(self):
        # Inicializa la hora actual en milisegundos
        self.__inicia = time.time() * 1000
        self.__finaliza = self.__inicia

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = time.time() * 1000

    def detener(self):
        self.__finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


def ordenacion_por_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --- Programa de Prueba ---
if __name__ == "__main__":
    TAMANO = 100000
    print(f"Generando {TAMANO:,} números aleatorios...")
    numeros = [random.randint(1, 1000000) for _ in range(TAMANO)]

    cronometro = Cronometro()
    print("Iniciando la ordenación por selección...")
    cronometro.inicia()
    ordenacion_por_seleccion(numeros)
    cronometro.detener()

    tiempo_ms = cronometro.lapsoDeTiempo()
    print(f"Tiempo transcurrido: {tiempo_ms:.2f} ms ({tiempo_ms / 1000:.2f} segundos)")