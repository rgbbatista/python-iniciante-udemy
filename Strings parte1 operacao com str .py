'''Strings é um tipo de dados em que se armazena coleçoes
de caracteres(texto), são declaradas entre aspas'''
var='1'
#Operação com Strings
# 1ºConcatenação de Strings:soma aplicada a duas variaveis
a = 'Rodrigo'
b = 'Batista'
c ='Gomes'
concatenar = a+''+c+' '+b
print(concatenar)

#2ºtamanho de um str
tamanho = len(concatenar)
print(tamanho)

tamanho = len(c)
print(tamanho)

#3ºNavegação sobre os índices: usando []colchetes
print(a[0])
print(a[2])
print(c[4])
print(a[0:7])
print(c[1:3])

