# 11) Crie um programa que leia um vetor de 10 inteiros. Os valores
# deverão estar no intervalo [0,100]. O programa não deverá aceitar
# valores fora deste intervalo. O programa deverá indicar a soma dos
# inteiros múltiplos de 5 existentes no vetor.


# Variables
numero = 0;
arrayofIntegers = [];
total = 0;

# Algorithm
for i in range(1, 10):
    numero = int(input('Introduza um numero: '));
    if numero < 0 or numero > 100:
        while numero < 0 or numero > 100:
            print('O numero introduzido não é valido!');
            numero = int(input('Introduza outro numero: '));

    arrayofIntegers.append(numero);
    if numero % 5 == 0:
        total += numero;

# Print information
print('Foram introduzidos alguns numeros múltiplos de 5 o seu total é: {}!'.format(total));