# Funciones de orden superior
from functools import reduce


def run():

    numeros = [1, 2, 3, 6, 5]
    cuadrados = []

    # Convertir la lista numeros en una lista de numeros al cuadrado con "for"
    print('Convertir la lista numeros en una lista de numeros al cuadrado con "for"')
    for i in numeros:
        cuadrados.append(i**2)

    print('numeros normales')

    for i in range(len(numeros)):
        print(f'indice: {i}, en el elemento: {numeros[i]}')

    print('numeros al cuadrado')

    for i in range(len(cuadrados)):
        print(f'indice: {i}, en el elemento: {cuadrados[i]}')

    print()

    # Convertir la lista numeros en una lista de numeros al cuadrado con "List Comprehensions"
    print('Convertir la lista numeros en una lista de numeros al cuadrado con "List Comprehensions"')

    cuadrados = [i**2 for i in numeros]

    for i in range(len(numeros)):
        print(f'indice: {i}, en el elemento: {numeros[i]}')

    print('numeros al cuadrado')

    for i in range(len(cuadrados)):
        print(f'indice: {i}, en el elemento: {cuadrados[i]}')

    # Convertir la lista numeros en una lista de numeros al cuadrado con "map"
    print('Convertir la lista numeros en una lista de numeros al cuadrado con "map"')

    cuadrados = list(map(lambda x: x**2, numeros))

    for i in range(len(cuadrados)):
        print(f'indice: {i}, en el elemento: {cuadrados[i]}')

    print()

    # Uso de la funcion de orden superior "reduce", primero con "for"
    print('Uso de la funcion de orden superior "reduce"')

    base = 1

    for i in numeros:
        base *= i

    print(base)

    # Uso de la funcion de orden superior "reduce"
    print('Uso de la funcion de orden superior "reduce"')

    lista = reduce(lambda a, b: a * b, numeros)
    print(lista)

if __name__ == '__main__':
    run()
