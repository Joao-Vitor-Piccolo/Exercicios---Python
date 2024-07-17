# Exercicio 1:

"""

a = [1, 0, 5, -2, -5, 7]
variavel = int(input('Variavel: '))
a.insert(0, variavel)
a.insert(1, variavel)
a.insert(5, variavel)
print('Soma', sum(a))
a.insert(4, 100)
for v in a:
    print(v)


"""

# Exercicio 2:

"""

c = 1
b = []

while c != 7:
    a = int(input(f'{c}) Valor: '))
    b.append(a)
    c += 1
print('Valores lidos:', b)

"""

# Exercicio 3:

"""

l1 = []
l2 = []
for i in range(10):
    l1.append(float(input("Digite um número decimal: ")))
    l2.append(l1[i] ** 2)

print(l1)
print(l2)

"""

# Exercicio 4:

"""

vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(input('Valor 1: '))
y = int(input('Valor 2: '))

x = vetor[x - 1]
y = vetor[y - 1]

print(f'Letra: {x} ')
print(f'Letra: {y} ')


"""

# Exercicio 5:

"""

vetor = []

for i in range(1, 11):
    if i % 2 == 0:
        vetor.append(i)
print(vetor)


"""

# Exercicio 6:

"""

vetor = []

for i in range(1, 11):
    vetor.append(i)

print(max(vetor))
print(min(vetor))

"""

# Exercicio 7:

"""

vetor = []

for i in range(1, 11):
    vetor.append(i)

print(f'Maior Número: {max(vetor)}, Seu indice: {vetor.index(max(vetor))}')


"""

# Exercicio 8:

"""

vetor = []

for i in range(1, 11):
    vetor.append(i)

print(f'Ordem inversa: {vetor[::-1]}')


"""

# Exercicio 9:

"""

vetor = []

for i in range(1, 7):
    if i % 2 == 0:
        vetor.append(i)

print(f'Ordem inversa: {vetor[::-1]}')

"""

# Exercicio 10:

"""

vetor = []
s = 0
for i in range(1, 16):
    n = int(input('Digite o numero: '))
    vetor.append(n)
    s += n

print(f'Media: {s / len(vetor)}')


"""

# Exercicio 11:

"""

vetor1 = []
vetor2 = []

for i in range(1, 11):
    n = int(input('Digite o numero: '))
    if n >= 1:
        vetor1.append(n)
    else:
        vetor2.append(n)

print(f'Numeros negativos: {vetor2}, Numeros positivos: {vetor1}')


"""

# Exercicio 12:

"""

vetor = []
s = 0

for i in range(1, 6):
    n = int(input('Insira o valor: '))
    vetor.append(n)
    s += n

print(f'Media: {s / len(vetor)}, Maior: {max(vetor)}, Menor: {min(vetor)}')


"""

# Exercicio 13:

"""

vetor = []

for i in range(1, 11):
    valor = int(input(f'{i}) Digite o valor: '))
    vetor.append(valor)
print('Valores:', vetor)
print('Maximo:', max(vetor))
print('Minimo:', min(vetor))
print('Media:', sum(vetor) / len(vetor))

"""

# Exercicio 14:

"""

vetor = []
iguais = 0
valores = []

for i in range(1, 11):
    valor = int(input(f'{i}) Digite o valor: '))
    vetor.append(valor)

for valor in vetor:
    if vetor.count(valor) > 1:
        iguais += 1
        valores.append(valor)
print('Valores:', valores)
print('Iguais:', iguais)

"""

# Exercicio 15:

"""

vetor = [1, 2, 3, 4, 4, 5, 5]
iguais = 0


for i in range(1, 21):
    valor = int(input(f'{i}) Digite o valor: '))
    vetor.append(valor)
    
for valor in vetor:
    if vetor.count(valor) > 1:
        iguais += 1
        vetor.pop(valor)
        
print('Valores:', vetor)
print('Iguais:', iguais)

"""

