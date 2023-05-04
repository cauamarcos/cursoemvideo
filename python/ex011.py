largura = float (input ('Largura da parede a ser pintada: '))
altura = float (input ('Altura da parede a ser pintada: '))
print (f'''Área a ser pintada: {largura * altura :.2f} m²
Qtd de tinta necessária: {(largura * altura) / 2 :.2f} l''') #cada litro de tinta rende 0.5 m²
