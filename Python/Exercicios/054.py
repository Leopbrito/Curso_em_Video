from datetime import date
Datual = date.today().year
maior = menor = 0
for x in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {x}° pessoa ?'))
    if Datual - nasc >17:
        maior += 1
    else:
        menor += 1
print(f'''Maiores de idade: {maior}
Menores de idade: {menor}''')