
# Exercicios Seção 2:
"""
Seção 2 de exercicos da geek:
"""

# 1 Exercicio.
"""

n1 = float(input('1) Insira um numero: '))
n2 = float(input('2) Insira um numero: '))

if n1 > n2:
    print(n1)
else:
    print(n2)


"""

# 2 Exercicio.
"""

n1 = int(input('Digite um numero: '))
if n1 > 0:
    print(f'A raiz quadrada do seu numero é: {(n1 ** 0.5):.2f}')
else:
    print('Insire um numero positivo.')

"""

# 3 Exercicio.
"""

n1 = int(input('Digite um numero: '))
if n1 > 0:
    print(f'A raiz quadrada do seu numero é: {(n1 ** 0.5):.2f}')
else:
    print(f'Seu numero ao quadrado: {(n1 ** 2):.2f}')


"""

# 4 Exercicio.
"""

n1 = int(input('Digite um numero: '))

if n1 > 0:
    print(f'A raiz quadrada do seu numero é: {(n1 ** 0.5):.2f}')
    print(f'O seu numero ao quadrado: {n1 ** 2}')
else:
    print('Insire um numero positivo.')


"""

# 5 Exercicio.
"""

n1 = int(input('Digite um numero: '))

if (n1 % 2) == 1:
    print('Numero é Impar.')
else:
    print('Numero é Par')


"""

# 6 Exercicio.
"""

n1 = int(input('1) Digite um numero: '))
n2 = int(input('2) Digite um numero: '))

if n1 > n2:
    print(f'O Primeiro numero é maior que o segundo, e sua diferença é: {n1 - n2} ')
else:
    print(f'O Segundo numero é maior que o primeiro, e sua diferença é: {n2 - n1} ')


"""

# 7 Exercicio.
"""

n1 = int(input('1) Digite um numero: '))                
n2 = int(input('2) Digite um numero: '))                
                                                        
if n1 > n2:                                             
    print(f'O Primeiro numero é maior que o segundo')   
elif n1 == n2:                                          
    print(f'Numeros iguais')                            
else:                                                   
    print(f'O Segundo numero é maior que o primeiro')

"""

# 8 Exercicio.
"""

n1 = float(input('1) Digite um numero: '))
n2 = float(input('2) Digite um numero: '))
m = (n1 + n2) / 2
if m > 10:
    print(f'A Nota Inserida ({m}), é invalida.')
elif m < 0:
    print(f'A Nota Inserida ({m}), é invalida.')
else:
    print(f'A Media do Aluno: {m}')

"""

# 9 Exercicio.
"""

s = float(input('Insira seu salário: '))
v = float(input('Insira o valor da prestação: '))
p1 = (v / s) * 100

if p1 < 21:
    print('Emprestimo concedido!')
else:
    print('Emprestimo Negado.')


"""

# 10 Exercicio.
"""

print('Digite seu sexo...')
s = int(input('Digite (1), para homem e (2) para mulher: '))

if s == 1:
    a = float(input('Insira sua altura: '))
    print(f'Seu peso ideal é {((72.7 * a) - 58):.2f}')

elif s == 2:
    a = float(input('Insira sua altura: '))
    print(f'Seu peso ideal é {((62.1 * a) - 44.7):.2f}')

else:
    print(f'Você digitou um numero errado')

"""

# 11 Exercicio.
"""

n = input('Digite um numero inteiro: ')
soma = 0
i = 0

if int(n) < 0:
    print('Voce digitou um numero negativo.')
else:
    for digito in n:
        soma += int(digito)
if int(n) > 0 or int(n) == 0:
    print(f'Sua soma foi {soma}')

"""

# 12 Exercicio.
"""

b = int(input('Insira o a base do logaritmo: '))
n = int(input('Insira o numero do logaritmo: '))
l = 1  # Começa com 1 para multiplicação

if b <= 0:
    print('A base deve ser um número positivo e diferente de zero!')
elif n <= 0:
    print('O número deve ser um número positivo e diferente de zero!')
else:
    while n >= b:
        n /= b
        l += 1

print("O logaritmo é:", l)

"""

# 13 Exercicio.
"""

n1 = int(input('1) Insira sua nota: '))
n2 = int(input('2) Insira sua nota: '))
n3 = int(input('3) Insira sua nota: '))

m = (n1 + n2 + (n3 * 2)) / 4

if m > 59:
    print('Voce passou! Sua nota final:', m)
else:
    print('Voce REPROVOU! Sua nota final:', m)

"""

