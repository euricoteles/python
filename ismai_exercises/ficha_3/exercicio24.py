# 24) Crie um programa para escrever a série de Fibonacci até a um
# limite pedido pelo utilizador. (1, 2, 3, 5, 8, 13, 21...)

# Variables
numeroStop = 0
primeiroNumero = 0
segundoNumero = 1
proximoNumero = 0

# Algorithm

numeroStop = int(input('Introduza quantos numeros da impressão da série de Fibonacci quer ver: '))

for i in range(1, numeroStop+1):
    print(primeiroNumero, ' ')

    proximoNumero = primeiroNumero + segundoNumero
    primeiroNumero = segundoNumero
    segundoNumero = proximoNumero
