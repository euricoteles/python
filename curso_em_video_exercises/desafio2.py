# Crie um script que leia o dia, o mes, o ano de nascimento de uma pessoa
# e mostre uma mensagem com a data formatada (Nasceu no dia dd do mm no aaaa).

# Variables received by input
dia = input('Qual o seu dia de nascimento? ')
mes = input('Qual o seu mes de nascimento? ')
ano = input('Qual o seu ano de nascimento? ')

# print information
print('Nasceu no dia {} do mes {} do ano {}'.format(dia, mes, ano))