from math import fabs #módulo

r1 = float (input ('Digite o comprimeto de uma reta: '))
r2 = float (input ('Digite o comprimeto de outra reta: '))
r3 = float (input ('Digite o comprimeto de mais uma reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 and fabs (r1 - r2) < r3 and fabs (r2 - r3) < r1 and fabs (r1 - r3) < r2:
    print ('Essas retas podem formar um triângulo!')
else:
    print ('Essas retas não podem formar um triângulo!')
