# 16) Crie um programa que conte o número de números primos num
# vetor de inteiros.


# Variables
size = int(input('Introduza o tamanho do array: '));

# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;


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


def countPrimesNumbers(arrayOfNumbers):
    contador = 0;

    for i in range(0, len(arrayOfNumbers)):
       if isPrime(arrayOfNumbers[i]):
                contador += 1;

    return contador;

# Print information
arrayOfNumbers = fillArray();

contador = countPrimesNumbers(arrayOfNumbers);

print('Existem {} numeros primos no array!'.format(contador));