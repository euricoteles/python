# 1) Escreva um programa que preencha um vetor de 100 posições com os
# primeiros 100 números pares.

# Variables
numbersPairsArray = [];


# Algorithm
# Functions
def fillArrayWithPairs():
    for i in range(0, 100, 2):
        numbersPairsArray.append(i);


# Call the Function
fillArrayWithPairs();

# Print information
print(numbersPairsArray);
