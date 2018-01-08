# 17) [utilização de flags]. Crie um programa que determine se um
# número inteiro é primo.

# Variables
numero = 0
div = 0

# Variables received by input
numero = int(input('Introduza um numero para ver se é primo: '))

# Algorithm
for i in range(1, numero + 1):
    if numero % i == 0:
        div += 1

# Print information
if div == 2:
    print('O número {} é primo!'.format(numero))
else:
    print("O número {} não é primo!".format(numero))