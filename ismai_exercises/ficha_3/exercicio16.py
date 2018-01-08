# 16) Escreva um programa que some os algarismos de um número.

# Variables
numero = 0
soma = 0
numeroClone = 0

# Variables received by input
numero = int(input('Introduza um numero para fazer a soma dos seus algarismos: '))

# Algorithm
numeroClone = numero

while numeroClone != 0:
    soma += (numeroClone % 10)
    numeroClone /= 10

# Print information
print('A soma dos algarismos do numero {} é : {}'.format(numero, soma))