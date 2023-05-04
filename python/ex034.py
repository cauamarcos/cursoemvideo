valor = float (input ('Qual o valor do seu salário? '))
if valor > 1250:
    print (f'Você receberá um aumento de 10% e passará receber {valor * 1.1 :.2f}')
else:
    print (f'Você receberá um aumento de 15% e passará receber {valor * 1.15 :.2f}')
