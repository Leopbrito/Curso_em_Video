alt = float(input('Digite sua altura(cm): '))
peso = float(input('Digite seu peso(kg): '))
IMC = peso/((alt/100)**2)
print('Seu IMC é {:.1f}'.format(IMC))
if IMC <= 18.5:
    print('Voce está abaixo do peso')
elif IMC > 18.5 and IMC <= 25:
    print('Voce está no peso ideal')
elif IMC > 25 and IMC <= 30:
    print('Voce está com sobrepeso')
elif IMC > 30 and IMC <= 40:
    print('Voce está obeso')
else:
    print('Voce está com Obesidade morbida')
