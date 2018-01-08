# Crie um script que leia quanto dinheiro uma pessoa tem na carteira e converter em dolares.

# variables received by input
valor = int(input('Qual o valor para converter em dolares:'))

dolares = (1.18*valor)/1

# print information
print('O valor em dolares fica : {}'.format(dolares))