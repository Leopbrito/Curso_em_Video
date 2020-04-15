expr = input('Digite a expressão: ')
vrf = []
for simb in expr:
    if simb == '(':
        vrf.append('(')
    elif simb == ')':
        if len(vrf) > 0:
            vrf.pop()
        else:
            vrf.append(')')
            break
if len(vrf) == 0:
    print('A expressão está correta')
else:
    print('A expressão está incorreta')