# Exercicio 1:
"""

def dobro(numero):
    return numero * 2


num = int(input('Digite o numero: '))

print(dobro(num))


"""

# Exercicio 2:
"""

def data(dia, mes, ano):
    return print(f'{dia}/{mes}/{ano}')


dia = str(input('Digite um dia: '))
mes = str(input('Digite um mes: '))
ano = str(input('Digite um ano: '))
data(dia, mes, ano)


"""

# Exercicio 3:
"""

def positivo(num):
    if num > 0:
        return print('Numero positivo')
    return print('Numero negativo')


num = int(input('Numero: '))
positivo(num)

"""

# Exercicio 4:
"""

def square_roof(num):
    if (num ** 0.5) * (num ** 0.5) == num:
        return print('É um quadrado perfeito')
    return print(f'{num}, não é um quadrado perfeito.')


num = int(input('Digite um número: '))
square_roof(num)

"""

# Exercicio 5:
"""

def raio(parametro):
    return print(f'O volume é: {(parametro ** 3) * 3.14 * 4/3:.2f}')


parametro = int(input('Digite o parametro: '))
raio(parametro)


"""

# Exercicio 6:
"""

def tempo(horas, minutos, segundos):
    return print(f'O tempo em segundos é: {horas * 120 + minutos * 60 + segundos}')


horas, minutos, segundos = 1, 10, 20
tempo(horas, minutos, segundos)


"""

# Exercicio 7:
"""

def conversaof(celcius):
    return celcius * (9.0/5.0) + 32.0


num = int(input('Digite um número: '))
print(conversaof(num))

"""

# Exercicio 8:
"""

def hipotenusa(cateto_a, cateto_b):
    return (cateto_a ** 2 + cateto_b ** 2) ** 0.5


num_a = int(input('Digite um número: '))
num_b = int(input('Digite outro numero: '))
print(f'{hipotenusa(num_a, num_b):.3f}')

"""

# Exercicio 9:
"""

def cilindro(altura, raio):
    return 3.14 * (raio ** 2) * altura


print(cilindro(20, 10))

"""

# Exercicio 10:
"""

def maior_num(num1, num2):
    if num1 > num2:
        return num1
    return num2


num_a = int(input('Digite um número: '))
num_b = int(input('Digite outro numero: '))
print(f'{maior_num(num_a, num_b)}')


"""

# Exercicio 11:
"""

def media(nota1, nota2, nota3, letra):
    if letra == 'a':
        return (nota1 + nota2 + nota3) / 3
    return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)


print(media(20, 10, 10, 'b'))


"""

# Exercicio 12:
"""

def retorno(num):
    num = str(num)
    soma = 0
    for i in num:
        soma += int(i)
    return soma

print(retorno(235))

"""

# Exercicio 13:
"""

def consumo(num1, num2, simbulo):
    if simbulo == '+':
        return num1 + num2
    if simbulo == '-':
        return num1 - num2
    if simbulo == '/':
        return num1 / num2
    return print('Simbulo errado vacilão!')


num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
simbulo = str(input('Digite um simbulo: '))
print(consumo(num1, num2, simbulo))


"""

# Exercicio 14:
"""

def consumo(kilometros, consumido):
    valor = kilometros / consumido
    if valor < 8:
        return 'Venda o carro!'
    if 14 > valor >= 8:
        return 'Economico!'
    if valor > 13:
        return 'Super economico!!'


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(consumo(num1, num2))


"""

# Exercicio 15:
"""

def consumo(valorA, valorB, valorC):
    if (valorA + valorB) > valorC and (valorC + valorB) > valorA:
        print('Triangulo valido!')
    if valorA == valorB == valorC:
        return 'Equilatero!'
    elif valorA == valorB or valorA == valorC or valorB == valorC:
        return 'Isósceles!'
    return 'Seu triangulo é escaleno'


num1 = int(input('Digite o lado A: '))
num2 = int(input('Digite o lado B: '))
num3 = int(input('Digite o lado C: '))
if num1 <= 0 or 0 >= num2 or num3 <= 0:
    print('Numero menor que zero!')
else:
    print(consumo(num1, num2, num3))

"""

# Exercicio 16:
"""

def desenha_linha(num):
    # :param num: Tamanho da linha
    # :return: O simbulo vezes a quantia de tamanho, ou seja, o tamanho que a linha terá
    return print('=' * num)


tamanho = int(input('Digite o tamanho da linha: '))
desenha_linha(tamanho)

"""

