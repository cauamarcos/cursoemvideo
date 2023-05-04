from math import fabs

r1 = float (input ('Comprimento da reta 1: '))
r2 = float (input ('Comprimento da reta 2: '))
r3 = float (input ('Comprimento da reta 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and fabs (r1 - r2) < r3 and fabs (r1 - r3) < r2 and fabs (r2 - r3) < r1:
    print ('\033[32mEssas retas podem formar um triângulo!!\033[m')
    print (f'Esse triângulo é {"equilátero" if r1 == r2 and r1 == r3 else "isósceles" if r1 == r2 or r1 == r3 or r2 == r3 else "escaleno"}!')
else:
    print ('\033[31mEssas retas não podem formar um triângulo!\033[m')
