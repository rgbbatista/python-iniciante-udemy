#Função enumerate

'''navegar por uma lista e obter ao mesmo tempo que
imprime nomes queira imprimir o índice de cada
elementos normalmente usando a função renge e len '''

lista = ['abacate', 'bola', 'cachorro']

for i in range(len(lista)):
    print(i,lista[1])
print()

'''Usando a função Enumerate'''
print('Usando a função Enumerate')

for i, nome in enumerate(lista):
    print(i,nome)