# Exercicio 17:
"""

def soma_2(num1, num2):
    soma = 0
    for i in range(num1, num2 + 1):
        soma += i
    return soma


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(soma_2(num1, num2))

"""

# Exercicio 18:
"""

def funcao(a, b=2):
    return a ** b


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(funcao(num1, num2))

"""

# Exercicio 19:

"""



"""

# Exercicio 20:
"""

def funcao(num):
    fatorial = 1
    for i in range(num, 0, -1):
        fatorial *= i
    return fatorial


num1 = int(input('Digite um número: '))
print(funcao(num1))


"""

# Exercicio 21:

"""

def funcao(num):
    primos = []
    for x in range(2, num):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primos.append(x)
    return primos


num1 = int(input('Digite um número: '))
print(funcao(num1))

"""

# Exercicio 22:

"""

def triangulo(num):
    for i in range(0, num + 1):
        print('!' * i)
    return


num = int(input('Digite um número: '))
triangulo(num)


"""

# Exercicio 23:

"""

def triangulo(num):
    for i in range(num + 1):
        print('*' * i)
    for i in range(num - 1, 0, -1):
        print('*' * i)

triangulo(4)

"""

# Exercicio 24:

"""

def triangulo(num):
    for i in range(num):
        for j in range(i, num):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        for j in range(i + 1):
            print('*', end='')
        print()
    return


num = int(input('Digite um número: '))
triangulo(num)

"""

# Exercicio 25:

"""

def funcao(num):
    soma = 0
    for i in range(num):
        soma += (i ** 2) + 1 / num + 3
    return soma


print(funcao(10))

"""

# Exercicio 26:

"""

def funcao(num):
    soma = 0
    for i in range(num + 1):
        soma += i
    return soma


print(funcao(5))

"""

# Exercicio 27:

"""



"""

# Exercicio 28:

"""



"""

# Exercicio 29:

"""



"""

# Exercicio 30:

"""



"""

# Exercicio 31:

"""



"""

# Exercicio 32:

"""

def mdc(a, b):
    while b != 0:
        if b > a:
            a, b = b, a
        a, b = b, a - b
    return a


num1 = int(input('Digite o nominador: '))
num2 = int(input('Digite o denominador: '))
mdc = mdc(num1, num2)
print(f'A fração simplificada é: {int(num1 / mdc)}/{int(num2 / mdc)}')


"""

# Exercicio 33:

"""

def soma(a):
    n1 = a
    for i in range(1, a):
        n1 *= i
    n2 = 0
    for i in str(n1):
        n2 += int(i)
    return n2


num = int(input('Digite o número: '))
print(soma(num))

"""

# Exercicio 34:

"""

def fatorial_duplo(a):
    n1 = a
    for i in range(1, a):
        if i % 2 == 1:
            n1 *= i
    return n1


num = int(input('Digite o número impar: '))
if num % 2 == 1:
    print(fatorial_duplo(num))
else:
    print('Voce digitou um par!')

"""

# Exercicio 35:

"""

def fatorial_quadruplo(a):
    n1 = a
    n2 = a * 2
    for i in range(1, a):
        n1 *= i
    for i in range(1, n2):
        n2 *= i
    return n2 / n1


num = int(input('Digite o número: '))
print(f'{fatorial_quadruplo(num)}')

"""

# Exercicio 36:

"""

def super_fatorial(a):
    total = 1
    for x in range(1, a + 1):
        n1 = x
        for y in range(1, n1):
            n1 *= y
        total *= n1
    return total


num = int(input('Digite um numero: '))
print(super_fatorial(num))

"""

# Exercicio 37:

"""

def hiper_fatorial(a):
    n1 = 1
    for i in range(1, a + 1):
        b = i ** i
        n1 *= b
    return n1


num = int(input('Digite um numero: '))
print(hiper_fatorial(num))

"""

# exercicio 38:

"""

def fatorial_exponencial(a):
    n1 = a
    for i in range(1, a):
        n1 **= a - i
    return n1


print(fatorial_exponencial(4))

"""

# exercicio 39:

"""

def troque(a, b):
    a, b = b, a
    return print(a, b)


variavel_a = input('A) Digite uma variavel: ')
variavel_b = input('B) Digite uma variavel: ')

print(troque(variavel_a, variavel_b))


"""

# exercicio 40:

