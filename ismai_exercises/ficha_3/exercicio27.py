# 27) Aproveite o programa anterior para escrever um programa que
# realize a soma, subtração, multiplicação e divisão de frações e
# apresente o resultado na forma reduzida.

# Variables
frac1 = 0
frac2 = 0
frac3 = 0
frac4 = 0
numeroUm = 0
numeroDois = 0
opcao = 0

# Variables received by input
frac1 = int(input('Introduza o valor da primeira fracao: '))
frac2 = int(input('Introduza o valor da segunda fracao: '))
frac3 = int(input('Introduza o valor da terceira fracao: '))
frac4 = int(input('Introduza o valor da quarta fracao: '))

print('Qual a operação que deseja fazer:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    numeroUm = frac1 + frac3
    if frac2 == frac4:
        numeroDois = frac2
    else:
        numeroDois = frac2 * frac4
elif opcao == 2:
    numeroUm = frac1 - frac3
    if frac2 == frac4:
        numeroDois = frac2
    else:
        numeroDois = frac2 * frac4
elif opcao == 3:
    numeroUm = frac1 * frac3
    numeroDois = frac2 * frac4
else:
    numeroUm = frac1 * frac4
    numeroDois = frac2 * frac3

# Algorithm
# Calculate GCD = Greatest common divisor
gcd = numeroUm % numeroDois

while gcd > 0:
    numeroUm = numeroDois
    numeroDois = gcd
    gcd = numeroUm % numeroDois

gcd = numeroDois

frac1 /= gcd
frac2 /= gcd

print('A fracao reduzida é: {} / {}'.format(frac1, frac2))