# 14 Exercicio.
"""

n1 = int(input('1) Insira sua nota: '))
n2 = int(input('2) Insira sua nota: '))
n3 = int(input('3) Insira sua nota: '))

m = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

if m < 3:
    print('Voce REPROVOU! Sua nota final:', m)
elif m < 5:
    print('Voce esta de REC! Sua nota final:', m)
else:
    print('Voce passou! Sua nota final:', m)

"""

# 15 Exercicio.
"""

dia = int(input('Escolha o dia: '))
match dia:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sabado")
if dia < 1 or dia > 8:
    print('Voce digitou um numero não correspondente:', dia)


"""

# 16 Exercicio.
"""

dia = int(input('Escolha o dia: '))
match dia:
    case 1: print("Janeiro")
    case 2: print("Fevereiro")
    case 3: print("Março")
    case 4: print("Abril")
    case 5: print("Maio")
    case 6: print("Junho")
    case 7: print("Julho")
    case 8: print("Agosto")
    case 9: print("Setembro")
    case 10: print("Outubro")
    case 11: print("Novembro")
    case 12: print("Dezembro")
if dia < 1 or dia > 12:
    print('Voce digitou um numero não correspondente:', dia)


"""

# 17 Exercicio.
"""

b1 = float(input('Digite a base maior: '))
b2 = float(input('Digite a base menor: '))
al = float(input('Digite a altura: '))
if b1 > 1 and b2 > 1:
    a = (b1 + b2) * al / 2
    print(f'A area do seu trapezio: {a} ')
else:
    print('Voce digitou um numero menor que zero')

"""

# 18 Exercicio.
"""

op = int(input(f'Digite qual operação matematica voce deseja das seguintes opções: '
               f'\n Soma: 1'
               f'\n Divisão: 2'
               f'\n Multiplicação: 3'
               f'\n Raiz Quadrada: 4'
               f'\n Digite qual voce deseja: '))

if op == 4:
    n1 = float(input('1) Digite o seu numero: '))
elif 4 > op > 0:
    n1 = float(input('1) Digite o seu numero: '))
    n2 = float(input('2) Digite o seu numero: '))
else:
    print('Digite um numero valido!', op)

match op:
    case 1: print(f'Sua soma é: {n1 + n2} ')
    case 2: print(f'Sua divisão é: {n1 / n2}')
    case 3: print(f'Sua Multiplicação é: {n1 * n2}')
    case 4: print(f'Sua Raiz é: {(n1 ** 0.5):.2f}')


"""

# 19 Exercicio.

"""

n1 = int(input("Digite um numero inteiro: "))
d1 = n1 % 5
d2 = n1 % 3

if d1 == 0:
    print('Seu numero é divisivel por 5')
elif d2 == 0:
    print('Seu numero é divisivel por 3')
else:
    print('Seu numero não é divisivel')


"""

# 20 Exercicio.
"""

a = float(input('Digite o lado A do triangulo: '))
b = float(input('Digite o lado B do triangulo: '))
c = float(input('Digite o lado C do triangulo: '))

if a < 1 < b or c < 1:
    print('Triangulo invalido.')
else:
    if (a + b) > c and (c + a) > b and (b + c) > a:
        print('Seu triangulo é valido.')
        if a == b == c:
            print('Seu triangulo é um equilátero.')
        elif a == b or a == c or b == c:
            print('Seu triangulo é isósceles.')
        else:
            print('Seu triangulo é escaleno.')


"""

# 21 Exercicio.
"""

print(f' 1- Soma de 2 numeros.'
      '\n 2- Diferença entre 2 numeros (maior pelo menor).'
      '\n 3- Produto entre 2 numeros.'
      '\n 4- Divisão entre 2 numeros (o denominador não pode ser zero).')

op = int(input('Escolha a opção: '))
if op == 4:
    n1 = int(input('1) Digite seu numero: '))
    n2 = int(input('2) Digite seu denominador: '))
    if n2 == 0:
        print('Operação invalida!')
    else:
        print(f'Seu resultado é: {(n1 / n2):.2f}')
elif 0 > op < 4:
    n1 = int(input('1) Digite seu numero: '))
    n2 = int(input('2) Digite seu numero: '))
else:
    print('Resultado invalido!')

match op:
    case 1: print(f'Sua soma: {n1 + n2}')
    case 2: print(f'A diferença dos mesmos: {n1 - n2}')
    case 3: print(f'A sua Multiplicação: {n1 * n2}')


"""

