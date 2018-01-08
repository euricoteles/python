# 19) Escreva um programa que leia 10 números do utilizador e
# indique, no fim, quantos números são primos, quantos são pares e
# quantos são divisíveis por 3.


# Variables
numero = 0
div = 0
contadorNumeros = 0
contadorPrimos = 0
contadorPares = 0
contadorDivisiveis = 0

# Algorithm
while contadorNumeros < 10:
    # Variables received by input
    numero = int(input('Introduza um numero: '))

    for i in range(1, numero + 1):
        if numero % i == 0:
            div += 1

    if div == 2:
        contadorPrimos += 1
    else:
        div = 0

    if numero % 2 == 0:
        contadorPares += 1

    if numero % 3 == 0:
        contadorDivisiveis += 1

    contadorNumeros += 1

# Print information
print('Houve {} numeros primos, {} numeros pares, {} numeros divisiveis por 3!'.format(contadorPrimos, contadorPares, contadorDivisiveis))