# Exercicio 16:

"""



"""

# Exercicio 17:

"""

vetor = [-1, 2, -3, 4, -4, 5, 5, -8, 9]
for valor in vetor:
    if valor < 0:
        vetor.insert(valor, 0)

print(vetor)

"""

# Exercicio 18:

"""

m = 0
vetor = []
for i in range(1, 11):
    vetor.append(i)

print(vetor)
n = int(input('Digite um numero do vetor: '))
list = []

for i in range(1, 11):
    m = n * i
    list.append(m)

print(list)

"""

# Exercicio 19:

"""

vetor = []
for i in range(1, 51):
    vetor.append((i + 5 * i) % (i + 1))
print(vetor)


"""

# Exercicio 20:

"""

vetor1 = []
vetor2 = []
for i in range(1, 5):
    n = int(input(f'{i}/50) Digite um numero: '))
    if n % 2 == 1:
        vetor2.append(n)
    vetor1.append(n)

for i in range(0, len(vetor1), 2):
    print(f'Vetor 1: {vetor1[i]}, {vetor1[i + 1]}')

for i in range(0, len(vetor2), 2):
    print(f'Vetor 2: {vetor2[i]}, {vetor2[i + 1]}')


"""

# Exercicio 21:

"""

vetora = [1, 4, 6, 8, 3, 4, 5, 6, 7, 5]
vetorb = [4, 1, 3, 7, 23, 32, 7, 9, 3, 2]
vetorc = []

for i in range(0, 10):
    s = vetora[i] - vetorb[i]
    vetorc.append(s)

print(vetorc)


"""

# Exercicio 22:

"""

vetora = [1, 4, 6, 8, 3, 4, 5, 6, 7, 5]
vetorb = [4, 1, 3, 7, 23, 32, 7, 9, 3, 2]

print(vetora)
print(vetorb)

for i in range(0, 10):
    if i % 2 == 0:
        vetorb.insert(i, vetora[i])
    else:
        vetora.insert(i, vetorb[i])
print(vetora)
print(vetorb)


"""

# Exercicio 23:

"""

vetor = []
e = 0
c = 1
for i in range(1, 6):
    x = int(input(f'{c}) Digite um valor x: '))
    c += 1
    y = int(input(f'{c}) Digite o valor y: '))
    c += 1
    e += (x * y)
    vetor.append(e)
print(vetor)

"""

# Exercicio 24:

"""

vetor1 = []
vetor2 = []
vetor3 = {}

altm = 0
altmenor = float('inf')

for i in range(1, 6):
    num = int(input('Digite o numero do aluno: '))
    vetor1.append(num)
    alt = int(input('Digite sua altura: '))
    vetor2.append(alt)

for i, n in enumerate(vetor1):
    vetor3[n] = vetor2[i]

for aluno, altura in vetor3.items():
    if altura > altm:
        altm = altura
    if altura < altmenor:
        altmenor = altura
        
print(altm, altmenor)

"""

# Exercicio 25:

"""

vetor = []
c = 0

while len(vetor) != 100:
    c += 1
    if c % 7 == 0 or '7' in str(c):
        vetor.append(c)

print(vetor)

"""

# Exercicio 26:

"""

n = [3, 7, 6, 5, 4 ]

m = sum(n) / (len(n))
d = []
v = 0
c = 0
for i in n:
    if i > 5:
        d.append(i - m)
    else:
        d.append(m - i)
    v += d[c] ** 2
    c += 1

print(f'O Desvio Padrão é a raiz: {v / len(n)}')
print(f'Raiz de {v / len(n)}: {v / len(n) ** 0.5:.3f}')


"""

# Exercicio 27:

"""

vetor = []

for i in range(1, 11):
    primo = True
    n = int(input(f'{i}) Digite um numero: '))
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            primo = False
            break
    if primo:
        vetor.append(n)
vetor.sort()

for i, valor in enumerate(vetor):
    print(f'Indice E Valor: {i}, {valor}')

"""

