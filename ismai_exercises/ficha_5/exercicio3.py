# 3) Escreva um programa em que 20 valores inteiros entre 1 e 10 são
# introduzidos pelo utilizador num vetor. Depois, o utilizador deverá
# indicar um valor e o programa deverá indicar em que posição ou
# posições, este valor existe no vetor. Se o valor não existir no
# vetor o programa deverá dar a respetiva mensagem.

# Variables
number = 0;
valueToSearch = 0;
arrayOfTwentyPositions = [];
arrayOfPositions = [];
flag = False;

# Algorithm
# Functions

def fillArray():
    for i in range(0, 20):
        number = int(input('Introduza um valor: '));
        if number > 0 and number <= 10:
            arrayOfTwentyPositions.append(number);
        else:
            while True:
                number = int(input('Introduza um novo valor: '));
                arrayOfTwentyPositions.append(number);
                if number > 0 and number <= 10:
                    break;


def searchValueInArray():
    valueToSearch = int(input('Introduza o valor a procurar: '));

    for i in range(len(arrayOfTwentyPositions)):
        if arrayOfTwentyPositions[i] == valueToSearch:
            flag = True;
            arrayOfPositions.append(i);


# Call functions
print(arrayOfTwentyPositions);
fillArray();
searchValueInArray();
print(arrayOfTwentyPositions);

# Print Information
if flag == True:
    for i in range(len(arrayOfPositions)):
        print('O numero a procurar encontra-se na posicao:', i)
else:
    print('O valor a procurar nao se encontra guardado!')
