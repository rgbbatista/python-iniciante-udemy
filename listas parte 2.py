#Ordenar lista numéricamente
lista =  [124,345,5,72,46,6,7,3,1,7,0]
#método sorte/sorted ordenar a lista
lista.sort()#ordenar a lista
print(lista)
#função sorted
lista =sorted(lista)#nec aplicar na varável
print(lista)
print('\n')
#Ordena de forma decrescente
lista =  [124,345,5,72,46,6,7,3,1,7,0]
lista.sort(reverse=True)
print(lista)
print('\n')
#reverter a lista, o primeiro vai ser o último sucessivamente
lista =  [124,345,5,72,46,6,7,3,1,7,0]
lista.reverse()
print(lista)
print('\n')

#ordenação de strigs ordem alfabética
lista2 = ['bola', 'abacate', 'dinheiro']
lista2.sort()
print(lista2)
#ou
lista2 = sorted(lista2)
print(lista2)
print('\n')

#Ordena de forma decrescente
lista2.sort(reverse=True)
print(lista2)



