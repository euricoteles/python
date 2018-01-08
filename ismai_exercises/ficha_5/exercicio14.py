# 14) Escreva um programa que verifique se todos os elementos de um
# determinado vetor existem noutro vetor.

# Variables
size = 0;
arrayOfNumbersFirst = [];
arrayOfNumbersSecond = [];

# Variables received by input
size = int(input('Introduza o tamanho do array: '));


# Algorithm
# Function
def fillFirstArray():
    arrayOfNumbersFirst = [0] * size;
    for i in range(0, len(arrayOfNumbersFirst)):
        arrayOfNumbersFirst[i] = int(input('Introduza um valor para o primeiro array: '));

    return arrayOfNumbersFirst;


def fillSecondArray():
    arrayOfNumbersSecond = [0] * size;
    for i in range(0, len(arrayOfNumbersSecond)):
        arrayOfNumbersSecond[i] = int(input('Introduza um valor para o segundo array: '));

    return arrayOfNumbersSecond;


def verficArray(arrayOfNumbersFirst, arrayOfNumbersSecond):
    flag = False;

    for i in range(0, len(arrayOfNumbersFirst)):
        for j in range(0, len(arrayOfNumbersSecond)):
            if arrayOfNumbersFirst[i] == arrayOfNumbersSecond[j]:
                flag = True;
                if i <= len(arrayOfNumbersFirst):
                   break;
            else:
                flag = False;

    return flag;


# Print information
arrayOfNumbersFirst = fillFirstArray();
arrayOfNumbersSecond = fillSecondArray();

print(arrayOfNumbersFirst);
print(arrayOfNumbersSecond);

flag = verficArray(arrayOfNumbersFirst, arrayOfNumbersSecond);
if flag:
    print('Existem todos os numeros no segundo array!');
else:
    print('Não existem todos os numeros no segundo array!');
