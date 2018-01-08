# 10) Escreva um programa que preencha um vetor de 20 posições com
# os primeiros 20 números primos.


# Variables
arrayOfPrimeNumbers = [];


# Functions
# Algorithm
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


def fillArray():
    contador = 0;
    for i in range(2, 50):
        if isPrime(i):
            arrayOfPrimeNumbers.append(i);
            contador += 1;

        if contador == 20:
            break;


# Call function
fillArray();
# Print information
print(arrayOfPrimeNumbers);



