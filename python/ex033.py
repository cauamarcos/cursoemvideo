n1 = float (input ('Digite um número: '))
n2 = float (input ('Digite outro: '))
n3 = float (input ('Digite mais um: '))
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1
print (f'''Maior: {maior}
Menor: {menor}''')
