from datetime import datetime 

def voto(anonasc):
    data = datetime.now().year
    idade = data - anonasc
    if 18 <= idade <= 70:
        situa = "Voto Obrigatorio"
    elif 16 <= idade < 18 or idade > 70:
        situa ='Voto Opcional'
    else:
        situa = 'Não vota'
    print(f'com {idade} anos: {situa} ')


anonasc = int(input('Em que ano voce nasceu? '))
voto(anonasc)
 