# Exercicio 28:

"""

vetor = []

for i in range(1, 11):
    vetor.append(i)

v1 = []
v2 = []

for i in vetor:
    if i % 2 == 0:
        v1.append(i)
    else:
        v2.append(i)
print(v1, v2)


"""

# Exercicio 29:

"""

vetor1 = []
vetor2 = []
c = 0
for i in range(1, 7):
    if i % 2 == 0:
        vetor1.append(i)
    else:
        c += 1
        vetor2.append(i)
print(vetor1)
print(sum(vetor1))
print(vetor2)
print(c)


"""

# Exercicio 30:

"""

vetor1 = [1, 1, 2, 3, 4, 5, 7, 7, 8]
vetor2 = [32, 9, 51, 1, 1, 2, 5, 7, 81]
vetor3 = set({})

for n1 in vetor1:
    for n2 in vetor2:
        if n1 == n2:
            vetor3.add(n2)

print(vetor3)


"""

# Exercicio 31:

"""

vetor1 = [1, 1, 2, 3, 4, 5, 7, 7, 8]
vetor2 = [32, 9, 51, 1, 1, 2, 5, 7, 81]
vetor3 = set({})

for n in vetor1:
    vetor3.add(n)
for n in vetor2:
    vetor3.add(n)

print(vetor3)


"""

# Exercicio 32:

"""

vetor1 = []
vetor2 = []
vetor3 = vetor1.copy()
s = 0

for i in range(1, 6):
    num1 = int(input(f'{i}) P/1 Digite um numero: '))
    vetor1.append(num1)
for i in range(6, 11):
    num2 = int(input(f'{i}) P/2 Digite um numero: '))
    vetor2.append(num2)

vetor3 = set(vetor1.copy())

for i in range(len(vetor1)):
    print(f'Soma: {vetor1[i] + vetor2[i]}')

for i in range(len(vetor1)):
    print(f'Multiplicação: {vetor1[i] * vetor2[i]}')

for n1 in vetor1:
    for n2 in vetor2:
        if n1 == n2:
            vetor3.discard(n1)

print('Diferença:', vetor3)

vetor3 = vetor1.copy()

for n1 in vetor1:
    for n2 in vetor2:
        if n1 == n2:
            vetor3.append(n1)
print('Interseção:', vetor3)

vetor3 = set(vetor2.copy())

for n1 in vetor2:
    for n2 in vetor1:
        if n1 == n2:
            vetor3.add(n1)
print('União:', vetor3)


"""

# Exercicio 33:

"""

from collections import deque

vetor1 = [1, 3, 0, 3, 4, 5, 0, 7, 8]
vetor2 = deque([])

for i in vetor1:
    if i <= 0:
        vetor2.appendleft(i)
    else:
        vetor2.append(i)
print(vetor2)

"""

# Exercicio 34:

"""
print('Digite um número maior que zero sem repetições.')
vetor = []
for i in range(1, 11):
    num = int(input(f'{i}/10) Digite um número: '))
    if num > 0:
        if num in vetor:
            print('Número repetido!')
            break
        else:
            print('Número aceito!')
            vetor.append(num)
    else:
        print('Número menor ou igual a 0.')
        break

print(vetor)


"""

# Exercicio 35:

"""

from collections import deque

print('Digite dois números menores que 10.000')
a = str(input('Digite um número: '))
b = str(input('Digite outro número: '))

vetor_a = deque([])
vetor_b = deque([])
vetor_s = deque([])

if 0 < int(a) < 10_000 and 0 < int(b) < 10_000:
    for i in a:
        vetor_a.append((int(i)))

    for i in b:
        vetor_b.append((int(i)))


max_len = max(len(vetor_a), len(vetor_b))
vetor_a.extendleft([0] * (max_len - len(vetor_a)))
vetor_b.extendleft([0] * (max_len - len(vetor_b)))

carry = 0
for i in range(max_len - 1, -1, -1):
    soma = vetor_a[i] + vetor_b[i] + carry
    if soma >= 10:
        carry = 1
        soma -= 10
    else:
        carry = 0
    vetor_s.appendleft(soma)

if carry == 1:
    vetor_s.appendleft(1)

print("Resultado:", vetor_s)


"""

