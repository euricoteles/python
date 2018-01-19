#  3) Crie uma função que receba três inteiros como argumentos (ano, mês, dia)
# e verifique se se trata de uma data válida. O ano deverá estar entre 1900 e
# o presente ano. Deverá retornar um valor booleano!

# Variables
ano = 0;
mes = 0;
dia = 0;

# Variables received by input
ano = int(input('Introduza um ano: '));
mes = int(input('Introduza um mes: '));
dia = int(input('Introduza um dia: '));


# Algorithm
# Function
def validData(ano, mes, dia):
    flag = False;

    if ano >= 1900 and ano <= 2018:
        if mes < 1 and mes > 12:
            if dia < 1 and dia > 31:
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    flag = True;
                elif mes == 2 and dia > 1 or dia <= 28:
                    flag = True;
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia < 31:
                    flag = True;
            else:
                flag = False;
        else:
            flag = False;
    else:
        flag = False;
    return flag;


dataValid = validData(ano, mes, dia);

if dataValid:
    print('Data válida!');
else:
    print('Data inválida!');