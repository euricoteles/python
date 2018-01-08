# 13) [utilização de flags (ou não...)]. Escreva um programa que leia
# n números (sendo n introduzido pelo utilizador) e indique se os
# números são todos pares, se são todos ímpares ou se há ambos os
# tipos.


# Variables
pares = False
impares = False
nVezes = 0

# Variables received by input
nVezes = int(input('Introduza o numero de vezes que quer introduzir numeros: '))

# Algorithm

for i in range(0, nVezes):
    numero = int(input('Introduza um numero: '))
    if numero % 2 == 0 :
        pares = True
    else:
        impares = True

# Print information
if pares == True and impares == False :
    print('Todos os numeros introduzidos são todos pares!')
elif impares == True and pares == False:
    print('Os numeros introduzidos são todos impares!')
else:
    print('Existem numeros pares e impares nos numeros introduzidos!')