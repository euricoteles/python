#  2) Escreva um programa para determinar o valor menos comum
# num vetor de inteiros. Teste com um vetor de 100 posições preenchido
# aleatoriamente com valores entre 0 e 10.


# Variables
# Import
import random

# Variables
arrayOfNumbers = [];
size = 0;
moda = 0;
min = 0;

# Variables received by input
size = int(input('Introduza o tamanho do array: '));


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = random.randint(0, 10);

    return arrayOfNumbers;


def minValue():
    global moda;
    maxContador = 0;
    minContador = 101;
    global min;

    for i in range(0, len(arrayOfNumbers)):
        contador = 0;
        for j in range(0, len(arrayOfNumbers)):
            if arrayOfNumbers[j] == arrayOfNumbers[i]:
                contador += 1
        if contador > maxContador:
            maxContador = contador;
            moda = arrayOfNumbers[i];
        if contador < minContador:
            minContador = contador;
            min = arrayOfNumbers[i];

    return min;

arrayOfNumbers = fillArray();
min = minValue();
print(arrayOfNumbers);
print('O numero que aparece menos vezes é o:', min);