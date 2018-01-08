# 11) Escreva um programa que leia 10 números inteiros e indique se
# um número é igual ao anterior. No final deverá indicar quantos
# números introduzidos são iguais ao anterior.

# Variables
numeroRepetido = 0
numeroRepetidoClone = 0
totalNumerosRepetidos = 0

# Algorithm
for i in range(1, 10):
    numero = int(input('Introduza um numero: '))
    if numero == numeroRepetido or numero == numeroRepetidoClone:
        numeroRepetidoClone = numeroRepetido
        totalNumerosRepetidos += 1
    numeroRepetido = numero

# Print information
print('Foram introduzidos {} numeros repetidos!'.format(totalNumerosRepetidos))