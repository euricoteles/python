# 1) Escreva um programa para imprimir os números inteiros entre 1
# e 10 na mesma linha, primeiro em ordem crescente e depois em
# ordem decrescente.

# Variables received by input

# print information
for i in range(1, 10):
	print(' ', i, sep=' ', end='', flush=True)
for i in range(10, 0, -1):
	print(' ', i, sep=' ', end='', flush=True)