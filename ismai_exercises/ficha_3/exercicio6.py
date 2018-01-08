# 6) Crie um programa para escrever a série de quadrados entre 1 e
# um valor inteiro inferior a 100 introduzido pelo utilizador. (1,
# 4, 9, 25...)

numero = int(input('Introduza um numero: '))

if numero < 1 or numero > 100:
    print('O numero tem que estar entre 1 e 100')
    while numero < 1 or numero > 100:
        numero = int(input('Introduza um numero: '))

for n in range(1, numero):
    if n*n < numero:
        print('Quadrado:', (n*n))