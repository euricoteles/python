# .8) Crie um programa que leia um vetor de n inteiros, sendo n um valor
# introduzido pelo utilizador, não havendo restrições. O programa deverá
# converter todos os valores negativos do vetor para 0, imprimir o vetor
# resultante e indicar quantos valores foram alterados.


# Variables received by input
numero = 0;
total = 0;
arrayOfNumbers = [];


# Algorithm
# Functions
def fillArray():
    total = int(input('Introduza o valor para o tamanho do array: '));


    for i in range(0, total):
        numero = int(input('Introduza um valor: '));
        arrayOfNumbers.append(numero);


def convertNumber():
    for i in range(len(arrayOfNumbers)):
        if arrayOfNumbers[i] < 0:
            arrayOfNumbers[i] = 0;


# print information
fillArray();
convertNumber();

print(arrayOfNumbers);