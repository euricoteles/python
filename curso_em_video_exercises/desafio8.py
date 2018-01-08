# Crie um script que leia um valor em metros e o converta em centimetros e milimetros.

# variables received by input
valor = int(input('Introduza um valor:'))

centimetros = (100*valor)/1

milimetros = (1000*valor)/1

# print information
print('O valor em centimetros é: {} cm e em milimetros é {} mm'.format(centimetros, milimetros))