# Exercicio 36:

"""

vetor = []

for i in range(1, 11):
    num = int(input(f'{i}) Digite um numero: '))
    vetor.append(num)
vetor.sort()

print(vetor)

"""

# Exercicio 37:

"""

vetor1 = []
for i in range(1, 11):
    # num = int(input(f'{i}) Digite um numero: '))
    vetor1.append(i)

vetor1.sort()
vetor2 = vetor1[5:10]
vetor3 = vetor1[:5]

print(vetor3[::-1] + vetor2)


"""

# Exercicio 38:

"""

vetor = []

for i in range(1, 11):
    num = int(input(f'{i}/10) Digite um numero: '))
    vetor.sort()
    vetor.append(i)


print(vetor)

"""

# Exercicio 39:

"""



"""


# Exercicios Seção 7 P/2
#
#
# Geek University:

# Exercicio 1:

"""

matriz = [[], [], [], []]
vetor = []

lengh = len(matriz)

for x in range(0, lengh):
    for y in range(0, lengh):
        n = int(input(f'Lista: {x + 1}, Indice: {y}) Digite seu numero: '))
        matriz[x].append(n)
        if n >= 10:
            vetor.append(n)
    if len(matriz[x]) == lengh:
        print('Lista completa!')
for x in range(0, lengh):
    for y in range(0, lengh):
        print(f'[{matriz[x][y]:^5}]', end='-')
    print()
print(vetor)


"""

# Exercicio 2:

"""

matriz = [[], [], [], [], []]
length = len(matriz)
i = 0

for lista in range(0, length):
    for indice in range(0, length):
        matriz[lista].append(0)

for i in range(length):
    matriz[i][i] = 1

for lista in range(0, length):
    for indice in range(0, length):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()


"""

# Exercicio 3:

"""

matriz = [[], [], [], []]
vetor = []
i = 0
n = 0
lengh = len(matriz)

for x in range(0, lengh):
    for y in range(0, lengh):
        n += 1
        matriz[x].append(n)
        if n >= 10:
            vetor.append(n)
    if len(matriz[x]) == lengh:
        print('Lista completa!')

for lista in range(0, lengh):
    for indice in range(0, lengh):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()

print(matriz)

"""

# Exercicio 4:

"""

import random

matriz = [[], [], [], []]
i = 0
mv = 0
mv_c = 0
mv_l = 0
for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[lista].append(n)
        if n > mv:
            mv = n
            mv_l = lista

    if len(matriz[lista]) == len(matriz):
        print('Lista completa!')

print('=*=' * 30)

for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()

print('=*=' * 20)

print(f'O maior valor, ({mv}) está na coluna: {matriz[mv_l].index(mv) + 1}'
      f'\nNa posição: {mv_l + 1}')

"""

# Exercicio 5:

"""

import random

matriz = [[], [], [], []]

for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[lista].append(n)
    if len(matriz[lista]) == len(matriz):
        print('Lista completa!')

print('=*=' * 15)

for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()

print('=*=' * 15)

n = int(input('Digite o valor procurado: '))

for i, lista in enumerate(matriz):
    if n in lista:
        print('Valor encontrado!')
        print(f'está na coluna: {lista.index(n) + 1}'
              f'\nNa posição: {i + 1}')
        break
else:
    print('Valor não encontrado...')

"""

# Exercicio 6:

"""

import random

matriz = [[], [], [], []]
maior = 0
vetor = []

for i, lista in enumerate(matriz):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[i].append(n)
    vetor.append(max(matriz[i]))

print('=*=' * 15)

for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()

print('=*=' * 15)
print(f'Os maiores valores de cada fileira: {vetor}')


"""

