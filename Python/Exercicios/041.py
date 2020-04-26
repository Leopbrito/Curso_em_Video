from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÂO: MIRIM')
elif idade > 9 and idade <= 14:
    print('CLASSIFICAÇÂO: INFATIL')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÂO: JUNIOR')
elif idade > 19 and idade <= 25:
    print('CLASSIFICAÇÂO: SÊNIOR')
else:
    print('CLASSIFICAÇÂO: MASTER')