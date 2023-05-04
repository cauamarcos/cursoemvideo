n1 = float (input ('Digite sua nota da primeira prova: '))
n2 = float (input ('Digite sua nota da segunda prova: '))
media = (n1 + n2) / 2
if media < 5:
    print (f'\033[36;41mReprovado: {media}\033[m')
elif 5 <= media < 7:
    print (f'\033[33mRecuperação: {media}\033[m')
else:
    print (f'\033[36;42mAprovado: {media}\033[m')