# Exercicio 7:

"""

import random

matriz = [[], [], [], [], [], [], [], [], [], []]
maior = 0
vetor = []

for i, lista in enumerate(matriz):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        if i < n:
            matriz[i].append(i + n - 2)
        elif i == n:
            matriz[i].append((i ** 2) - 1)
        elif i > n:
            matriz[i].append((i ** 3) - (5 ** 2) + 1)

print('=*=' * 30)
for lista in range(len(matriz)):
    for indice in range(len(matriz)):
        print(f'=[{matriz[lista][indice]:^5}]', end='=')
    print()
print('=*=' * 30)


"""

# Exercicio 8:

"""

import random

matriz = [[], [], []]
soma = 0

for i, lista in enumerate(matriz):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[i].append(n)
        if indice < i:
            soma += n

print('=*=' * 15)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * 15)

print("Soma dos elementos abaixo da diagonal principal:", soma)
"""

# Exercicio 9:

"""

import random

matriz = [[], [], []]
soma = 0

for i, lista in enumerate(matriz):
    for indice in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[i].append(n)
        if indice > i:
            soma += n

print('=*=' * 15)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * 15)

print("Soma dos elementos acima da diagonal principal:", soma)

"""

# Exercicio 10:

"""

import random

matriz = [[], [], []]
soma = 0

for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[indice].append(n)
        if num == indice:
            soma += n

print('=*=' * 15)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * 15)

print("Soma dos elementos da diagonal principal:", soma)

"""

# Exercicio 11:

"""

import random

matriz = [[], [], []]
soma = 0

for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[indice].append(n)

for indice in range((len(matriz) - 1), -1, -1):
    for num in range((len(matriz) - 1), -1, -1):
        if num == indice:
            print(matriz[indice][num])
            soma += matriz[indice][num]


print('=*=' * 15)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * 15)

print("Soma dos elementos da diagonal principal invertida :", soma)


"""

# Exercicio 12:

"""

import random

matriz = [[], [], []]
transposta = [[], [], []]
soma = 0
frufru = 9

for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[indice].append(n)
        transposta[indice].append(0)
    # linha
for indice in range(len(matriz)):
    for lista in range(len(matriz[0])): # Colunas
        transposta[lista][indice] = matriz[indice][lista]

print('Matriz')
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print()
print('Matriz Transposta')
for lista in transposta:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# Exercicio 13:

"""

import random

matriz = [[], [], [], []]
soma = 0
frufru = 12

for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 21)
        if num > indice:
            matriz[indice].append(0)
        else:
            matriz[indice].append(n)

print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)


"""

# Exercicio 14:

"""

import random

matriz = [[], [], [], []]
soma = 0
frufru = 12

for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[indice].append(n)

for indice1, lista1 in enumerate(matriz):
    for num1 in range(len(matriz)):
        for indice2, lista2, in enumerate(matriz):
            for num2 in range(0, len(matriz)):
                if num2 > 0:
                    if lista1[num1] == lista2[num2]:
                        print(lista1[num1])
                        n = random.randint(1, 100)
                        while n in [item for lista in matriz for item in lista]:
                            n = random.randint(1, 100)

print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# Exercicio 15:

