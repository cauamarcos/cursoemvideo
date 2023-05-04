cidade = (input ('Digite o nome de uma cidade: ')).strip ()
iniciais = cidade[:4].lower ()
print (f'O nome dessa cidade começa com "São"? {"são " in iniciais or "sao " in iniciais}')
