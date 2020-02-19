dia = float(input('Quantos dia(s) alugado(s): '))
km = float(input('Quantos km(s) rodado(s): '))
preco = (dia * 60) + (km * 0.15)
print('O total a pagar é {}'.format(preco))