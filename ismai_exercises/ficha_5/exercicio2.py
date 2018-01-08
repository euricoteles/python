# 2) Escreva um programa que procure e indique o maior valor (e a
# respetiva posição) de um vetor de 10 posições introduzido pelo
# utilizador.

# Variables
number = 0;
arrayOfTenPositions = [];
posicao = 0;


# Algorithm
# Functions
def fillArray():
    for i in range(0, 10):
        number = int(input('Por favor introduza um valor: '));
        arrayOfTenPositions.append(number);


def searchInArray():
    maximo = 0;
    for i in range(len(arrayOfTenPositions)):
        if arrayOfTenPositions[i] > maximo:
            maximo = arrayOfTenPositions[i];
            posicao = i;

    # Print Information
    print('O maior valor no array é:', maximo, 'e encontra-se na posição', posicao);


# Call the functions
fillArray();
searchInArray();
