# 22) Escreva um programa em que o utilizador introduz números
# inteiros até introduzir um número em que a soma dos algarismos
# seja superior a 20.

# Variables
numero = 0
soma = 0
numeroClone = 0

# Algorithm
while True:
    # Variables received by input
    numero = int(input('Introduza um numero para fazer a soma dos seus algarismos: '))

    numeroClone = numero

    while numeroClone != 0:
        soma += (numeroClone % 10)
        numeroClone //= 10

    # Print information
    if soma > 20:
        print('Foi introduzido um numero que a soma dos seus algarismos é > 20')
        break