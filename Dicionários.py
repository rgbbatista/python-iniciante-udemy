'''Dicionários:são lista de associação composta
 por uma chave {}e uma valor correspondete'''

meu_dicionario = {'a':'ameixa','b':'bola', 'c':'cachorro'}
#para imprimir utiliza a chave
print(meu_dicionario['a'])
print(meu_dicionario['c'])
print(meu_dicionario)#imprimri dicionario inteiro
print('\n')

#navegar pelo dicionário
'''imprimir as chaves'''
for chave in meu_dicionario:
    print(chave)
print('\n')
'''imprimir o valor'''
for chave in meu_dicionario:
    print(meu_dicionario[chave])#Imprime dicionario na posição chave
print('\n')
'''imprimir as chaves e o valor'''
for chave in meu_dicionario:
    print(chave + '-'+ meu_dicionario[chave])
print('\n')

#usando função items
'''vai converter o dicionário em uma tupla(lista imúltavel)'''
for i in meu_dicionario.items():
    print(i)
print('\n')

#função método values
for i in meu_dicionario.values():
    print(i)#retorna os valores
print('\n')
#função método keys
for i in meu_dicionario.keys():
    print(i)#retorna as chaves
print('\n')