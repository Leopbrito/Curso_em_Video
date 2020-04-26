media = 0
hnome = ''
hidade = 0
mmenor = 0
for pessoa in range(1,5):
    print(f'-------- {pessoa}° Pessoa --------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').upper()
    media += idade
    if sexo == 'M' and idade > hidade:
        hidade = idade
        hnome = nome
    if sexo == 'F' and idade < 20: 
        mmenor += 1
media = media/4
print(f'''A média de idade do grupo é {media}
O homem mais velho tem {hidade} anos e se chama {hnome}
Ao todo são {mmenor} mulheres com menos de 20 anos''')