"""

def vetor(a):
    valor = 0
    for i in a:
        if i % 2 == 0:
            valor += 1
    return valor


print(vetor([1, 2, 4, 5, 6]))

"""

# exercicio 41:

"""

def vetor(a):
    return max(a)


print(vetor([1, 2, 4, 5, 6]))

or

def vetor(a):
    maior = 0
    for i in a:
        if i > maior:
            maior = i
    return maior


print(vetor([1, 2, 4, 5, 6]))


"""

# exercicio 42:

"""

def media(a):
    soma = 0
    for i in a:
        soma += i
    return soma / len(a)


print(media([1, 2, 4, 5, 6]))


"""

# exercicio 43:

"""

import random


def aleatorios(a):
    true = True
    while len(a) != 10:
        n = random.randint(1, 11)
        if n in a:
            continue
        else:
            a.append(n)
    return a


print(aleatorios([]))

"""

# exercicio 44:

"""

vetor = []


while len(vetor) != 30:
    n = int(input('Digite um número: '))
    vetor.append(n)


def par_impar(a):
    vetor_x = []
    vetor_y = []
    for i in vetor:
        if i % 2 != 0:
            vetor_x.append(i)
        else:
            vetor_y.append(i)
    return vetor_x, vetor_y


print(par_impar(vetor))


"""

# exercicio 45:

"""

def desvio_padrão(a):
    media = 0
    for i in a:
        media += i
    media = media / len(a)
    variancia = 0
    for i in a:
        if i > media:
            variancia += (i - media) ** 2
        else:
            variancia += (media - i) ** 2
    variancia = variancia / media
    return variancia ** 0.5


print(f'{desvio_padrão([3, 7, 6, 5, 4]):.2f}')


"""

# exercicio 46:

"""

def impressao(a):
    return print(a)


def inversa(a):
    for i in range((len(a) - 1), -1, -1):
        print(a[i], end=' ')


def media(a):
    media = 0
    for i in a:
        media += i
    return media / len(a)

"""

# exercicio 47:

"""

import random

matriz1 = []
length = 4

for lista in range(0, length):
    matriz1.append([])
    for indice in range(0, length):
        matriz1[lista].append(random.randint(1, 30))


def matriz(a):
    contagem = 0
    for lista in a:
        for item in lista:
            if item > 10:
                contagem += 1
    return contagem

print(matriz(matriz1))

"""

# exercicio 48:

"""

import random

matriz = []
tamanho = 3
frufru = 9

for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 20))


def soma_diagonal(a):
    i = -1
    soma = 0
    for lista in matriz:
        i += 1
        for item in range(len(lista)):
            if item > i:
                soma += lista[item]
    return soma

print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print(soma_diagonal(matriz))


"""

# exercicio 49:

"""
import random

matriz = []
tamanho = 3
frufru = 9
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def soma_diagonal_abaixo(a):
    soma = 0
    for indice_matriz in range(len(matriz)):
        for indice_lista in range(len(matriz[indice_matriz])):
            if indice_matriz > indice_lista:
                soma += matriz[indice_matriz][indice_lista]
                print(matriz[indice_matriz][indice_lista])
    return soma


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Soma', soma_diagonal_abaixo(matriz))


"""

# exercicio 50:

"""

import random

matriz = []
tamanho = 3
frufru = 9
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def soma_diagonal(a):
    soma = 0
    for indice_matriz in range(len(matriz)):
        for indice_lista in range(len(matriz[indice_matriz])):
            if indice_matriz == indice_lista:
                soma += matriz[indice_matriz][indice_lista]
                print(matriz[indice_matriz][indice_lista])
    return soma

print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Soma', soma_diagonal(matriz))

"""

# exercicio 51:

"""

import random

matriz = []
tamanho = 3
frufru = 9
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def soma_diagonal2(a):
    soma = 0
    i = -1
    for indice in range(len(a) - 1, -1, -1):
        i += 1
        print(matriz[i][indice])
        soma += matriz[i][indice]
    return soma


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Soma', soma_diagonal2(matriz))


"""

# exercicio 52:

"""

import random

matriz = []
transposta = []
tamanho = 3
frufru = 9
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def transposta(a):
    transposta = []
    listas = len(a)
    indices = len(a[0])
    for ilistas in range(len(a)):
        transposta.append([])
        for i in a[ilistas]:
            transposta[ilistas].append(0)
    for x in range(listas):
        for y in range(indices):
            transposta[y][x] = a[x][y]
    return transposta


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

transposta = transposta(matriz)

print('Matriz Transposta: ')
print('=*=' * frufru)
for lista in transposta:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# exercicio 53:

"""

