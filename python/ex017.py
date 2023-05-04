import math

co = float (input ('Tamanho do cateto oposto: '))
ca = float (input ('Tamanho do cateto adjacente: '))
print (f'Tamanho da hipotenusa: {math.sqrt (math.pow (co, 2) + math.pow (ca, 2)) :.1f}')
