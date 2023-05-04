from random import shuffle

rep1 = (input ('Representante do grupo 1: '))
rep2 = (input ('Representante do grupo 2: '))
rep3 = (input ('Representante do grupo 3: '))
rep4 = (input ('Representante do grupo 4: '))
lista = [rep1, rep2, rep3, rep4]
shuffle (lista)
print ('A ordem de apresentação será:', lista)
