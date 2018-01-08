# 12) Escreva um programa que indique se todos os valores de um
# vetor são iguais, se são todos diferentes, ou se há valores
# repetidos no vetor. Para testar utilize um vetor cujo tamanho e
# valores inteiros são introduzidos pelo utilizador.


# Variables
size = 0;
numero = 0;
arrayOfNumbers = [];

# Variables received by input
size = int(input('Introduza o tamanho do array: '));


# Algorithm
# Functions
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def searchInArray(arrayOfNumbers):
    for i in range(0, len(arrayOfNumbers)):
        for j in range(1, len(arrayOfNumbers)):
            if arrayOfNumbers[i] == arrayOfNumbers[j]:
                return True;
            else:
                return False;


# Print information
arrayOfNumbers = fillArray();

flag = searchInArray(arrayOfNumbers);
if flag:
    print('Foram introduzidos numeros iguas!');
else:
    print('Não foram introduzidos numeros iguais!');
