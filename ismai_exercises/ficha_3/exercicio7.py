# 7) Escreva um programa que leia 10 números inteiros introduzidos
# pelo utilizador e indique o máximo, a média, o mínimo e a soma
# dos valores.

x = 0
vMax = -999
vMin = 999
soma = 0
media = 0

for x in range(0, 10):
    num = int(input('Introduza um valor: '))
    if num > vMax:
        vMax = num
    if num < vMin:
        vMin = num
    soma += num

print('O valor minimo é: ', vMin)
print('O valor maximo é: ', vMax)
print('A média dos valores é: ', (soma/10))