compra = 0
barato = 0
prodbarato = ''
caro = 0

print('---'*10)
print('Lojão Leopbrito ')
print('---'*10)
while True:
    produto = input('Produto: ')
    preço = float(input('Preço: R$'))
    compra += preço
    if barato == 0:
        barato = preço
        prodbarato = produto
    if preço < barato:
        barato = preço
        prodbarato = produto
    if preço > 1000:
        caro += 1
    resp = ' '
    while resp not in "SN":
        resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break
print(f'''Total da compra: R${compra:.2f}
Produtos custando mais R$1000: {caro:.0f}
O produto mais barato foi {prodbarato} custando R${barato:.2f}
''')