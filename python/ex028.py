from random import randint

num = randint (0, 5)
palpite = int (input ('Estou pensando em um número inteiro de 0 a 5, tente acertar qual é! '))
if palpite == num:
    print ('Você acertou!')
else:
    print ('Você errou!')
