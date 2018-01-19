# Variables
size = 5;
arrayOfNumbers = [];
newArray = [];


# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


def zipArray():
    for i in range(0, len(arrayOfNumbers)):
        for j in range(i+1, len(arrayOfNumbers)):
            if arrayOfNumbers[i] == 0:
                temp = arrayOfNumbers[i];
                arrayOfNumbers[i] = arrayOfNumbers[j]
                arrayOfNumbers[j] = temp



arrayOfNumbers = fillArray();
zipArray()
print(arrayOfNumbers);