# 22 Exercicio.
"""

i = int(input('Digite a sua idade: '))
t = int(input('Digite a seu tempo de serviço: '))

if i > 64 or t > 29:
    print('Sua aposentadoria é valida!')
elif i > 59 and i > 24:
    print('Sua aposentadoria é valida!')
else:
    print('Sua aposentadoria é invalida...')

"""

# 23 Exercicio.
"""

a = int(input('Digite o seu ano: '))
d1 = a % 400
d2 = a % 4
d3 = a % 100

if d1 == 0 or d2 == 0 and d3 != 0:
    print('Seu ano é bissexto!')
else:
    print('Seu ano não é bissexto...')

"""

# 24 Exercicio.
"""

print("Estados: MG 7%"
      "\n SP 12%"
      "\n RJ 15%"
      "\n MS 8%")
es = input('Digite o estado: ')
es = es.upper()
v = float(input('Digite o valor: '))
if es not in ['MG', 'SP', 'RJ', 'MS']:
    print('Nome invalido', es)
else:
    match es:
        case 'MG':
            print(f'Seu produto vale: {(v ** 0.7) + v:.2f}. \nCom o acrescimo sendo: {(v ** 0.7):.2f}')
        case 'SP':
            print(f'Seu produto vale: {(v ** 0.12) + v:.2f}. \nCom o acrescimo sendo: {(v ** 0.12):.2f}')
        case 'RJ':
            print(f'Seu produto vale: {(v ** 0.15) + v:.2f}. \nCom o acrescimo sendo: {(v ** 0.15):.2f}')
        case 'MS':
            print(f'Seu produto vale: {(v ** 0.8) + v:.2f}. \nCom o acrescimo sendo: {(v ** 0.8):.2f}')


"""

# 25 Exercicio.
"""



"""

# 26 Exercicio.
"""

km = float(input('Insira a kilometragem: '))
l = float(input('Digite a quantia de gasolina: '))
m = km / l
if m < 8:
    print('Venda o carro!')
elif 7 > m < 15:
    print('Econômico!')
elif m > 12:
    print('Super econômico!')


"""

# 27 Exercicio.
"""

i = int(input('Insira sua idade: '))

if i > 4:
    if 4 < i < 8:
        print('Infantil A')
    elif 7 < i < 11:
        print('Infantil B')
    elif 10 < i < 14:
        print('Juvenil A')
    elif 13 < i < 18:
        print('Juvenil B')
    else:
        print('Senior')


"""

# 28 Exercicio.
"""

x = float(input('1) Digite seu numero: '))
y = float(input('2) Digite seu numero: '))
z = float(input('3) Digite seu numero: '))
g = (x * y * z) ** (1/3)
p = (x + 2 * y + 3 * z) / 6
h = (1 / (1/x) + (1/y) + (1/z))
a = (x + y + z) / 3

print(f'As suas medias são: '
      f'\n Geometrica: {g:.2f}'
      f'\n Ponderada: {p:.2f}'
      f'\n Harmonica: {h:.2f}'
      f'\n Aritmetica: {a:.2f}')


"""

# 29 Exercicio.
"""

import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
a = 0
e = 0

r1 = int(input(f'1) Qual a soma de {n1} + {n2}? '
               f'\nResposta: '))

if r1 == (n1 + n2):
    a += 1
if r1 != (n1 + n2):
    e += 1

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

r2 = int(input(f'2) Qual a soma de {n1} + {n2}? '
               f'\nResposta: '))

if r2 == (n1 + n2):
    a += 1
if r2 != (n1 + n2):
    e += 1

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

r3 = int(input(f'3) Qual a soma de {n1} + {n2}? '
               f'\nResposta: '))

if r3 == (n1 + n2):
    a += 1
if r3 != (n1 + n2):
    e += 1

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

r4 = int(input(f'4) Qual a soma de {n1} + {n2}? '
               f'\nResposta: '))

if r4 == (n1 + n2):
    a += 1
if r4 != (n1 + n2):
    e += 1

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

r5 = int(input(f'5) Qual a soma de {n1} + {n2}? '
               f'\nResposta: '))
if r5 == (n1 + n2):
    a += 1
if r5 != (n1 + n2):
    e += 1

print('Seus acertos:', a)
print('Seus erros:', e)


"""

