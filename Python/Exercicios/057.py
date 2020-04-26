s = input('Informe seu sexo[M/F]: ').upper()
while s != 'M' and s != 'F':
    s = input('Dado invalido!!!, Informe seu sexo[M/F]:').upper
print(f'Seu sexo({s}) foi cadastrado!')