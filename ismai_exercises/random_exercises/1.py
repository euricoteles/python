# Variables
size = 16;
arrayOfNumbers = [];
newArray = [];


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def switchArray():
    newArray = [0] * 16;
    index = 0;
    for i in range(0, len(arrayOfNumbers)):
        if i >= 8:
            newArray[index] = arrayOfNumbers[i];
            index += 1

    for i in range(0, 8):
        newArray[index] = arrayOfNumbers[i];

        index += 1

    return newArray;


arrayOfNumbers = fillArray();
print(arrayOfNumbers);

array = switchArray();
print(array);
