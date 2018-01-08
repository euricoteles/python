# 8) Escreva um programa em que o utilizador vai introduzindo as
# idades dos alunos de uma determinada turma até ser introduzido o
# número -1. No fim deverá indicar o número de alunos e a média de
# idades. O programa deverá garantir que apenas são introduzidos
# números positivos (com a exceção do -1 final).

# Variables received by input
numAlunos = 0
media = 0
totalIdade = 0

# Algorithm
while True:
    idade = int(input('Introduza uma idade: '))
    if idade > 0:
        numAlunos += 1
        totalIdade += idade
    elif idade < -1:
        print('Idade tem que ser acima de 0!');
    if idade == -1:
        break

media = totalIdade / numAlunos

# print information
print('O numero de alunos lidos é {} e a média: {}'.format(numAlunos, media))