"""

gabarito = []
acertos = []
erros = []
frufru = 30
questoes = int(input('Digite a quantia de questoes: '))
alunos = int(input('Digite a quantia de alunos: '))

for i in range(1, questoes + 1):
    n = str(input(f'Digite o gabarito da questão {i}: '))
    gabarito.append(n)
    if n != 'a' and n != 'b' and n != 'c' and n != 'd':
        print('Digite uma letra correta:', n)
        break
for aluno in range(0, alunos):
    acertos.append([])
    erros.append([])
    for x, y in enumerate(gabarito):
        n = str(input(f'Aluno {aluno + 1}) Digite a resposta da questão {x + 1}: '))
        if n == y:
            acertos[aluno].append(n)
        elif n != y:
            erros[aluno].append(n)
            if n != 'a' and n != 'b' and n != 'c' and n != 'd':
                print('Digite uma letra correta:', n)
                break


print()
print('GABARITO')
for lista in gabarito:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()

print('=*=' * frufru)

print('Respostas Corretas')
for x, lista in enumerate(acertos):
    print(f'Aluno: {x + 1}')
    for y, resposta in enumerate(lista):
        print(f'Resposta {y + 1}: [{resposta:^5}]', end=' ')
        print()

print('=*=' * frufru)

print('Respostas Incorretas')
for x, lista in enumerate(erros):
    print(f'Aluno: {x + 1}')
    for y, resposta in enumerate(lista):
        print(f'Resposta {y + 1}: [{resposta:^5}]', end=' ')
        print()


"""

# Exercicio 16:

"""

gabarito = []
acertos = []
erros = []

frufru = 30
questoes = 10
alunos = 3

for i in range(1, questoes + 1):
    n = str(input(f'Digite o gabarito da questão {i}: '))
    gabarito.append(n)
    if n != 'a' and n != 'b' and n != 'c' and n != 'd' and n != 'e':
        print('Digite uma letra correta:', n)
        break
for aluno in range(0, alunos):
    acertos.append([])
    erros.append([])
    for x, y in enumerate(gabarito):
        n = str(input(f'Aluno {aluno + 1}) Digite a resposta da questão {x + 1}: '))
        if n == y:
            acertos[aluno].append(n)
        elif n != y:
            erros[aluno].append(n)
            if n != 'a' and n != 'b' and n != 'c' and n != 'd' and n != 'e':
                print('Digite uma letra correta:', n)
                break


print()
print('GABARITO')
for lista in gabarito:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()

print('=*=' * frufru)

print('Respostas Corretas')
for x, lista in enumerate(acertos):
    print(f'Aluno: {x + 1}')
    m = 0
    for y, resposta in enumerate(lista):
        print(f'Resposta {y + 1}: [{resposta:^5}]', end=' ')
        m += 1
    print()
    print(f'Media do Aluno {x + 1}: {m}')

print('=*=' * frufru)

print('Respostas Incorretas')
for x, lista in enumerate(erros):
    print(f'Aluno: {x + 1}')
    for y, resposta in enumerate(lista):
        print(f'Resposta {y + 1}: [{resposta:^5}]', end=' ')
        print()


"""

# Exercicio 17:

"""

import random

matriz = []
vetor = []
soma = 0
n = 0
na = 0
frufru = 13


for x in range(10):
    matriz.append([])
    vetor.append([])
for indice, lista in enumerate(matriz):
    for num in range(0, 3):
        n = random.randint(1, 11)
        matriz[indice].append(n)
    vetor[indice].append(min(matriz[indice]))
print()
print(vetor)

print('=*=' * frufru)
for i, lista in enumerate(matriz):
    print(f'Pior nota: {vetor[i]}')
    print(f'Aluno {i + 1:^2}:', end='')

    for elemento in lista:
        print(f' [{elemento:^5}]', end='')

    print()
print('=*=' * frufru)



"""

# Exercicio 18:

"""

import random

tamanho = int(input('Digite o tamanho da matriz: '))
transposta = [[], [], []]
matriz = []
vetor = []
soma = 0
frufru = 9

for i in range(tamanho + 1):
    if i > 0:
        matriz.append([])
        vetor.append([])
for indice, lista in enumerate(matriz):
    for num in range(len(matriz)):
        n = random.randint(1, 100)
        matriz[indice].append(n)
        transposta[indice].append(0)
        vetor[indice].append(n)

    # linha
for indice in range(len(matriz)):
    for lista in range(len(matriz[0])): # Colunas
        transposta[lista][indice] = matriz[indice][lista]

print(vetor)

print('Matriz: ')
print('=*=' * frufru)
for i in range(len(vetor)):
    print(f'-[{sum(vetor[i]):^5}]', end='-')
print()
for i, lista in enumerate(transposta):
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)


"""

