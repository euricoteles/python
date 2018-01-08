# 15) Escreva um programa que calcule o fatorial de um número.

# Variables
numero = 0
fatorial = 1

# Variables received by input
numero = int(input('Introduza o numero para fazer o factorial: '))

# Algorithm
for i in range(1, numero):
        fatorial += (fatorial * i)

# Print information
print('O fatorial do numero {} é : {}'.format(numero, fatorial))