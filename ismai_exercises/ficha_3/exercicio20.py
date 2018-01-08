# 20) Escreva um programa em que o utilizador introduza números até
# introduzir um número par seguido de um número ímpar.

# Variables
numero = 0
numeroClone = 0

# Algorithm
while True:
    # Variables received by input
    numero = int(input('Introduza um numero: '))
    numeroClone = int(input('Introduza um numero: '))

    # Print information
    if numero % 2 == 0 and numeroClone % 2 != 0:
        print('Foi introduzido um numero par seguido de um impar!')
        break;