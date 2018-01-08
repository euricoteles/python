import math

# crie um script que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# variables received by input
number = int(input('introduza um numero: '))

# print information
print('o dobro do numero lido é: {}! o triplo é {}! e a raiz quadrada é {}'.format(number*2, number*3, math.sqrt(number)))