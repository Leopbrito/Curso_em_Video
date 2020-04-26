Aluno = dict()
Aluno['Nome'] = input('Nome: ')
Aluno['Média'] = float(input(f'Média de {Aluno["Nome"]}: '))
if Aluno['Média'] >= 7:
    Aluno['Situação'] = 'Aprovado'
elif 5 <= Aluno['Média'] < 7:
    Aluno['Situação'] = 'Recuperação'
else:
    Aluno['Situação'] = 'Reprovado'
for k, v in Aluno.items():
    print(f'A {k} é igual a {v}')
