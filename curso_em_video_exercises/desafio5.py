# Crie um script que leia um numero Inteiro e mostre na tela o seu sucessor e o seu antecessor.

# variables received by input
number = int(input('Por favor introduza um numero: '))

# print information
print('O antecedor do numero lido é o {} e o seu sucessor é o {}!'.format(number-1, number+1))