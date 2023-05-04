from random import choice

lista = ['pedra', 'papel', 'tesoura']
a = choice (lista)
b = str (input ('Jokenpô: ')).strip ().lower ()
if a == b:
    print ('\033[33mEu escolhi o mesmo que você\033[m')
elif a == 'pedra' and b == 'tesoura':
    print ('\033[31mPedra quebra tesoura\033[m')
elif a == 'tesoura' and b == 'papel':
    print ('\033[31mTesoura corta papel\033[m')
elif a == 'papel' and b == 'pedra':
    print ('\033[31mPapel enrola pedra\033[m')
elif a == 'tesoura' and b == 'pedra':
    print ('\033[32mPedra quebra tesoura\033[m')
elif a == 'papel' and b == 'tesoura':
    print ('\033[32mTesoura corta papel\033[m')
elif a == 'pedra' and b == 'papel':
    print ('\033[32mPapel enrola pedra\033[m')
