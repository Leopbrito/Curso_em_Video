def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Aprovado'
        elif 5 <= r['media'] < 7:
            r['situação'] = 'Recuperação'
        else:
            r['situação'] = 'Reprovado'  
    return r



resp = notas(2, 2.5, 4, sit=True)
resp2 = notas(2, 5, 9, 4, sit=True)
resp3 = notas(8, 9, 7, 4, 10, sit=True)
print(resp)
print(resp2)
print(resp3)