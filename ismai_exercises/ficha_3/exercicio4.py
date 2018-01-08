# 4) Crie um programa que escreva os números inteiros entre 0 e 100
# em intervalos (incremento) dados pelo utilizador. O intervalo
# deverá ser um número entre 1 e 10. (Por exemplo, com intervalos
# de 4).

limiteUm = int(input('Introduza um valor: '))
limiteDois = int(input('Introduza um valor: '))
incremento = int(input('Introduza o incremento: '))

while incremento < 1 and incremento > 10:
    print('O incremnto tem que estar entre 1 e 10, introduza de novo:')
    incremento = int(input('Novo incremento:'))

for n in range(0, 100, incremento):
    print(n)