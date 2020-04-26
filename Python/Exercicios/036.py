casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salario: '))
tempo = int(input('Quantos anos de financiamento: '))
prest = casa/(tempo*12)
print('O valor da prestação é R${:.2f}.'.format(prest))
if prest > salario*0.30:
    print('A prestação do financiamento compromete mais que 30% do seu salario, não podendo ser concedido o financiamento')
else:
    print('A prestação do financiamento é menor do que 30% do seu salario, podendo ser concedido o financiamento')