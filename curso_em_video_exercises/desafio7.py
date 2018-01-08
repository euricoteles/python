#  Crie um script leia duas notas de um aluno, calcule e mostre a sua média.

# variables received by input
nota1 = int(input('Introduza a primeira nota:'))
nota2 = int(input('Introduza a segunda nota: '))

media = (nota1+nota2) / 2

# print information
print('As nota do aluno foram nota 1: {} nota 2: {} a sua média é : {}'.format(nota1, nota2, media))