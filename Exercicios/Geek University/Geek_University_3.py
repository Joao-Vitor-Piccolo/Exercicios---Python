# Exercicios Seção 3:
"""
Seção 3 de exercicos da geek:
"""

# 1 Exercicio.

"""

n = 0

for r in range(1, 4):
    n = 3 * r
    print(n)


"""

# 2 Exercicio.

"""

1) for r in range(1, 101):
    print(r)
    
2) n = 0

while n != 100:
    n += 1
    print(n)    
    
    

"""

# 3 Exercicio.

"""

n = 11

while n != 0:
    n -= 1
    print(n)


"""

# 4 Exercicio.

"""

n = 0

while n != 10000:
    n += 1000
    print(n)

"""

# 5 Exercicio.

"""

s = 0
c = 0
while c != 10:
    c += 1
    n = int(input(f'{c}) Digite um numero: '))
    s = s + n
print('Sua soma:', s)


"""

# 6 Exercicio.

"""

s = 0
c = 0
while c != 10:
    c += 1
    n = float(input(f'{c}) Digite um numero: '))
    s = s + n
print('Sua média:', (s / 10))

"""

# 7 Exercicio.

"""

c = 1
s = 0
while c != 11:
    n = int(input(f'{c}) Digite um numero: '))
    if n > 0:
        c += 1
        s += n
        print(s)
print(s / 10)

"""

# 8 Exercicio.

"""

c = 1
s = 0
n2 = 0
n3 = 0
while c != 11:
    n1 = int(input(f'{c}) Digite um numero: '))
    c += 1
    if n1 > n2:
        n2 = n1
    if n1 < n3:
        n3 = n1
print(f'O maior numero: {n2}\n'
      f'O menor numero: {n3}')


"""

# 9 Exercicio.

"""

n = int(input('digite um numero: '))

for r in range(1, n+1):
    if (r % 2) == 1:
        print(r)


"""

# 10 Exercicio.

"""

for r in range(1, 51):
    if (r % 2) == 0:
        print(r)

"""

# 11 Exercicio.

"""

n = int(input('digite um numero: '))

for r in range(0, n+1):
    print(r)


"""

# 12 Exercicio.

"""

n = int(input('digite um numero: '))

for r in range(n, 0):
    print(r)

"""

# 13 Exercicio.

"""

n = int(input('digite um numero: '))

for r in range(1, n+1):
    if (r % 2) == 0:
        print(r)

"""

# 14 Exercicio.

"""

n = 1
while (n % 2) != 0:
    n = int(input('digite um numero: '))

for r in range(1, n+1):
    if (r % 2) == 0:
        print(r)

"""

# 15 Exercicio.

"""

n = 0
while (n % 2) != 1:
    n = int(input('digite um numero: '))

for r in range(1, n+1):
    if (r % 2) == 1:
        print(r)

"""

# 16 Exercicio.

"""

n = 0
while (n % 2) != 1:
    n = int(input('digite um numero: '))

for r in range(n, 0):
    if (r % 2) == 1:
        print(r)


"""

# 17 Exercicio.

"""

n = int(input('Digite o numero: '))
s = 0
for i in range(0, n+1):
    s += i
print(s)

"""

# 18 Exercicio.

"""

c1 = int(input('Digite a quantia de numeros: '))
c = 1
s = 0
n2 = 0

while c != (c1 + 1):
    n1 = int(input(f'{c}) Digite um numero: '))
    c += 1
    if n1 > n2:
        n2 = n1
    if n1 == n2:
        s += 1
print(f'O maior numero: {n2}\n'
      f'Vezes lidas: {s}')


"""

# 19 Exercicio.

"""

n = 112
if 100 < n < 1000:
    for n in str(n):
        print(n)

"""

# 20 Exercicio.

"""

d1 = 0
n = 0
while n < 1000:
    n = int(input('Digite um valor: '))
    for i in range(1, n+1):
        if i % 2 == 0:
            d1 += 1
    print(f'Valores lidos: {n} '
          f'Numeros pares: {d1}')

"""

# 21 Exercicio.

"""

n1 = int(input('1) Digite um numero: '))
n2 = int(input('2) Digite um numero: '))
s = 0
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        s += i
    elif i % 2 == 1:
        m = i
        m *= i
print(f'A soma: {s}\n'
      f'A multiplicação: {m}')

"""

# 22 Exercicio.

"""

n1 = int(input('Digite o numero de notas: '))
c = 1
m = 0
n = 0
if 10 >= n1 < 20:
    while c != (n1 + 1):
        n = int(input(f'{c}) Digite sua nota: '))
        c += 1
        m += n

print('Sua media:', n)

"""

# 23 Exercicio.