import random

matriz = []
transposta = []
tamanho = 3
frufru = 9
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


#def matriz_exata(a):
#    for indice_matriz in range(len(a)):
#        for indice_lista in range(len(a[indice_matriz])):
#            if indice_matriz == indice_lista:
#                a[indice_matriz][indice_lista] = tamanho
#    return a


def leitor_m_identidade(a):
    conta = 0
    for indice_matriz in range(len(a)):
        for indice_lista in range(len(a[indice_matriz])):
            if indice_matriz == indice_lista:
                if a[indice_matriz][indice_lista] == len(a):
                    conta += 1
    if conta == len(a):
        return print('Matriz é uma matriz de indentidade')
    return print('Matriz não é uma matriz de indentidade')


print('Matriz: ')
print('=*=' * frufru)
# matriz = matriz_exata(matriz)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

leitor_m_identidade(matriz)

"""

# exercicio 54:

"""


matriz = []
transposta = []
tamanho = 4
frufru = 12
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def soma_m(a):
    if len(a) == 4 and len(a[0]) == 4:
        soma = 0
        for lista in a:
            for item in lista:
                soma += item
        return soma


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print(soma_m(matriz))

"""

# exercicio 55:

"""

import random
matriz = []
transposta = []
tamanho = 4
frufru = tamanho * 3
for lista in range(tamanho):
    matriz.append([])
    for indice in range(tamanho):
        matriz[lista].append(random.randint(1, 21))


def soma_diagonal(a):
    if len(a) == 4 and len(a[0]) == 4:
        soma1 = 0
        soma2 = 0
        for indice in range(len(a)):
            soma1 += matriz[indice][indice]
        i = -1
        for indice in range(len(a) - 1, -1, -1):
            i += 1
            soma2 += matriz[i][indice]
        return soma1, soma2


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print(soma_diagonal(matriz))

"""

# exercicio 56:

"""

import random

matriz = []
transposta = []
listas = 7
itens = 6
frufru = itens * 3
for lista in range(listas):
    matriz.append([])
    for indice in range(itens):
        matriz[lista].append(random.randint(1, 21))


def soma_diagonal(matriz, num):
    soma = 0
    if len(matriz) == 7 and len(matriz[0]) == 6:
        for indice, lista in enumerate(matriz):
            if indice == num - 1:
                soma += sum(lista)
                print(lista)
    return soma


