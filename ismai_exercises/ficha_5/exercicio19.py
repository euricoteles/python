# 19)  Crie um programa para determinar o maior valor entre as
# posições de dois vetores e colocar o resultado num 3 vetor.

# Variables
arrayOfNumbersFirst = [];
arrayOfNumbersSecond = [];
resultArray = [];
sizeFirstArray = 0;
sizeSecondArray = 0;

# Variables received by input
sizeFirstArray = int(input('Introduza o tamanho do primeiro array: '));
sizeSecondArray = int(input('Introduza o tamanho do segundo array: '));

# Algorithm
# Function
def fillArray():
    arrayOfNumbersFirst = [0] * sizeFirstArray;
    for i in range(0, len(arrayOfNumbersFirst)):
        arrayOfNumbersFirst[i] = int(input('Introduza um valor para o primeiro array: '));

    return arrayOfNumbersFirst;


def fillSecondArray():
    arrayOfNumbersSecond = [0] * sizeSecondArray;
    for i in range(0, len(arrayOfNumbersSecond)):
        arrayOfNumbersSecond[i] = int(input('Introduza um valor para o segundo array: '));

    return arrayOfNumbersSecond;


def findMaximumInArrays(arrayOfNumbersFirst, arrayOfNumbersSecond):
    maximo = 0;
    if len(arrayOfNumbersFirst) > len(arrayOfNumbersSecond):
        resultArray = [0];
        for i in range(0, len(arrayOfNumbersFirst)):
            if i < len(arrayOfNumbersSecond):
                if arrayOfNumbersFirst[i] > maximo:
                    maximo = arrayOfNumbersFirst[i];
                    resultArray[0] = maximo;
                if arrayOfNumbersSecond[i] > maximo:
                    maximo = arrayOfNumbersSecond[i];
                    resultArray[0] = maximo;
                if arrayOfNumbersFirst[i] == arrayOfNumbersSecond[i]:
                    resultArray[0] = arrayOfNumbersSecond[i];
    elif len(arrayOfNumbersFirst) < len(arrayOfNumbersSecond):
        resultArray = [0];
        for i in range(0, len(arrayOfNumbersSecond)):
            if i < len(arrayOfNumbersFirst):
                if arrayOfNumbersFirst[i] > maximo:
                    maximo = arrayOfNumbersFirst[i];
                    resultArray[0] = maximo;
                if arrayOfNumbersSecond[i] > maximo:
                    maximo = arrayOfNumbersSecond[i];
                    resultArray[0] = maximo;
                if arrayOfNumbersFirst[i] == arrayOfNumbersSecond[i]:
                    resultArray[0] = arrayOfNumbersSecond[i];
    else:
        resultArray = [0];
        for i in range(0, len(arrayOfNumbersFirst)):
            if arrayOfNumbersFirst[i] > maximo:
                maximo = arrayOfNumbersFirst[i];
                resultArray[0] = maximo;
            if arrayOfNumbersSecond[i] > maximo:
                maximo = arrayOfNumbersSecond[i];
                resultArray[0] = maximo;
            if arrayOfNumbersFirst[i] == arrayOfNumbersSecond[i]:
                resultArray[0] = arrayOfNumbersSecond[i];

    return resultArray;


# Print information
arrayOfNumbersFirst = fillArray();
arrayOfNumbersSecond = fillSecondArray();
resultArray = findMaximumInArrays(arrayOfNumbersFirst, arrayOfNumbersSecond);
print(resultArray);