"""

n = int(input('Digite um numero positivo: '))

if n > 0:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')



"""

# 24 Exercicio.

"""

n = int(input('Digite um numero positivo: '))
s = 0
if n > 0:
    for i in range(1, n + 1):
        if i == n:
            break
        elif n % i == 0:
            s += i
            print(i, end=' ')
print(f'Sua soma: {s}')


"""

# 25 Exercicio.

"""

s = 0

for i in range(1, 1001):
    if (i % 3) == 0 or (i % 5) == 0:
        s += i
print(s)

"""

# 26 Exercicio.

"""


c = int(input('Digite um numero: '))

while (c % 11) != 0 or (c % 13) != 0 or (c % 17) != 0:
    c += 1
print(c)

"""

# 27 Exercicio.

"""

n = 12
h = 1

for i in range(1, n + 1):
    h += 1/i
print(f'Sua serie harmónica: {h:.2f}')


"""

# 28 Exercicio.

"""

n = 5
e = 1
for d in range(1, n + 1):
    var = 1
    for i in range(d, 0, -1):
        var *= i
    e += 1/var
print(f'Seu "E": {e:.4f}')


"""

# 29 Exercicio.

"""

n = 5
e = 0
var = 0
v = 0
for d in range(1, n + 1):
    var += 2
    v += 1
    for i in range(d, 0, -1):
        var *= i
    e += v/var
print(f'Sua "S": {e:.4f}')

"""

# 30 Exercicio.

"""

t = int(input('numero: '))

c1 = 0
c2 = 0
c3 = 0

for i in range(1, t + 1):
    c1 += i
    if i == t:
        if i % 2 == 0:
            c2 += -i + (2 * t - 1)

        elif i % 2 == 1:
            c2 += i + (2 * t - 1)
            c3 += i

        c3 += (2 * t - 1)

        break

    if i % 2 == 0:
        c2 -= i

    elif i % 2 == 1:
        c2 += i
        c3 += i

print(c1)
print(c2)
print(c3)


"""

# 31 Exercicio.

"""

n1 = 1
n2 = 1
s = n1 / n2
for i in range(1, 100):
    n1 += 2
    n2 += 1
    s += n1 / n2
print(s)

"""

# 32 Exercicio.

"""

import random


for i in range(1, 7):
    d1 = random.randint(1, 7)
    d2 = random.randint(1, 7)
    if d1 > d2:
        print(f'D1 maior que d2')
    elif d1 < d2:
        print(f'D1 menor que D2')
    else:
        print('Numeros iguais')


"""

# 33 Exercicio.

"""

c1 = int(input('1) Digite o numero: '))
n1 = int(input('1) Digite o numero: '))
n2 = int(input('1) Digite o numero: '))
c2 = 0
i = -1

while c2 != c1:
    i += 1
    if (i % n1) == 0 or (i % n2) == 0:
        c2 += 1
        print(i, end=', ')


"""

# 34 Exercicio.

"""

c = 0
mmc = False

while not mmc:
    c += 1
    for i in range(1, 21):
        if c % i != 0:
            break
    else:
        mmc = True

print('O menor divisor comum dos números de 1 a 20 é:', c)

"""

# 35 Exercicio.

"""

n1 = int(input('1) Digite um numero: '))
n2 = int(input('2) Digite um numero: '))

if n1 > 0 and n2 > 0:
    s = 0
    for i in range(n1, n2):
        if i % 2 != 0:
            s += i
    print(s)
else:
    print('Numero torto')


"""

# 36 Exercicio.

"""

c1 = 0
c2 = 0

for i in range(1, 11):
    c1 += (i ** 2)
    c2 += i
print(f'A diferença: {(c2 ** 2) - c1}')

"""

# 37 Exercicio.

"""

b1 = 0
b2 = 0


for i in range(1000, 10000):
    x = str(i)
    b1 = (x[:2])
    b2 = (x[2:])
    if ((int(b1) + int(b2)) ** 2) == i:
        print(i)

"""

# 38 Exercicio.

"""



"""

# 39 Exercicio.

"""

b = int(input('Insira a base: '))
h = int(input('Insira a altura: '))
if b > 0 or h > 0:
    print('Sua area:', (h * b) / 2)
else:
    print('Besta')

"""

# 40 Exercicio.

"""

m = True
c = 0
n2 = float('-inf')
n3 = float('inf')

while m is True:
    c += 1
    n1 = int(input(f'{c}) Digite um numero: '))
    if n1 < 0:
        m = False
        break
    else:
        if n1 > n2:
            n2 = n1
        if n1 < n3:
            n3 = n1


print(n3, n2)

"""

# 41 Exercicio.