# 30 Exercicio.
"""

n1 = int(input('1) Insira o numero: '))
n2 = int(input('2) Insira o numero: '))
n3 = int(input('3) Insira o numero: '))

l = [n1, n2, n3]
l.sort()
print(l)

"""

# 31 Exercicio.
"""

a = float(input('Insira sua altura: '))
p = float(input('Insira seu peso: '))

if a < 1.20:
    if p < 60:
        print('Sua classificação: A')
    elif 59 < p < 90:
        print('Sua classificação: D')
    else:
        print('Sua classificação: G')

elif 1.21 < a < 1.71:
    if p < 60:
        print('Sua classificação: B')
    elif 59 < p < 90:
        print('Sua classificação: E')
    else:
        print('Sua classificação: H')

elif a > 1.70:
    if p < 60:
        print('Sua classificação: C')
    elif 59 < p < 90:
        print('Sua classificação: F')
    else:
        print('Sua classificação: I')


"""

# 32 Exercicio.
"""

print(f'Cardápio:'
      f'\n Cachorro quente: 100/1,20'
      f'\n Bauru Simples: 101/1,30'
      f'\n Bauru Com Ovo: 102/1,50'
      f'\n Hamburguer: 103/1,20'
      f'\n Cheeseburger: 104/1,70'
      f'\n '
      f'\n Suco: 105/2,20'
      f'\n Refrigerante: 106/ 1,00'
      f'\n ')

c = int(input("Digite o código: "))

if 99 < c < 107:
    match c:
        case 100:
            print('Cachorro quente, o preço foi de: 1.20 reais')
        case 101:
            print('Bauru Simples, o preço foi de: 1.30 reais')
        case 102:
            print('Bauru Com Ovo, o preço foi de: 1.50 reais')
        case 103:
            print('Hamburguer, o preço foi de: 1.20 reais')
        case 104:
            print('Cheeseburger, o preço foi de: 1.70 reais')
        case 105:
            print('Suco, o preço foi de: 2.20 reais')
        case 106:
            print('Refrigerante, o preço foi de: 1.00 reais')
else:
    print('Código Invalido: ', c)

"""

# 33 Exercicio.
"""

p = float(input('Digite o preço: '))
n = 0
if p < 51:
    n = p * 0.05
    print(f'O aumento foi de: {p * 0.05} (5%)')
elif 50 < p < 101:
    n = p * 0.10
    print(f'O aumento foi de: {p * 0.10} (10%)')
elif p > 100:
    n = p * 0.15
    print(f'O aumento foi de: {p * 0.15} (15%)')
if n < 81:
    print('Barato')
elif 80 < n < 121:
    print('Normal')
elif 120 < n < 201:
    print('Caro')
elif n > 199:
    print('Muito caro')

"""

# 34 Exercicio.
"""

f = int(input('Digite a quantia de falta: '))
n = float(input('Digite a nota do aluno: '))
if f <= 20:
    if 9 <= n < 10:
        print('Sua nota: A')
    elif 7.5 <= n <= 8.9:
        print('Sua nota: B')
    elif 5.0 <= n <= 7.4:
        print('Sua nota: C')
    elif 4.0 <= n <= 4.9:
        print('Sua nota: D')
    elif 0 <= n <= 3.9:
        print('Sua nota: E')
else:
    if 9 <= n < 10:
        print('Sua nota: B')
    elif 7.5 <= n <= 8.9:
        print('Sua nota: C')
    elif 5.0 <= n <= 7.4:
        print('Sua nota: D')
    elif 4.0 <= n <= 4.9:
        print('Sua nota: E')
    elif 0 <= n <= 3.9:
        print('Sua nota: E')


"""

# 35 Exercicio.
"""

d = int(input("Digite um dia: "))
m = int(input('Digite um mês: '))
a = int(input('Digite o seu ano: '))

if 0 < a <= 2024:
    if m == 2:
        d1 = a % 400
        d2 = a % 4
        d3 = a % 100
        ab = d1 == 0 or d2 == 0 and d3 != 0
        if ab is True:
            if 0 < d <= 29:
                print('Sua data é valida')
            elif d > 29:
                print('data invalida!')
        elif ab is False:
            if 0 < d <= 28:
                print('data valida')
            elif d > 29:
                print('Data invalida')
    elif 0 < m <= 12 and m != 2:
        if 0 < d <= 31:
            print('Seu data é valida!')
else:
    print('data invalida')

"""

