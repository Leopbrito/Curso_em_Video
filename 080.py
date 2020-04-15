num = []

for x in range(0,5):
    n = int(input('Digite um valor: '))
    if len(num) == 0:
        num.append(n)
        print('O primeiro valor foi adicionado...')
    elif n >= num[-1]:
        num.append(n)
        print('O valor foi adicionado no final da lista...')
    else:
        for pos in range(0, len(num)):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'O valor foi adicionado na {pos}ª posição...')
                break
print('-=-'*25)
print(num)