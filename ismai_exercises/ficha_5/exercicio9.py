# 9) Crie um programa que leia 10 números float, coloque-os num vetor
# e calcule a sua média.


# Variables received by input
numero = 0;
media = 0;
arrayOfNumbers = [];


# Algorithm
# Functions
def fillArray():
    media = 0;

    for i in range(0, 10):
        numero = float(input('Introduza um valor: '));
        media += numero;
        arrayOfNumbers.append(numero);

    return media/10;

# Call function
media = fillArray();

# Print information
print('A media é:', media);