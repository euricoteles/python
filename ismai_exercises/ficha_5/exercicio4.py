# 4) Crie um programa que apresente a soma de todos os valores de um
# vetor de inteiros de 10 posições. Os valores devem ser introduzidos
# pelo utilizador.

# Variables
number = 0;
arrayOfTenPositions = [];
total = 0;

# Algorithm
# Functions

def fillArray():
    total = 0;
    for i in range(0, 10):
        number = int(input('Introduza um valor: '));
        arrayOfTenPositions.append(number);
        total += arrayOfTenPositions[i];

    return total;

# Call function
total = fillArray();

# Print Information
print('A soma de todos os valores guardados é:', total);