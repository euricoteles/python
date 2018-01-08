# 18) Crie um programa para somar 2 vetores de tamanhos diferentes
# e colocar o resultado num 3 vetor.

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


def sumArrays(arrayOfNumbersFirst, arrayOfNumbersSecond):
    if len(arrayOfNumbersFirst) > len(arrayOfNumbersSecond):
        resultArray = [0] * len(arrayOfNumbersFirst);
        for i in range(0, len(arrayOfNumbersFirst)):
            if i < len(arrayOfNumbersSecond):
                resultArray[i] = arrayOfNumbersFirst[i] + arrayOfNumbersSecond[i];
            else:
                resultArray[i] = arrayOfNumbersFirst[i];
    else:
        resultArray = [0] * len(arrayOfNumbersSecond);
        for i in range(0, len(arrayOfNumbersSecond)):
            if i < len(arrayOfNumbersFirst):
                resultArray[i] = arrayOfNumbersSecond[i] + arrayOfNumbersFirst[i];
            if i > len(arrayOfNumbersFirst):
                resultArray[i] = arrayOfNumbersSecond[i];

    return resultArray;


# Print information
arrayOfNumbersFirst = fillArray();
arrayOfNumbersSecond = fillSecondArray();
resultArray = sumArrays(arrayOfNumbersFirst, arrayOfNumbersSecond);

print(arrayOfNumbersFirst);
print(arrayOfNumbersSecond);
print(resultArray);
