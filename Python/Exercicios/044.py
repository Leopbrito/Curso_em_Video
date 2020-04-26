print('======== LOJA DO LEOPBRITO ========')
compra = float(input('Preço da compra: R$'))
print('''[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input("Qual a forma de pagamento: "))
if opção == 1:
    print('Sua compra de R${}, com 10% de desconto vai custar R${}'.format(compra, compra*0.90))
elif opção == 2:
    print('Sua compra de R${}, com 5% de desconto vai custar R${}'.format(compra, compra*0.95))
elif opção == 3:
    print('Sua compra de R${}, em 2x no cartão vai custar 2x de R${}'.format(compra, compra/2))
elif opção == 4:
    parcelas = int(input('Quantidade de parcelas: '))
    print('Sua compra de R${}, em {}x no cartão vai custar {}x de R${} com juros, totalizando R${}'.format(compra,parcelas,parcelas,(compra*1.20)/parcelas, compra*1.20 ))