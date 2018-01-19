# 4) Escreva um programa e respetivas funçoes, que peça as idades de 20 alunos de uma turma.
# O programa deve guardar estes valores num vetor e no final indicar as primeiras quatro notas
# mais altas, a media, e a mediana da turma. No conjunto dos dados [1,3,3,6,7,8,9], por exemplo,
# a mediana é 6. Se houver um número par de observações, não há um unico valor do meio. Então a
# mediana é definida como a média dos dois valores do meio.

# Variables
size = 6;
arrayOfNumbers = [];
arrayIdades = [];

# Algorithm
# Function
def fillArray():
    arrayOfNumbers = [0] * size;
    for i in range(0, len(arrayOfNumbers)):
        arrayOfNumbers[i] = int(input('Introduza um valor:'));

    return arrayOfNumbers;

def mediaArray():
    media = 0;

    for i in range(0, len(arrayOfNumbers)):
        media += arrayOfNumbers[i];

    media /= len(arrayOfNumbers);

    return media;

def idadesAlta():
    arrayFiveIdades = [0] * 5;
    for j in range(0, len(arrayOfNumbers)):
        for i in range(4, -1, -1):
            if arrayOfNumbers[j] > arrayFiveIdades[i]:
                if i == 4:
                    arrayFiveIdades[i] = arrayOfNumbers[i];
                else:
                    temp = arrayFiveIdades[i];
                    arrayFiveIdades[i] = arrayOfNumbers[j];
                    arrayFiveIdades[i+1] = temp;

    return arrayFiveIdades;

# Print information
arrayOfNumbers = fillArray();
print(arrayOfNumbers);
media = mediaArray();
print(media);
arrayIdades = idadesAlta();
print(arrayIdades);