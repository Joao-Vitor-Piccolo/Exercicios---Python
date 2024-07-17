from random import randint
i = 0


def montar_matriz_rdm():
    listas = int(input('Digite a quantia de listas: '))
    itens = int(input('Digite a quantia de itens: '))
    matriz = [[randint(1, 21) for itens in range(itens)] for listas in range(listas)]
    return matriz


def print_matriz(matriz):
    print()
    global i
    i += 1
    frufru = len(matriz[0]) * 3
    print(f'Matriz {i}: ')
    print('=*=' * frufru)
    for lista in matriz:
        for elemento in lista:
            print(f'=[{elemento:^5}]', end='=')
        print()
    print('=*=' * frufru)


def multiplica_matriz(matriz1, matriz2):
    matriz3 = [[0 for linha in range(len(matriz1))] for coluna in range(len(matriz2[0]))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            matriz3[i][j] = soma
    return matriz3


def montar_matriz_nula():
    listas = int(input('Digite a quantia de listas: '))
    itens = int(input('Digite a quantia de itens: '))
    matriz = [[0 for itens in range(itens)] for listas in range(listas)]
    return matriz


if __name__ == '__main__':
    matriz = montar_matriz_nula()
    print_matriz(matriz)
