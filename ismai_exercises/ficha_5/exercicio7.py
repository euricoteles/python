# 7) Crie um programa que leia um conjunto de valores inteiros do
# utilizador e os coloque num vetor. O programa deverá terminar a
# leitura quando for introduzido um número que já exista no vetor, ou
# seja, quando for introduzido um número repetido. No final deverá
# apresentar o vetor.


# Variables
numero = 0;
arrayOfNumbers = [0] * 10;
flag = False;

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
            print("Este numero ja existe!")
            flag = True;
            break;

    if flag:
        break;

    arrayOfNumbers[i] = numero;


print(arrayOfNumbers);