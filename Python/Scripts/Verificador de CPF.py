CPF = input('Digite seu CPF(sem ponto e sem hifen): ')

if len(CPF) != 11 or CPF == '11111111111' or CPF == '22222222222' or CPF == '33333333333' or CPF == '44444444444' or CPF == '55555555555' or CPF == '66666666666' or CPF == '77777777777' or CPF == '88888888888' or CPF == '99999999999' or CPF == '00000000000':
  print('CPF Invalido')
else:
  '''Calculo 1° digito verificador'''
  soma = 0
  for x in range(0,9):
    soma = soma + (float(CPF[x]) * (10-x))
  dig1 = 11 - (soma%11)
  if dig1 >= 10:
    dig1 = 0

  '''Calculo 2° digito verificador'''
  soma = 0
  for x in range(0,10):
    soma = soma + (float(CPF[x]) * (11-x))
  dig2 = 11 - (soma%11)
  if dig2 >= 10:
    dig2 = 0

  '''Script verificador '''  
  if dig1 == float(CPF[9])  and dig2 == float(CPF[10]):
    print('CPF valido') 
  else:
    print('CPF invalido')