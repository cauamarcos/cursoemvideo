num = int (input ('Digite um número: '))
numDivisores = 0
for c in range (1, num + 1):
    if num % c == 0:
        numDivisores += 1
if numDivisores == 2:
    print (f'{num} é primo!')
else:
    print (f'{num} não é primo!')
