# Variables
sizeVetor1 = 0;
arrayOfNumbers = [];
newArray = [];

sizeVetor1 = int(input('Introduza o tamanho do vetor 1: '))


# Algorithm
# Function
def fillArrayUm():
    arrayOfNumbers = [0] * sizeVetor1;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def deleteZero():
    newArray = [];
    for i in range(0, len(arrayOfNumbers)):
        if arrayOfNumbers[i] != 0 and arrayOfNumbers[i] % 2 != 0:
            newArray.append(arrayOfNumbers[i]);
        elif arrayOfNumbers[i] != 0 and arrayOfNumbers[i] % 2 == 0:
            newArray.append(arrayOfNumbers[i]);

    for i in range(0, len(newArray)):
        for j in range(i + 1, len(newArray)):
            if newArray[i] %2 == 0:
                temp = newArray[i];
                newArray[i] = newArray[j]
                newArray[j] = temp

    return newArray;




arrayOfNumbers = fillArrayUm();
print(arrayOfNumbers)
newArray = deleteZero();

arrayOfNumbers = newArray;
print(arrayOfNumbers)