"""

r1 = int(input('Digite o valor: '))
r2 = int(input('Digite o valor: '))

while r1 != 0 or r2 !=0:
    print(f'Sua resistencia: {(r1 * r2) / (r1 + r2):.2f}')
    r1 = int(input('Digite o valor: '))
    r2 = int(input('Digite o valor: '))
print('Fim')

"""

# 42 Exercicio.

"""

m = False
c = 0

while not m:
    c += 1
    n = int(input(f'{c}) Digite um número: '))
    if n <= 0:
        print('FIM')
        m = True
    else:
        print(f'Raiz quadrada: {(n ** 0.5):.2f}'
              f'\n Seu número elevado ao cubo: {n ** 3}'
              f'\n Seu número elevado ao quadrado: {n ** 2}')

"""

# 43 Exercicio.

"""

m = False
m1 = 0
c = 0

while not m:
    c += 1
    i = int(input(f'{c}) Digite a idade: '))
    m1 += i
    if i != 0:
        continue
    m = True

print('Media:', m1 / (c - 1))

"""

# 44 Exercicio.

"""

n = int(input('Digite um numero: '))
n1, n2 = 1, 1

while n2 <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print(n2)

"""

# 45 Exercicio.

"""

m = False

while not m:
    print()
    print('1) Converta para kilometros '
          '\n2) Converta para metros'
          '\n''"Fim", para finalizar')
    e = input('Escolha uma opção: ')
    match e:
        case '1':
            n1 = float(input('Digite a quantia em metros: '))
            print(f'Valor em kilometros: {n1 / 1000:.2f}')
        case '2':
            n1 = float(input('Digite a quantia em Kilometros: '))
            print(f'Valor em metros: {n1 * 1000}')
            print()
        case 'Fim':
            m = True

"""

# 46 Exercicio.

"""

import random
n1 = random.randint(1, 1000)
print(n1)
m = False
c = 0
while not m:
    c += 1
    n2 = int(input(f'{c}) Digite um número: '))
    if n2 == n1:
        print('Acertou!')
        m = True
        break
    else:
        continue

"""

# 47 Exercicio.

"""

m = False

while not m:
    print('')
    print(f'Adição: opção 1'
          f'\nSubtração: opção 2'
          f'\nMultiplicação: opção 3'
          f'\nDivisão: opção 4'
          f'\nSaida: opção 5')
    op = input('Escolha a opção: ')
    print('')
    match op:
        case 'opção 1':
            print('Opção 1')

            n1 = float(input('1) Digite o numero: '))
            n2 = float(input('2) Digite o numero: '))
            print(f'Subtração: {n1 - n2}')
        case 'opção 3':
            print('Opção 3')

            n1 = float(input('1) Digite o numero: '))
            n2 = float(input('2) Digite o numero: '))
            print(f'Multiplicação: {n1 * n2}')
        case 'opção 4':
            print('Opção 4')

            n1 = float(input('1) Digite o numero: '))
            n2 = float(input('2) Digite o numero: '))
            print(f'Divisão: {n1 / n2}')
        case 'opção 2':
            print('Opção 2')

            n1 = float(input('1) Digite o numero: '))
            n2 = float(input('2) Digite o numero: '))
            print(f'Subtração: {n1 - n2}')
        case 'opção 5':
            print('Opção 5')

            print('Saida.')
            m = True
            break


"""

# 48 Exercicio.

"""

n = 4_000_000
n1, n2 = 1, 1
s = 0

while s <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n2 % 2 == 0:
        s += n2

print(n2)

"""

# 49 Exercicio.

"""

s1 = float(input('1) Salario: '))
s2 = s1 / 3
c = 0
print()
while s2 < s1:
    c += 1
    s1 += (s1 ** 0.2)
    s2 += (s2 ** 0.5)

print(f'Salário 1: {s1:.2f}.\nSalário 2: {s2:.2f}. \nDemorou: {c} meses')


"""

# 50 Exercicio.

"""

ch = 150
z = 110
c = 0
while ch > z:
    c += 1
    ch += 2
    z += 3

print(f'Chico: {ch}.\nZé: {z}. \nDemorou: {c} anos.')

"""

# 51 Exercicio.

"""


ano = 1997
s = 2000
p = 1.5

while ano != 2024:
    ano += 1
    p += p
    print(p)
    s += (s + p)
print(s)

"""

# 52 Exercicio.

