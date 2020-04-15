num = []
par = []
imp = []

while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    opc =' '
    while opc not in 'SN':
        opc = input('Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print(f'''A lista completa: {num}
A lista de Pares: {par}
A lista de Impares: {imp}
''')
