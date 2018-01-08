# 5) Escreva um programa que determine o 2º maior valor de um vetor.

# Variables
number = 0;
arrayOfTenPositions = [];


# Algorithm
# Functions

def fillArray():
    for i in range(0, 10):
        number = int(input('Introduza um valor: '));
        arrayOfTenPositions.append(number);


def secondBigger():
    maximo = 0;
    secondMaximo = 0;

    for i in range(len(arrayOfTenPositions)):
        if arrayOfTenPositions[i] > maximo:
            secondMaximo = maximo;
            maximo = arrayOfTenPositions[i];
        elif arrayOfTenPositions[i] > secondMaximo and arrayOfTenPositions[i] < maximo:
            secondMaximo = arrayOfTenPositions[i];

    # Print Information
    print('O segundo valor maior guardado é: ', secondMaximo);


# Call function
fillArray();
secondBigger();
