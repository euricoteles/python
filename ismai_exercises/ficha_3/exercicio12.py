# 12) [utilização de flags]. Escreva um programa que leia n números
# (sendo n introduzido pelo utilizador) e indique se os números são
# todos iguais.

# Variables
numeroRepetido = 0
repetido = True
nVezes = 0

# Variables received by input
nVezes = int(input('Introduza o numero de vezes que quer introduzir numeros: '))

# Algorithm

numeroRepetido = int(input('Introduza um numero: '))

for i in range(1, nVezes):
    numero = int(input('Introduza um numero: '))
    if numero != numeroRepetido:
        repetido = False
    numeroRepetido = numero

# Print information
if repetido == True:
    print('Todos os numeros introduzidos são iguas!')
else:
    print('Os numeros introduzidos não são iguais!')