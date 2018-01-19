# Variables
sizeVetor1 = 0;
sizeVetor2 = 0;
arrayOfNumbers1 = [];
arrayOfNumbers2 = [];

sizeVetor1 = int(input('Introduza o tamanho do vetor 1: '))
sizeVetor2 = int(input('Introduza o tamanho do vetor 2:' ))


# Algorithm
# Function
def fillArrayUm():
    arrayOfNumbers1 = [0] * sizeVetor1;
    for i in range(0, len(arrayOfNumbers1)):
        arrayOfNumbers1[i] = int(input('Introduza um valor para o primeiro array:'));

    return arrayOfNumbers1;

def fillArrayDois():
    arrayOfNumbers2 = [0] * sizeVetor2;
    for i in range(0, len(arrayOfNumbers2)):
        arrayOfNumbers2[i] = int(input('Introduza um valor para o segundo array:'));

    return arrayOfNumbers2;

def isPrime(i):
    prime = True;
    for j in range(2, i):
        if i % j == 0:
            prime = False;

        # Print information
        if prime:
            return True;
        else:
            return False;

def searchNumbersNotPrime():
    newArray = [];
    for i in range(0, len(arrayOfNumbers1)):
        if not isPrime(arrayOfNumbers1[i]):
            newArray.append(arrayOfNumbers1[i]);
            arrayOfNumbers1[i] = 0;

    for j in range(0, len(arrayOfNumbers2)):
        if not isPrime(arrayOfNumbers2[j]):
            newArray.append(arrayOfNumbers2[j]);
            arrayOfNumbers2[j] = 0;


    return newArray

arrayOfNumbers1 = fillArrayUm();
arrayOfNumbers2 = fillArrayDois();
newArray = searchNumbersNotPrime();

print(newArray);