# Exercicio 19:

"""

matriz = []
frufru = 12

print(f'Digite as seguintes informações nesta ordem: '
      '\n1) Numero da matricula;'
      '\n2) Media das provas;'
      '\n3) Media dos trabalhos;')

#   coluna
for lista in range(0, 5):
    matriz.append([])
#       linha
    for indice in range(0, 4):
        if indice < 3:
            n = int(input(f'{indice + 1}/3) Digite o número: '))
            matriz[lista].append(n)
        if indice == 3:
            n = (matriz[lista][1] + matriz[lista][2]) / 2
            matriz[lista].append(n)
print(matriz)

print('Matriz')
print('=*=' * frufru)

print(f'[{"Numero":^3}] '
      f'[{"Media 1":^3}] '
      f'[{"Media 2":^3}] '
      f'[{"Media Total":^3}]')
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# Exercicio 20:

"""

import random

matriz = []
frufru = 18
soma1 = 0
soma2 = 0
media = 0

print(f'Digite as seguintes informações nesta ordem: '
      '\n1) Numero da matricula;'
      '\n2) Media das provas;'
      '\n3) Media dos trabalhos;')

for lista in range(0, 3):
    matriz.append([])
    for indice in range(0, 6):
        n = random.randint(1, 50)
        if indice == 0 or indice == 1:
            soma2 += n
        if indice % 2 == 1:
            soma1 += n
        if indice == 1 or indice == 3:
            media += n
        matriz[lista].append(n)
        if indice == 5:
            matriz[lista][indice] = soma2

print('Soma Das Colunas Impares:', soma1)
print(f'Media: {media / 6:.2f}')

print('Matriz Modificada: ')
print('=*=' * frufru)
for lista in matriz:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# Exercicio 21:

"""

import random

matriz1 = []
matriz2 = []
soma = 0

frufru = 6

print('a) Somar as duas matrizes'
      '\nb) Subtrair a primeira matriz da segunda'
      '\nc) Adicionar uma constante ás duas matrizes'
      '\nd) Imprimir as matrizes')
r = str(input('Digite uma letra para a opção: '))

if r == 'a' or r == 'b':
    somalist = []
for i in range(2):
    if r == 'a' or r == 'b':
        somalist.append([])
    matriz1.append([])
    matriz2.append([])
for indice, lista in enumerate(matriz1):
    for num in range(len(matriz1)):
        n1 = random.randint(1, 100)
        matriz1[indice].append(n1)
        n2 = random.randint(1, 100)
        matriz2[indice].append(n2)
        if r == 'c' and indice == 0:
            lista[indice] = 10
        if r == 'a':
            somalist[indice].append(n1 + n2)
        elif r == 'b':
            if n1 > n2:
                somalist[indice].append(n1 - n2)
            else:
                somalist[indice].append(n2 - n1)
if r == 'c':
    for i, lista in enumerate(matriz2):
        if i == 0:
            lista[i] = 10
print('Matriz 1')
print('=*=' * frufru)
for lista in matriz1:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Matriz 2')
print('=*=' * frufru)
for lista in matriz2:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)
if r == 'a' or r == 'b':
    print('Matriz 3')
    print('=*=' * frufru)
    for lista in somalist:
        for elemento in lista:
            print(f'=[{elemento:^5}]', end='=')
        print()
    print('=*=' * frufru)

"""

# Exercicio 22:

