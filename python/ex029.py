speed = int (input ('A quantos km/h você passou pelo radar? '))
if speed > 80:
    print (f'O limite era de 80 km/h, a multa custará R${(speed - 80) * 7}.')
else:
    print ('Que bom! O limite era de 80 km/h.')
