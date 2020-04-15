from datetime import datetime

trabalhador = dict()

trabalhador['nome'] = input('Nome: ')
trabalhador['anonasc'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.today().year - trabalhador['anonasc']
trabalhador['CTPS'] = input('Carteira de trabalho [0 não possui]: ')
if trabalhador['CTPS'] != '0':
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: '))
    trabalhador['aposcentadoria'] = trabalhador['contratação'] - trabalhador['anonasc'] + 35
print('-'*30)
for k, v in trabalhador.items():
    if v == trabalhador['anonasc']:
        continue
    else:
        print(f'{k} tem o valor {v}')