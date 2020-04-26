num = int(input('Digite um número: '))
if num%2 == 0:
    print('O número {} é \033[0;34mPAR\033[0;0m'.format(num))
elif num%2 == 1:
    print('O número {} é \033[0;34mIMPAR\033[0;0m'.format(num))