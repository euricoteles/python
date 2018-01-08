# 20) Crie um programa que simule 100 lançamentos de 2 dados, guarde
# os resultados em vetores e produza uma estatística.

# Information
# Sum = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 }
# Probabilidade = { 2 = 1/36, 3 = 2/36, 4 = 3/36, 5 = 4/36, 6 = 5/36, 7 = 6/36, 8 = 5/36, 9 = 4/36, 10 = 3/36, 11 = 2/36
# 12 = 1/36 }
# Product = { 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36 }

# Import
import random

# Variables
arrayOfNumbersDadoOne = [0];
arrayOfNumbersDadoTwo = [0];
numLanc = 0;

# Variables received by input
numLanc = int(input('Introduza o numero de lancamentos: '));

# Algorithm
# Function
def fillArrayDadoOne():
    arrayOfNumbersDadoOne = [0] * numLanc;
    for i in range(0, len(arrayOfNumbersDadoOne)):
        arrayOfNumbersDadoOne[i] = random.randint(1,6);

    return arrayOfNumbersDadoOne;


def fillArrayDadoTwo():
    arrayOfNumbersDadoTwo = [0] * numLanc;
    for i in range(0, len(arrayOfNumbersDadoTwo)):
        arrayOfNumbersDadoTwo[i] = random.randint(1,6);

    return arrayOfNumbersDadoTwo;


arrayOfNumbersDadoOne = fillArrayDadoOne();
arrayOfNumbersDadoTwo = fillArrayDadoTwo();
print(arrayOfNumbersDadoOne);
print(arrayOfNumbersDadoTwo);