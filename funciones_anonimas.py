# Funciones anónimas

#funcion anónima palíndromo

def run():

    print('funcion anónima palíndromo')
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))

    print()

    y = 1
    x = 3

    print('sumar con una expresion lambda dos numeros')
    sumar_lambda = lambda a, b: a + b
    print(f'La suma de {y} + {x} es igual a {sumar_lambda(x, y)}')

    print()

    print('Exponente de un numero con lambda')
    exponent_lambda = lambda a, b: a**b
    print(f'La exponenciacion de {x} a la {y} es: {exponent_lambda(x, y)}')




if __name__ == '__main__':
    run()