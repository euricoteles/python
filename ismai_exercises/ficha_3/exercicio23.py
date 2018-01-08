# 23) Escreva um programa que indique ao utilizador todos os números
# primos entre dois números inteiros introduzidos pelo utilizador.

# Variables
numero = 0
numeroDois = 0
maximo = 0
minimo = 0
minimoClone = 0
div = 0


# Algorithm

numero = int(input('Introduza um numero: '))
numeroDois = int(input('Introduza um numero: '))

# Define o limite do menor para o maior
if numero > numeroDois:
    maximo = numero
    minimo = numeroDois
else:
    maximo = numeroDois
    minimo = numero

for i in range(minimo, maximo+1):
    # numeros primos > que 1
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        # Print information
        else:
            print(i)
