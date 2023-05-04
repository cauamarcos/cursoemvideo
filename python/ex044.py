preco = float (input ('Digite o preço do produto: '))
e = int (input ('''Escolha a forma de pagamento:
[ 1 ] = à vista em dinheiro
[ 2 ] = à vista no cartão
[ 3 ] = 2x no cartão
[ 4 ] = 3x ou mais no cartão
Sua escolha: '''))
if e == 1:
    print (f'O valor a ser pago é R${0.9 * preco:.2f}')
elif e == 2:
    print (f'O valor a ser pago é R${0.95 * preco:.2f}')
elif e == 3:
    print (f'O valor a ser pago é R${preco:.2f}')
elif e == 4:
    print (f'O valor a ser pago é R${1.2 * preco:.2f}')