"""

vl = int(input('Insira o valor do saque: '))
s = 0

while vl > -1:
    vl -= s
    s = 0
    if vl >= 100:
        s += 100
        print(100)
    elif 100 > vl >= 50:
        s += 50
        print(50)
    elif 50 > vl >= 20:
        print(20)
        s += 20
    elif 20 > vl >= 10:
        print(10)
        s += 10
    elif 10 > vl >= 5:
        s += 5
        print(5)
    elif 5 > vl >= 2:
        print(2)
        s += 2
    elif vl == 1:
        print(1)
        s += 1

ou

cedulas = [100, 50, 20, 10, 5, 2, 1]

vl = int(input('Insira o valor do saque: '))

if vl <= 0:
    print("Valor inválido. O valor do saque deve ser maior que zero.")
else:
    print(f'Serão entregues as seguintes cédulas para o saque de {vl}:')
    for cedula in cedulas:
        if vl >= cedula:
            qtd_cedulas = vl // cedula
            vl -= qtd_cedulas * cedula
            print(f'{qtd_cedulas} cédula(s) de {cedula}')
    if vl > 0:
        print(f'Ficou faltando {vl} para completar o saque.')


"""

# 53 Exercicio.

"""


m = 0
l = []

for i in range(1, 7):
    l.append(i)
    for x in range(len(l)):
        m += 1
        print(m, end=' ')
    print()

"""

# 54 Exercicio.

"""

n = int(input('Digite um número inteiro positivo: '))
p = True if n > 1 else False

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        p = False
        break

if p:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo.')


"""

# 55 Exercicio.

"""


n1 = int(input('Digite um numero: '))
c1 = 0
c2 = 1

while c1 != n1:
    c2 += 1
    for i in range(2, int(c2 ** 0.5) + 1):
        if c2 % i == 0:
            break
    else:
        c1 += 1
        print(c2)


"""

# 56 Exercicio.

"""

n1 = 2_000_000
c1 = 0
c2 = 1
s = 0
while c1 != n1:
    c2 += 1
    for i in range(2, int(c2 ** 0.5) + 1):
        if c2 % i == 0:
            break
    else:
        s += c2
        c1 += 1
print(s)

"""

# 57 Exercicio.

"""

na = int(input('Digite o inicio: '))
nb = int(input('Digite o fim: '))
c1 = 0
c2 = na

while c1 != nb:
    c2 += 1
    for i in range(2, int(c2 ** 0.5) + 1):
        if c2 % i == 0:
            break
    else:
        c1 += 1
        print(c2)


"""

# 58 Exercicio.

"""

na = int(input('Digite o inicio: '))
nb = int(input('Digite o fim: '))
c1 = 0
c2 = na
s = 0
while c1 != nb:
    c2 += 1
    for i in range(2, int(c2 ** 0.5) + 1):
        if c2 % i == 0:
            break
    else:
        s += c2
        c1 += 1
        print(c2)
print(s)


"""

# 59 Exercicio.

"""

n1 = int(input('Numero de habitantes: '))
vk = int(input('Valor do kwh: '))
m = 0

for i in range(1, n1 + 1):
    cm = float(input('Digite o consumo do mes: '))
    cd1 = int(input('Digite o codigo do consumidor Residencial: '))
    cd2 = int(input('Digite o codigo do consumidor Comercial: '))
    cd3 = int(input('Digite o codigo do consumidor Industrial: '))
    if cd3 < cd1 > cd2:
        print('Maior:', cd1)
    elif cd3 < cd2 > cd1:
        print('Maior:', cd2)
    elif cd1 < cd3 > cd2:
        print('Maior:', cd3)
    if cd3 > cd1 < cd2:
        print('Menor:', cd1)
    elif cd1 > cd2 < cd3:
        print('Menor:', cd2)
    else:
        print('Menor:', cd3)
    print(f'Media: {cd1 + cd2 + cd3 / 3}, Consumo total: {cd1 + cd2 + cd3}')

"""

# 60 Exercicio.

"""

c1 = 0
n1 = 1
n2 = 0
n3 = float('inf')

m = True
c2 = 0
np = 0
print('A entrada de dados finalizará com "0".')
print()
s = 0
while n1 != 0:
    c1 += 1
    n1 = int(input(f'{c1}) Digite um numero: '))
    s += n1
    if n1 % 2 == 0:
        np += n1
        c2 += 1
    if n1 > n2:
        n2 = n1
    if n1 < n3:
        n3 = n1
        
print('Soma:', s,
      'Quantos numeros:', (c1 - 1),
      'Media:', (s / (c1 - 1)),
      'Maior:', n2,
      'Menor:', n3,
      'Media dos pares:', np / (c2 - 1))
print('Fim')


"""

# 61 Exercicio.

"""

for i in range(999, 100, -1):

    polindromo = ''

    for j in range(i, 100, -1):
        polindromo = str(i * j)

        if polindromo[::1] == polindromo[::-1]:
            break

    if polindromo[::1] == polindromo[::-1]:
        print(f'{polindromo} = {i} * {j}')
        break

"""

# 62 Exercicio.

"""



"""
