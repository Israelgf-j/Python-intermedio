def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Israel", "lastname": "Gutierrez"}

    super_list = [
        {"firstname": "Israel", "lastname": "Gutierrez"},
        {"firstname": "Oscar", "lastname": "García"},
        {"firstname": "Brayan", "lastname": "Flores"},
        {"firstname": "Fernanda", "lastname": "Montes"},
        {"firstname": "Raul", "lastname": "Gasca"},
    ]

    super_dicts = {
        "natural_nums": [1, 2, 3, 4],
        "prims_nums": [2, 3, 5, 7, 11],
        "negative_nums": [-1, -2, -3, -4]
    }

    print('Impresion de un super diccionario, un diccionario con diccionarios dentro\n')
    for key, value in super_dicts.items():
        print(key, "-", value)

    print()

    print('Impresion de una super lista, una lista con diccionarios dentro\n')
    for i in enumerate(super_list):
        print(i)

    print()

    for i in super_list:
        print(i)



if __name__ == '__main__':
    run()