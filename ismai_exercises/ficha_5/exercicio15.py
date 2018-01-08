# 15) Escreva um programa que inverta a ordem dos elementos de um
# vetor de inteiros. Compare os resultados com a função reverse.


# Variables
size = 0;
arrayOfNumbers = [];

# Variables received by input
size = int(input('Introduza o tamanho do array: '));

# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def reverseArray(arrayOfNumbers):
    # Sort Array
    for i in range(0, len(arrayOfNumbers)):
        for j in range(0, len(arrayOfNumbers)):
            if arrayOfNumbers[i] > arrayOfNumbers[j]:
                temp = arrayOfNumbers[i];
                arrayOfNumbers[i] = arrayOfNumbers[j];
                arrayOfNumbers[j] = temp;

# Print information
arrayOfNumbers = fillArray();

print('Normal Order:', arrayOfNumbers);

reverseArray(arrayOfNumbers);

print('Reverse by me:', arrayOfNumbers);

print('Reverse by function Reverse:');
arrayOfNumbers.reverse();
print(arrayOfNumbers);
