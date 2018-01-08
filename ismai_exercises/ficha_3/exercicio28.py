# 28) Escreva um programa que, a partir do preço em euros e do
# dinheiro entregue, apresente o troco usando o menor número
# possível de moedas.

# Variables
valorPagar = 0
valorReceber = 0
troco = 0


# Variables received by input
while True:
    valorPagar = int(input('Valor a pagar: '))
    valorReceber = int(input('Valor a receber: '))

    if valorReceber >= valorPagar:
        break

# Algorithm
if valorReceber > valorPagar:
    troco = valorReceber - valorPagar
else:
    troco = valorPagar - valorReceber

# Print information
print('\n')
print('Troco:')
for moedas in (2, 1, 0.50, 0.20, 0.10, 0.05):
	print(f'Total de {troco // moedas} moedas de {moedas}€')
	troco %= moedas

