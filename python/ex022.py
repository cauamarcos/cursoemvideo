nome = input ('Digite um nome: ').strip ()
#o strip serve para remover espaços teclados antes e depois do nome
nomeEmLista = nome.split () #cada palavra do nome vira um elemento da lista
print (nome.upper ())
print (nome.lower ())
nomeTudoJunto = ''.join (nomeEmLista)
print (len (nomeTudoJunto))
print (len (nomeEmLista[0]))
