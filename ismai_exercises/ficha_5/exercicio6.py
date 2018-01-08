# 6) Crie um programa que leia um vetor de 10 valores inteiros do
# utilizador, não permitindo a introdução de valores repetidos.

# Variables
numero = 0;
arrayOfNumbers = [0] * 10;


# Algorithm
# Functions
print(arrayOfNumbers);
numero = int(input('Introduza um numero: '));
arrayOfNumbers[0] = numero;

for i in range(1, 10):
    numero = int(input('Introduza um numero: '))
    # Search in the array for the number
    for j in range(i):
        while arrayOfNumbers[j] == numero:
            print("Este numero ja existe!");
            numero = int(input('Introduza outro numero: '));


    arrayOfNumbers[i] = numero;

print(arrayOfNumbers);