print('Matriz: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

num = int(input('Digite a linha que voce quer somar: '))
print(soma_diagonal(matriz, num))


"""

# exercicio 57:

"""

import random
i = 0

def montar_matriz():
    listas = int(input('Digite a quantia de listas: '))
    itens = int(input('Digite a quantia de itens: '))
    matriz = [[random.randint(1, 21) for x in range(itens)] for y in range(listas)]
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


def soma_coluna(matriz, num):
    soma = []
    if len(matriz) == 7 and len(matriz[0]) == 6:
        for lista in matriz:
            if num - 1 < len(lista):
                soma.append(lista[num - 1])
    print(soma)
    return sum(soma)


matriz = montar_matriz()
print_matriz(matriz)

num = int(input('Digite a coluna que voce quer somar: '))
print(soma_coluna(matriz, num))


"""

# exercicio 58:

"""

import random

i = 0


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


def montar_matriz():
    listas = int(input('Digite a quantia de listas: '))
    itens = int(input('Digite a quantia de itens: '))
    matriz = [[random.randint(1, 21) for itens in range(itens)] for listas in range(listas)]
    return matriz


matriz1 = montar_matriz()
matriz2 = montar_matriz()


def multiplica_m(matriz1, matriz2):
    matriz3 = [[0 for linha in range(len(matriz1))] for coluna in range(len(matriz2[0]))]
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            matriz3[i][j] = soma
    return matriz3


print_matriz(matriz1)
print_matriz(matriz2)
print_matriz(multiplica_m(matriz1, matriz2))

"""

# exercicio 59:

"""

import random

vetor1 = []
vetor2 = []
for i in range(10):
    vetor1.append(random.randint(1, 5))
    vetor2.append(random.randint(1, 5))


def uniao(vetor1, vetor2):
    vetor3 = []
    soma = 0
    if len(vetor1) != len(vetor2):
        return 'Paia'
    for i in range(len(vetor1)):
        soma += vetor1[i] + vetor2[i]
    vetor3 = soma
    return vetor3


print(uniao(vetor1, vetor2))

"""

# exercicio 60:

"""

def sub_string(a, b):
    a = a.split()
    for string in a:
        if string == b:
            return string
    return -1


print(sub_string('Paçoca quente amanha', 'Paçoca'))
print(sub_string('Paçoca quente amanha', 'ontem'))

"""

# exercicio 61:

"""

def anagrama(a, b):
    i = 0
    if a != str(a) or b != str(b):
        return 'Insira uma string!'
    a = a.lower()
    b = b.lower()
    for letra in a:
        if letra in b:
                i += 1
    if i == len(b):
        return 'é um anagrama'
    return 'Não é um anagrama'

"""

# exercicio 62:

"""

def count_str(a):
    return print(len(a))


count_str('Geek University?')


"""

# exercicio 63:

"""

def strings(a, b):
    if a in b:
        return 'Iguais'
    return 'Diferentes'


print(strings('Geek', 'Geek'))
print(strings('Geeky', 'Geek'))

"""

# exercicio 64:

"""

def strings(a, b):
    if a == str(a) and b == str(b):
        return a + b

    return 'Ambas devem ser strings'


print(strings('Gosto de ', 'dinheiro'))


"""

# exercicio 65:

"""

def strings(a, b, n):
    if a == str(a) and b == str(b):
        return a[:n + 1] + b[:n + 1]

    return 'Ambas devem ser strings'


print(strings('Gosto', ' de dinheiro', 4))


"""

# exercicio 66:

"""

def strings(a, b):
    if b not in a:
        return 'Digite outro caractere'
    i = a.find(b)
    a = a[:i] + b.upper()
    return a

print(strings('Arroz', 'z'))

"""

# exercicio 67:

"""

def getchar():
    caractere = input('Informe um caractere: ')
    return caractere


def rotina(tamanho):
    vetor = []
    for x in range(tamanho):
        valor = getchar()
        if valor != '':
            vetor.append(valor)
        else:
            break
    return vetor


tamanho = int(input('Insira o tamanho: '))
print(rotina(tamanho))

"""

# exercicio 68:

"""

def intercalada(a, b):
    if b > a:
        a, b = b, a
    c = ''
    for i in range(len(a)):
        c += a[i]
        if len(b) > i:
            c += b[i]
    return c


print(intercalada('Geek', 'University'))

"""

# exercicio 69:

"""

def simplificaf(a, b):
    num1 = a
    num2 = b
    # mdc
    while b != 0:
        if b > a:
            a, b = b, a
        a, b = b, a - b
    return f'{num1 // a} / {num2 // a}'


def somaf(numerador1, denominador1, numerador2, denominador2):
    numerador = numerador1 * denominador2 + numerador2 * denominador1
    denominador = denominador1 * denominador2
    return simplificaf(numerador, denominador)


def subtraif(numerador1, denominador1, numerador2, denominador2):
    numerador = numerador1 * denominador2 - numerador2 * denominador1
    denominador = denominador1 * denominador2
    return simplificaf(numerador, denominador)


def dividef(numerador1, denominador1, numerador2, denominador2):
    numerador = numerador1 * denominador2
    denominador = denominador1 * numerador2
    return simplificaf(numerador, denominador)


def multiplicaf(numerador1, denominador1, numerador2, denominador2):
    numerador = numerador1 * numerador2
    denominador = denominador1 * denominador2
    return simplificaf(numerador, denominador)


def quociente(numerador, denominador):
    if denominador == 0:
        return 'tentando dividir por zero?'
    return numerador / denominador

"""

# exercicio 70:

"""

def simplificaf(a, b):
    num1 = a
    num2 = b
    # mdc
    while b != 0:
        if b > a:
            a, b = b, a
        a, b = b, a - b
    return f'{num1 // a} / {num2 // a}'


def neg(a, b):
    a *= -1
    b *= -1
    return a, b


def soma(a, b):
    a += b
    return a


def mult(x, y):
     x *= y
     return x


def div(x, y):
    x /= y
    return x

"""

# exercicio 71:

"""



"""

# exercicio 72:

"""



"""

# exercicio 73:

"""



"""

