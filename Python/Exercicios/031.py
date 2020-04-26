dist = float(input('Qual a distancia da sua viagem: '))
if dist < 200:
    print('O preço da sua viagem é R${:.2f}'.format(dist * 0.50))
else:
    print('O preço da sua viagem é R${:.2f}'.format(dist * 0.45))
