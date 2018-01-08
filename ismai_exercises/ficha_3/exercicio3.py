# 3) Escreva um programa que apresente a tabuada dum número inteiro
# entre 1 e 9 dado pelo utilizador. Se o número estiver fora dessa
# gama, o programa deverá dar uma mensagem.
nTabu = int(input('Introduza um valor para calcular a sua tabuada: '))


if nTabu < 0 or nTabu > 9:
    print('Valor tem que estar entre 1 e 10!')
    while nTabu < 0 or nTabu > 9 :
        print('Valor tem que estar entre 1 e 10!')
        nTabu = int(input('Introduza um valor: '))
n = 1

if nTabu > 0 or nTabu <= 9:
    for n in range(1, 10):
        print(nTabu, "*", (n), "=", (nTabu * n))
        n += 1