# 26) Escreva um programa que reduza uma fração.

# Variables
frac1 = 0
frac2 = 0
numeroUm = 0
numeroDois = 0

# Variables received by input
frac1 = int(input('Introduza o valor da primeira fracao: '))
frac2 = int(input('Introduza o valor da segunda fracao: '))

numeroUm = frac1
numeroDois = frac2

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