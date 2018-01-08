# 17) Escreva um programa que peça as idades de 32 alunos de uma
# turma. O programa deve guardar estes valores num vetor e no final
# indicar a idade máxima, mínima média e moda da turma.


# Variables
size = 32;
arrayOfNumbers = [];
maximo = 0;
minimo = 99999;
moda = 0;


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def maxAndMinimumValues():
    global maximo;
    global minimo;

    for i in range(0, len(arrayOfNumbers)):
        if arrayOfNumbers[i] > maximo:
            maximo = arrayOfNumbers[i];
        if arrayOfNumbers[i] < minimo:
            minimo = arrayOfNumbers[i];


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

# Print information
arrayOfNumbers = fillArray();
maxAndMinimumValues();
modeValue();

print('O valor maior é: {}\nO menor é: {}\nE a moda é: {}'.format(maximo, minimo, moda));