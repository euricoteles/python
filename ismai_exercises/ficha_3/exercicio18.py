# 18) Escreva um programa em que o utilizador vai introduzindo
# números inteiros positivos até o número introduzido ser um número
# primo.


# Variables
numero = 0
div = 0


# Algorithm
while True:
    # Variables received by input
    numero = int(input('Introduza um numero para ver se é primo: '))

    for i in range(1, numero + 1):
        if numero % i == 0:
            div += 1

    # Print information
    if div == 2:
        print('O número {} é primo!'.format(numero))
        break;
    else:
        div = 0