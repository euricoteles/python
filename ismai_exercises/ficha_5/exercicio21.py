#  21) Escreva um programa para determinar o valor mais comum (moda)
# num vetor de inteiros. Teste com um vetor de 100 posições preenchido
# aleatoriamente com valores entre 0 e 10.


# Variables
# Import
import random

# Variables
arrayOfNumbers = [];
size = 0;
moda = 0;

# Variables received by input
size = int(input('Introduza o tamanho do array: '));


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = random.randint(0, 10);

    return arrayOfNumbers;


def modeValue():
    global moda;
    maxContador = 0;

    for i in range(0, len(arrayOfNumbers)):
        contador = 0;
        for j in range(0, len(arrayOfNumbers)):
            if arrayOfNumbers[j] == arrayOfNumbers[i]:
                contador += 1
        if contador > maxContador:
            maxContador = contador;
            moda = arrayOfNumbers[i];

    return moda;

arrayOfNumbers = fillArray();
moda = modeValue();
print(arrayOfNumbers);
print('O numero que aparece mais vezes é o:', moda);
