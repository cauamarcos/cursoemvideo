dist = float (input ('Quantos km você vai viajar? '))
if dist <= 200:
    custo = dist * 0.5
else:
    custo = dist * 0.45
print (f'O custo ficará em R${custo :.2f}.')
