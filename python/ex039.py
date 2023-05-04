from datetime import date

data = date.today ().year
anoNasc = int (input ('Digite seu ano de nascimento: '))
idade = data - anoNasc
if idade < 18:
    print (f'\033[32mVocê deverá se alistar {"ano que vem" if idade == 17 else f"daqui {18 - idade} anos"}!\033[m')
elif idade == 18:
    print ('\033[36;41mVocê deve se alistar esse ano!\033[m')
else:
    print (f'\033[31mSeu prazo para alistamento militar expirou há {idade - 18} {"ano" if idade == 19 else "anos"}!\033[m')
