#listas: conj de dados(numérica n strings)

minha_lista = ['abacaxi','melancia', 'abacate']
minha_lista2 = [1,2,3,4,5,]
minha_lista3 = ['abacaxi',2,9.89,True]

print(minha_lista)
print('\n')
print(minha_lista2[3])#imprim o índice
print('\n')
#Navegar pelos elementos da lista com laço for
for elementos in minha_lista3:
    print(elementos)
print('\n')

#Tamanho da lista usando a função len
tamanho = len(minha_lista3)
print(tamanho)
print('\n')

#adicionando elementos a lista função append
minha_lista.append('limão')
print(minha_lista)
print('\n')

#verif se um elemento pertence a uma lista
if 3 in minha_lista2:
    print('3 está na lista')
    print('\n')

#remover elementos da lista função del
del minha_lista[2:]#remove do item 2 pro final
print(minha_lista)

del minha_lista3[:]#remove toda lista,fica em branco
print(minha_lista3)
print('\n')

#criar lista em branco e preenxer aos poucos
minha_lista4 = []
minha_lista4.append('jaca')
print(minha_lista4)
minha_lista4.append('manga')
print(minha_lista4)


