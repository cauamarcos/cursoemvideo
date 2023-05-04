idade = int (input ('Digite sua idade: '))
print (f'Sua categoria é: {"mirim" if idade < 12 else "júnior" if 12 <= idade < 18 else "sênior"}')
