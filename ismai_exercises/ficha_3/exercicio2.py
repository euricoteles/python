# 2) Escreva um programa para imprimir todos os números inteiros
# entre dois valores introduzidos pelo utilizador. O programa deverá
# verificar qual dos dois valores é o maior.


limiteUm = int(input('Introduza um valor: '))
limiteDois = int(input('Introduza um valor: '))

if limiteUm > limiteDois:
    maior = limiteUm
    menor = limiteDois
else:
    maior = limiteDois
    menor = limiteUm

for i in range(menor, maior+1):
    print(i, ' ', sep=' ', end='', flush=True)

print('\nO valor maior introduzido é o {}!'.format(maior))