
import time

def leer_archivo(nombre):
    with open(nombre, 'r') as archivo:
        numeros = archivo.read().split()
        return list(map(int, numeros))

def ordenar(lista):
    return sorted(lista)

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

datos = leer_archivo("datos.txt")

print("Datos cargados correctamente...")

inicio_orden = time.time()
datos_ordenados = ordenar(datos)
fin_orden = time.time()

print(f"Tiempo de ordenamiento: {fin_orden - inicio_orden:.6f} segundos")

numero = int(input("Ingresa el número a buscar: "))

inicio_busqueda = time.time()
resultado = busqueda_binaria(datos_ordenados, numero)
fin_busqueda = time.time()

print("\n RESULTADOS")

if resultado != -1:
    print(f"Número encontrado en la posición {resultado}")
else:
    print("Número no encontrado")

print(f"Tiempo de búsqueda: {fin_busqueda - inicio_busqueda:.6f} segundos")
