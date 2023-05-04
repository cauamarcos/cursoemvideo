peso = float (input ('Digite seu peso: '))
altura = float (input ('Digite sua altura: '))
imc = peso / altura ** 2
print (f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print ('\033[33mVocê está abaixo do peso!\033[m')
elif 18.5 <= imc < 25:
    print ('\033[32mVocê está na faixa de peso ideal!\033[m')
elif 25 <= imc < 30:
    print ('\033[33mVocê está com sobrepeso!\033[m')
elif 30 <= imc < 40:
    print ('\033[31mVocê está em situação de obesidade!\033[m')
else:
    print ('\033[36;41mVocê está em situação de obesidade mórbida!\033[m')