# 36 Exercicio.
"""

v = float(input('Insira sua venda: '))

if v >= 100_000_00:
    print(f'Sua comissão: {(700 + (v ** 0.16)):.2f}')

elif 100_000_00 > v >= 80_000_00:
    print(f'Sua comissão: {(650 + (v ** 0.14)):.2f}')

elif 80_000_00 > v >= 60_000_00:
    print(f'Sua comissão: {(600 + (v ** 0.14)):.2f}')

elif 60_000_00 > v >= 40_000_00:
    print(f'Sua comissão: {(550 + (v ** 0.14)):.2f}')

elif 40_000_00 > v >= 20_000_00:
    print(f'Sua comissão: {(500 + (v ** 0.14)):.2f}')
    
elif v < 20_000_00:
    print(f'Sua comissão: {(400 + (v ** 0.14)):.2f}')


"""

# 37 Exercicio.
"""

h1 = int(input('Insira a hora de entrada: '))
m1 = int(input('Insira o minuto de entrada: '))

h2 = int(input('Insira a hora de saida: '))
m2 = int(input('Insira o minuto de saida: '))

mt = (h2 - h1) * 60 + (m2 - m1)

ht = mt // 60
if mt % 60 > 0:
    ht += 1

if h2 < h1 or (h2 == h1 and m2 < m1):
    ht += 24

if ht > 0:
    if ht <= 2:
        print('1) Total a pagar:', ht * 1)
    elif ht == 3 or ht == 4:
        print('2) Total a pagar:', ht * 1.40)
    elif ht >= 5:
        print('3) Total a pagar:', ht * 2)


"""

# 38 Exercicio.
"""

d = int(input("Digite um dia: "))
m = int(input('Digite um mês: '))
a = int(input('Digite o seu ano: '))
p = 2, 9, 6, 11

if 0 < a <= 2024:
    if 9 == m or m == 6 or m == 11:
        if 0 < d <= 30:
            print('Data valida!')
        else:
            print('Data invalida')
    elif m == 2:
        d1 = a % 400
        d2 = a % 4
        d3 = a % 100
        ab = d1 == 0 or d2 == 0 and d3 != 0
        if ab is True:
            if 0 < d <= 29:
                print('Sua data é valida')
            elif d > 29:
                print('data invalida!')
        elif ab is False:
            if 0 < d <= 28:
                print('data valida')
            elif d > 28:
                print('Data invalida')
    elif 0 < m <= 12 and m is not p:
        if 0 < d <= 31:
            print('Seu data é valida!')
        else:
            print(' Sua data é invalida!')
else:
    print('data invalida')


"""

# 39 Exercicio.
"""

s = float(input('Coloque seu salario: '))
if s < 500.00:
    print(f'Seu novo salario: {s ** 0.25}, seu tempo de serviço, abaixo de 1 ano.')
if s < 1000.00:
    print(f'Seu novo salario: {s ** 0.20}, seu tempo de serviço, de 1 a 3 anos. Bonus: 100 ')
if s < 1500.00:
    print(f'Seu novo salario: {s ** 0.15}, seu tempo de serviço, de 4 a 6 anos. Bonus: 200 ')
if s < 2000.00:
    print(f'Seu novo salario: {s ** 0.10}, seu tempo de serviço, 7 a 10 anos. Bonus: 300 ')
if s > 2000.00:
    print(f'seu tempo de serviço: abaixo de 1 ano. Seu Bonus: 500 ')


"""

# 40 Exercicio.
"""

c = float(input('Digite o custo de fabrica: '))

if c <= 12_000.00:
    print(f'Custo: {c ** 0.05}')
elif 12_000.00 < c <= 25_000.00:
    print(f'Custo: {(c ** 0.10) ** 0.15}')
elif c > 25_000.00:
    print(f'Custo: {(c ** 0.15) ** 0.20}')


"""

# 41 Exercicio.
"""


a1 = int(input('Insira sua altura: '))
p = int(input('Qual seu peso atual: '))
a2 = a1 / 100
imc = p / a2 ** 2
print(f'seu imc: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do Peso!')
elif 24.9 > imc > 18.6:
    print('Saudável!')
elif 29.9 > imc > 25:
    print('Peso em excesso!')
elif 34.9 > imc > 30:
    print('Obesidade Grau I')
elif 39.9 > imc > 35:
    print('Obesidade Grau II')
elif imc > 40:
    print('Obesidade Grau III')


"""
