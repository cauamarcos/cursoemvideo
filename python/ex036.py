preco = float (input ('Qual o preço da casa que você pretende comprar? '))
salario = float (input ('Qual o valor do seu salário? '))
tempo = float (input ('Em quantos ano você pretende pagar a casa? '))
if preco / (tempo * 12) > salario * 0.3:
    print ('Você não deve fazer isso!')
else:
    print (f'O valor da prestação mensal será de R${preco / (tempo * 12) :.2f}')
