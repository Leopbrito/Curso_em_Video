soma = 0
cont = 0
for x in range(1,7):
    n = float(input('Digite o {}° número: '.format(x)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} valor(es) par(es) é {:.0f}'.format(cont,soma))
