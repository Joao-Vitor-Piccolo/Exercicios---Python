# Exercicios de List Comprehensions:

"""
========================================================================
1)

# Find all of the numbers from 1-1000 that are divisible by 7:

print([numero for numero in range(1, 1001) if numero % 7 == 0])

========================================================================

# Find all of the numbers from 1-1000 that have a 3 in them:

numeros_com_3 = [int(numero) for numero in range(1, 21) if '3' in str(numero)]
print(numeros_com_3)
print(type(numeros_com_3[0]))
========================================================================
2)

# Count the number of spaces in a string:

string = 'Geek University'
palavras = [palavra for palavra in string.split(' ')]
print(len(palavras) - 1)

ou

espacos = [item for item in string if item == ' ']
print(len(espacos))

========================================================================
3)

# Create a list of all the consonants in the string
# “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
              'v', 'x', 'y', 'w', 'z']

string = '“Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”'

consoantes2 = [consoante for consoante in string if consoante in consoantes]
print(consoantes2)

========================================================================
4)

# Get the index and the value as a tuple for items in the list
# “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)


tupla = ('hi', 4, 8.99, 'apple', ('t,b','n'))
print(tuple([(indices, itens) for indices, itens in enumerate(tupla)]))

========================================================================
5)

# Find the common numbers in two lists
# (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = 1, 2, 3, 4
list_b = 2, 3, 4, 5

print([numero for numero in list_a if numero in list_b])

========================================================================
6)

# Get only the numbers in a sentence like:
# ‘In 1984 there were 13 instances of a protest with over 1000 people attending’

string = '‘In 1984 there were 13 instances of a protest with over 1000 people attending’'
items = string.split()
set = set([int(item) for item in items for letra in item if letra in ['1','2','3','4','5','6','7','8','9','0']])
print(list(set))

========================================================================
7)

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even,
# and the word ‘odd’ if the number is odd. Result would look like: ‘odd’, ’odd’, ‘even’

[print('Even', end=" ") if numero % 2 == 0 else print('Odd', end=" ") for numero in range(20)]

========================================================================
8)

# Produce a list of tuples consisting of only the matching numbers in these
# lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

list_a = 1, 2, 3, 4, 5, 6, 7, 8, 9
list_b = 2, 7, 1, 12

tupla = [(numero, numero) for numero in list_a if numero in list_b]
print(tupla)

========================================================================
9)

# Find all of the words in a string that are less than 4 letters

string = 'Geek SOS University SOS SOS '

print([palavra for palavra in string.split() if len(palavra) < 4])

========================================================================
10)

# Use a nested list comprehension to find all of the numbers
# from 1-1000 that are divisible by any single digit besides 1 (2-9)

numeros = [numero for numero in range(1,1000) if True in [True for i in range(2,10) if numero % i == 0]]
print(numeros)

========================================================================

# Get only the last names:

escritores = [
    "Jane Austen",
    "William Shakespeare",
    "J.K. Rowling",
    "Ernest Hemingway",
    "F. Scott Fitzgerald",
    "George R.R. Martin",
    "T.S. Eliot",
    "James Joyce",
    "Charlotte Brontë",
    "Herman Melville",
]

print([nomes.split()[-1] for nomes in escritores])

"""

# Exercicios de Lambda Python:

"""
========================================================================
1) 

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an 
# argument, also create a lambda function that multiplies argument x with argument y and prints the result.

quinze = lambda x: x + 15

multiplica = lambda x, y: x * y

print(multiplica(quinze(10), quinze(10)))

========================================================================
2)

# Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.

========================================================================

"""

escritores = [
    "Jane Austen",
    "William Shakespeare",
    "J.K. Rowling",
    "Ernest Hemingway",
    "F. Scott Fitzgerald",
    "George R.R. Martin",
    "T.S. Eliot",
    "James Joyce",
    "Charlotte Brontë",
    "Herman Melville",
]
sobrenomes = (nomes.split()[-1] for nomes in escritores)

if __name__ == "__main__":
    print(list(sobrenomes))
