# 9) Escreva um programa em que o utilizador vai introduzindo
# números positivos até ser introduzido o valor 0 (zero). No fim o
# programa indicará a percentagem de números pares introduzidos.

# Variables received by input
totalNumeroPares = 0
percentagemPares = 0
contadorNumeros = 0

# Algorithm
while True:
    numero = int(input('Introduza um numero: '))
    if numero > 0:
        if numero % 2 == 0:
            totalNumeroPares+=1
        contadorNumeros += 1
    if numero == 0:
        break

percentagemPares = 100 * totalNumeroPares / contadorNumeros

# Print information
print('A percentagem de numeros pares é: {}'.format(percentagemPares))
