def run():

    my_dict = dict()

    print('Imprimir con ""List comprehension"", un diccionario que tenga los primero 100 numeros naturales de llave, y de valor que tenga el cubo de la llave')

    print('Codigo normal')

    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i**2

    for k, v in my_dict.items():
        print(k, '|', v)

    print('Codigo con list comprehension')

    # List comprehension
    my_dict = {i: i**2 for i in range(1,101) if i % 3 != 0}

    for k, v in my_dict.items():
        print(k, '|', v)

    print('excersise 1, write 1000 dicts, with the value "key" is the numbers by 1 to 1000, and de value of dictionary is the square value key')

    numeros = {i: i**0.5 for i in range(1001)}

    for k, v in numeros.items():
        print(k, '|', v)

if __name__ == '__main__':
    run()