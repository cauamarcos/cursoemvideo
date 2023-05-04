n = int (input ('Digite o primeiro termo de uma PA: '))
r = int (input ('Digite a razão da PA: '))
for c in range (n, n + 10 * r, r):
    print (c, end=' ')
