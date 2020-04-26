def leiaInt(n):
    if n.isnumeric():
        if n % 1 != 0.0000:
            print('Erro, digite um número inteiro')
            n = input('Digite um número: ')
        else:
            print(f'Voce digitou o número {n}')
    else:
        print('Erro, digite um número inteiro')
        n = input('Digite um número: ')


n = input('Digite um número: ')
leiaInt(n)
