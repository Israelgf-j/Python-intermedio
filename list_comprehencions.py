def run():

    """ for i in range(101):
        if i % 3 == 0:
            pass
        else:
            squares.append(i**2)
    """

    #LLENAR UNA LISTA CON LOS 100 PRIMEROS NUM. AL CUADRADO

    squares = [i**2 for i in range(0, 101) if i % 3 == 0]

    print('\nLista de numeros: ', squares)
    print()

    # ex1: Crear una lista de los multiplos de 4, de 6 y de 9 hasta 5 digitos.

    multiples = [i for i in range(1, 99999) if (i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0)]
    print('\nLista de numeros: ', multiples)



if __name__ == '__main__':
    run()
