grupo = []
aluno = []
iden = 0 
while True:
    opc = ' '
    nome = input('Nome: ').capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno.append(iden)
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    grupo.append(aluno[:])
    aluno.clear()
    iden += 1
    while opc not in 'SN':
        opc = input('Deseja continuar: [S/N] ').upper()
    if opc == 'N':
        break
print(f'{"N°.":<3} | {"NOME":<15} | {"Média":<7}')
print('-'*30)
for aluno in grupo:
    print(f'{aluno[0]:<3} | {aluno[1]:<15} | {(aluno[2]+aluno[3])/2:<7.2f}')

while True:
    a = int(input('Mostrar a nota de qual aluno [999 para sair]: '))
    print(f'As notas de {grupo[a][1]} são {grupo[a][2]} e {grupo[a][3]}')
    if a == '999':
        break
print('FIM')