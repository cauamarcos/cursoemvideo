dias = int (input ('Por quantos dias você alugou o carro? '))
dist = float (input ('Quantos km você andou? '))
print (f'O valor do aluguel ficou em R$ {30 + (dias * 40) + (dist * 0.2) :.2f}')
