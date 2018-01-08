# 21) [utilização de flags]. Escreva um programa que leia 10 valores
# do utilizador e indique no fim se foi introduzido algum número
# divisível por 7.

# Variables
numero = 0
flag = False

# Algorithm
for i in range(0, 10):
    # Variables received by input
    numero = int(input('Introduza um numero: '))

    if numero % 7 == 0:
        flag = True

# Print information
if flag:
    print('Nos numeros introduzidos foi introduzido um que era divisivel por 7!')
else:
    print('Nos numeros introduzidos não foi introduzido numeros que eram divisiveis por 7!')