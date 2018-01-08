# 25) Crie um programa que imprima um número de 4 dígitos invertido
# (ex. 4536 -> 6354).

# Variables
numero = 0
numeroInvertido = 0
resto = 0

# Algorithm
numero = int(input('Introduza um numero: '))

while numero != 0:
    resto = numero % 10
    numeroInvertido = (numeroInvertido * 10) + resto
    numero = numero // 10

# Print information
print("Reverse of entered number is = %d" %numeroInvertido)