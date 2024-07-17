
# Exercicio 1
# -=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-
"""
with open('arq.txt', 'a') as arquivo:
    while True:
        item = str(input('Digite um charactere, ou digite "0" para sair: '))
        if item == '0':
            break
        arquivo.write(item + '\n')

arquivo = open('arq.txt')
print(arquivo.read())
arquivo.close()
"""
# -=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-
# Exercicio 2
"""
arquivo = str(input('Digite o nome do arquivo: '))

from meu_pacote.alfabeto import vogais, consoantes

vogais()
consoantes()
if '.txt' not in arquivo:
    arquivo += '.txt'
with open(arquivo, 'r') as leitura:
    leitura = leitura.read()
    letras_v = [letra for letra in leitura if letra in vogais()]
    letras_c = [letra for letra in leitura if letra in consoantes()]

print(letras_c)
print(letras_v)
print(len(letras_c))
print(len(letras_v))
"""
# -=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-

# Exercicio 3

"""

arquivo = str(input('Digite o nome do arquivo: '))

if '.txt' not in arquivo:
    arquivo += '.txt'
with open(arquivo, 'r') as leitura:
    leitura = len(leitura.readlines())
    print(leitura)

"""

if __name__ == '__main__':
    arquivo = open('texto.txt', 'r')
    while True:
        leitura = arquivo.readline()
        print(leitura, end=' ')
        r = str(input('Voce quer parar de ler? '))
        r = r.title()
        if r == 'Sim':
            arquivo.close()
            break
