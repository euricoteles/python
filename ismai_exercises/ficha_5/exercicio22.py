# 22) Desenvolva um programa para simular o embaralhar de um baralho
# de cartas. Use um vetor e embaralhe as cartas fazendo trocas entre
# os elementos. Depois dê 4 mãos de 13 cartas.



# Variables
# Import
import random

# Variables
arrayOfCards = ["AsP", "2P", "3P", "4P", "5P", "6P", "7P", "8P", "9P", "10P", "JP",
                "QP", "KP", "AsC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC",
                "QC", "KC", "AsE", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "JE",
                "QE", "KE", "AsO", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O", "JO",
                "QO", "KO"];
sizeOfMao = 13;
arrayMaoOne = [0] * sizeOfMao;
arrayMaoTwo = [0] * sizeOfMao;
arrayMaoThree = [0] * sizeOfMao;
arrayMaoFour = [0] * sizeOfMao;


# Algorithm
# Function
def shufflingArray():
    arrayResult = [0] * sizeOfMao;
    for i in range(0, len(arrayResult)):
        index = random.randint(0, 51);
        while arrayOfCards[index] == 0:
            index = random.randint(0, 51);

        if arrayOfCards[index] != 0:
            arrayResult[i] = arrayOfCards[index];
            arrayOfCards[index] = 0;

    return arrayResult;


# Fill HandsGame
arrayMaoOne = shufflingArray();
arrayMaoTwo = shufflingArray();
arrayMaoThree = shufflingArray();
arrayMaoFour = shufflingArray();

# Print Hands
print('Mão do Jogador 1:', arrayMaoOne);
print('Mão do Jogador 2:', arrayMaoTwo);
print('Mão do Jogador 3:', arrayMaoThree);
print('Mão do jogador 4:', arrayMaoFour);
