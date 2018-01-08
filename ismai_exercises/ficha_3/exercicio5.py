# 5) Escreva um programa que peça ao utilizador um nome e um número
# inteiro (entre 1 e 20). Deverá mostrar esse nome um número de
# vezes igual a esse valor inteiro.

nome = str(input('Introduza um nome: '))
numero = int(input('Introduza um numero: '))

if numero < 1 or numero > 20:
    print('O numero tem que estar entre 1 e 20: ')
    while numero < 1 or numero > 20:
        numero = int(input('Introduza um numero: '))

for n in range(0, numero):
    print('Nome:', nome, 'Numero:', n)