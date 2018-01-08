# 10) Escreva um programa para ler as notas de n alunos (sendo n
# introduzido pelo utilizador). As notas deverão estar entre 1 e 5.
# O programa deverá contar quantos alunos tiveram cada uma das notas
# possíveis.

# Variables
notaUm = 0
notaDois = 0
notaTres = 0
notaQuatro = 0
notaCinco = 0
notas = 0
notasValidas = 0
notasInvalidas = 0

# Variables received by input
n = int(input('Introduz o numero de alunos: '))

# Algorithm
for i in range(1, n+1):
    notas = int(input('Introduza uma nota de (1 a 5): '))
    if notas == 1:
        notaUm += 1
        notasValidas += 1
    elif notas == 2:
        notaDois += 1
        notasValidas += 1
    elif notas == 3:
        notaTres += 1
        notasValidas += 1
    elif notas == 4:
        notaQuatro += 1
        notasValidas += 1
    elif notas == 5:
        notaCinco += 1
        notasValidas += 1
    else:
        print('Nota Invalida!')
        notasInvalidas += 1

# Print information
print('No total de {} alunos houve:'.format(n))
if notaUm > 0:
    print('Houve {} alunos que teve a nota 1.'.format(notaUm))
if notaDois > 0:
    print('Houve {} alunos que teve a nota 2.'.format(notaDois))
if notaTres > 0:
    print('Houve {} alunos que teve a nota 3.'.format(notaTres))
if notaQuatro > 0:
    print('Houve {} alunos que teve a nota 4.'.format(notaQuatro))
if notaCinco > 0:
    print('Houve {} alunos que teve a nota 5.'.format(notaCinco))
if notasInvalidas > 0:
    print('Houve {} notas lidas que não eram válidas!'.format(notasInvalidas))