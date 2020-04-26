from time import sleep

opc = 0
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while opc != 5:
    print('=-='*10)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')
    print('=-='*10)
    sleep(0.5)
    opc = int(input('>>>>> QUAL SUA OPÇÂO: '))
    print('\033[33mProcessando...\033[m')
    sleep(1.5)
    if opc == 1:
        soma = n1 + n2
        print(f'\033[32mA soma entre {n1} + {n2} é {soma}\033[m')
    elif opc == 2:
        mult = n1 * n2
        print(f'\033[32mA multiplicação entre {n1} * {n2} é {mult}\033[m')
    elif opc == 3:
        if n1 > n2:
            print(f'\033[32mO primeiro valor({n1}) é maior que o segundo valor({n2})\033[m')
        else:
            print(f'\033[32mO segundo valor({n2}) é maior que o primeiro valor({n1})\033[m')
    elif opc == 4:
        print('---> Digite novos valores <---')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opc == 5:
        print('O Programa foi finalizado!!!')
        break
    else:
        print('OPÇÂO invalida!!!')
        opc = int(input('>>>>> QUAL SUA OPÇÂO: '))