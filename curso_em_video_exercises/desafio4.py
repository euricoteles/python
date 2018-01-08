# Crie um script que leia algo do teclado e mostre o seu tipo primitivo e
# todas as informações possiveis sobre o que foi lido.

# variables received by input
variable = input('Introduza qualquer coisa: ')

# print information
print('Which type is:', type(variable))
print('Is alphanumeric:', variable.isalnum())
print('Is a alphabetic:', variable.isalpha())
print('Is a decimal:', variable.isdecimal())
print('Is a digit:', variable.isdigit())
print('Is a numeric:', variable.isnumeric())