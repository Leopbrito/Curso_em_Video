sal = float(input('Digite seu salario: R$'))
if sal >= 1250:
    print('O seu salario com 10% de aumento fica R${:.2f}'.format(sal*1.10))
else:
    print('O seu salario com 15% de aumento fica R${:.2f}'.format(sal*1.15))