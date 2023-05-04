somaPares = 0
print ('Você digitará 6 números')
for c in range (1, 7):
    n = int (input (f'Digite o {c}º número:'))
    if n % 2 == 0:
        somaPares += n
if somaPares == 0:
    print ('Você não digitou nenhum número par!')
else:
    print (f'A soma dos números pares que você digitou é {somaPares}')