"""

import random

matriz1 = []
matriz2 = []
c = []
length = 3
frufru = 9
for i in range(length):
    matriz1.append([])
    matriz2.append([])
    c.append([])
for indice in range(length):
    for num in range(len(matriz1)):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        matriz1[indice].append(n1)
        matriz2[indice].append(n2)
        c[indice].append(n1 * n2)

print('Matriz 1')
print('=*=' * frufru)
for lista in matriz1:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Matriz 2')
print('=*=' * frufru)
for lista in matriz2:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('Calculo')
print('=*=' * frufru)
for lista in c:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

"""

# Exercicio 23:

"""

import random

matriz1 = []
b = []
length = 3
frufru = 9
for i in range(length):
    matriz1.append([])
    b.append([])
for indice in range(length):
    for num in range(len(matriz1)):
        n1 = random.randint(1, 100)
        matriz1[indice].append(n1)
        b[indice].append(n1 ** 2)

print('Matriz 1')
print('=*=' * frufru)
for lista in matriz1:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)

print('A ao quadrado ')
print('=*=' * frufru)
for lista in b:
    for elemento in lista:
        print(f'=[{elemento:^5}]', end='=')
    print()
print('=*=' * frufru)


"""

# Exercicio 24:

"""



"""

# Exercicio 25:

"""

import random
from collections import Counter

matriz = []
length = 3
frufru = 9
contador_1 = 0
contador_2 = 0
contador1_1 = 0
contador2_2 = 0
transposta = []
true = True

for i in range(length):
    matriz.append([])
    transposta.append([])
for indice in range(length):
    for num in range(len(matriz)):
        n1 = 0
        matriz[indice].append(n1)
        transposta[indice].append(n1)
while true:
    print('Jogo da velha')
    print('Você será o "1" e o inimigo o "2"')
    print('=*=' * frufru)
    for lista in matriz:
        for elemento in lista:
            print(f'=[{elemento:^5}]', end='=')
        print()
    print('=*=' * frufru)
    if contador1_1 == 3 or contador2_2 == 3:
        print('FIM')
        true = False
        break
    elif contador_1 == 3 or contador_2 == 3:
        print('FIM')
        true = False
        break
    for i in range(3):
        contagem = Counter(matriz[i])
        if contagem[1] == 3 or contagem[2] == 3:
            print('FIM')
            true = False
            break
    if true == False:
        break
    print('Baseado no jogo acima...')
    coluna = int(input('Digite a coluna: '))
    linha = int(input('Digite a linha: '))
    if matriz[linha - 1][coluna - 1] == 1 or matriz[linha - 1][coluna - 1] == 2:
        false = False
        while not false:
            print('Linha e/ou coluna ocupada...')
            coluna = int(input('Digite outra coluna: '))
            linha = int(input('Digite outra linha: '))
            if matriz[linha - 1][coluna - 1] == 0 and matriz[linha - 1][coluna - 1] == 0:
                matriz[linha - 1][coluna - 1] = 1
                false = True
    else:
        matriz[linha - 1][coluna - 1] = 1
    for indice in range(len(matriz)):
        for lista in range(len(matriz[0])):  # Colunas
            transposta[lista][indice] = matriz[indice][lista]
    for i in range(3):
        contagem = Counter(transposta[i])
        if contagem[1] == 3 or contagem[2] == 3:
            print('FIM')
            true = False
            break

    coluna = random.randint(0, 2)
    linha = random.randint(0, 2)
    if matriz[linha][coluna] == 1 or matriz[linha][coluna] == 2:
        false = False
        while not false:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if matriz[coluna][linha] == 0:
                matriz[coluna][linha] = 2
                false = True
    else:
        matriz[linha][coluna] = 2
    contador_1 = 0
    contador_2 = 0
    for i in range(0, 3):
        if matriz[i][i] == 1:
            contador_1 += 1
        if matriz[i][i] == 2:
            contador_2 += 1
    contador1_1 = 0
    contador2_2 = 0
    for i in range(3):
        if matriz[i][2 - i] == 1:
            contador1_1 += 1
        if matriz[i][2 - i] == 2:
            contador2_2 += 1

"""
