num = int (input ('Digite um número inteiro: '))
print ('''Para qual base você deseja converter esse número?
[ 1 ] = binário
[ 2 ] = octal
[ 3 ] = hexadecimal''')
escolha = int (input ('Sua escolha: '))
if escolha == 1:
    print (f'{num} em binário corresponde a {bin (num) [2:]}')
elif escolha == 2:
    print (f'{num} em octal corresponde a {oct (num) [2:]}')
elif escolha == 3:
    print (f'{num} em hexadecimal corresponde a {hex (num) [2:]}')
else:
    print ('\033[31mErro\033[m')
