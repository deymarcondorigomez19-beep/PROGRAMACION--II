import math

def promedio(datos):
    n = len(datos)
    if n == 0:
        return 0.0
    
    suma = 0.0
    for x in datos:
        suma += x
    return suma / n

def desviacion(datos):
    n = len(datos)
    if n <= 1:
        return 0.0
    
    prom = promedio(datos)
    suma_cuadrados = 0.0
    for x in datos:
        suma_cuadrados += (x - prom) ** 2
        
    return math.sqrt(suma_cuadrados / (n - 1))


if __name__ == "__main__":
    print("Ingrese 10 números:")
    
    numeros = []
    while len(numeros) < 10:
        linea = input()
        partes = linea.replace(',', ' ').split()
        for valor in partes:
            numeros.append(float(valor))
            if len(numeros) == 10:
                break

    prom = promedio(numeros)
    desv = desviacion(numeros)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estandard es {desv:.5f}")