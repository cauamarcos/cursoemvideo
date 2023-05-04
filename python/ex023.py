num = int (input ('Digite um número de 0 a 9999: '))
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
unidadeMilhar = num // 1000
print (f'''Unidade de milhar: {unidadeMilhar}
Centena: {centena}
Dezena: {dezena}
Unidade: {unidade}''')
