# 13) Crie um programa que leia um vetor de inteiros cujo tamanho
# será introduzido pelo utilizador, tamanho esse que nunca será
# inferior a 5 ou superior a 25. O programa deverá indicar ao
# utilizador se o vetor é constituído (ou não) por valores pares e
# ímpares alternados. Exemplo: O vetor [1, 2, 5, 6, 3, 2] verifica
# esta condição.


# Variables
size = 0;
arrayOfNumbers = [];

# Variables received by input
size = int(input('Introduza o tamanho do array: '));
while size < 5 or size > 25:
    size = int(input('Introduza de novo o tamanho do array: '));


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));



    return arrayOfNumbers;


def verficArray(arrayOfNumbers):
    flag = False;
    firstValue = arrayOfNumbers[0];

    for i in range(1, len(arrayOfNumbers)):
        if firstValue % 2 != 0 and arrayOfNumbers[i] % 2 == 0:
            firstValue = arrayOfNumbers[i];
            flag = True;
        elif firstValue % 2 == 0 and arrayOfNumbers[i] % 2 != 0:
            firstValue = arrayOfNumbers[i];
            flag = True;
        else:
            flag = False;
        if not flag:
            break;

    return flag;


# Print information
arrayOfNumbers = fillArray();

print(arrayOfNumbers);

flag = verficArray(arrayOfNumbers);
if flag:
    print('A ordem de numeros inseridos é a correcta!');
else:
    print('A ordem de numeros inseridos não é a correcta!');
