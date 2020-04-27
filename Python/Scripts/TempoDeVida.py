import datetime
dataatual = datetime.date.today()
datanasc = (input('Digite sua data de nascimento(ex: DD/MM/AAAA): '))
datanasc = datetime.datetime.strptime(datanasc, '%d/%m/%Y').date()
data = (input('Digite a data à ser calculada: '))
data = datetime.datetime.strptime(data, '%d/%m/%Y').date()
if data == dataatual:
    data = datetime.date.today()
    diff = (data - datanasc).days
    anos = diff // 365.25
    mes = diff % 365.22 // 30.43
    dias = diff % 365.22 % 30.43 // 1
    print ('Você tem {} ano(s), {} mes(es) e {} dia(s).'.format(int(anos), int(mes), int(dias)))
else:
    if data < dataatual:
        diff = (data - datanasc).days
        anos = diff // 365.25
        mes = diff % 365.22 // 30.43
        dias = diff % 365.22 % 30.43 // 1
        print ('Você tinha {} ano(s), {} mes(es) e {} dia(s) em {}.'.format(int(anos), int(mes), int(dias), data))
    elif data > dataatual:
        diff = (data - datanasc).days
        anos = diff // 365.25
        mes = diff % 365.22 // 30.43
        dias = diff % 365.22 % 30.43 // 1
        print ('Você terá {} ano(s), {} mes(es) e {} dia(s) em {}.'.format(int(anos), int(mes), int(dias), data))
