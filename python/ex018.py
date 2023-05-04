from math import sin, cos, tan, radians
from random import randint

a = randint (0, 360)
print (f'''sen {a}° = {sin (radians (a)) :.2f}
cos {a}° = {cos (radians (a)) :.2f}
tg {a}° = {tan (radians (a)) :.2f}''')
