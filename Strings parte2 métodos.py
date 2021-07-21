#string = string.método()

a = 'Rodrigo'
b = 'Batista'
c ='Gomes'
concatenar = a + ' '+ c +' '+ b
print(concatenar)
#imprir em minúsculo: função lower()
print(concatenar.lower())

#imprir em caixa alta: função lower()
print(concatenar.upper())

# Assim mudou a atribuição de concatenar
concatenar = concatenar.lower()
print(concatenar)
print('\n')

#Função strip: remove os espaços no começo e no fim da str
print(a,'\n')
print(b)
print(a.strip())

print('\n')

#Função Split : Converte uma str em uma
minha_string = 'O rato roeu a roupa do rei de Roma'
minha_lista = minha_string.split()
print(minha_lista)

'''podemos fazer quebra de texto, por exemplo a letra r
o python e case sensitive diferencia a letra maiúscula de
minúscula, por isso R não foi quebrado'''

minha_lista = minha_string.split('r')
print(minha_lista)
print('\n')

#Buscando Substrings: método find
'''em qual posição está a palavra rei'''

minha_string = 'O rato roeu a roupa do rei de Roma'
busca = minha_string.find('rei')
print(busca)

'''imprimir a parte do texto que começa com rei até o final'''
print(minha_string [busca:])
''' imprimir a palavre rei'''
print(minha_string [busca:26])

'''se não encontrar retorna -1'''
minha_string = 'O rato roeu a roupa do rei de Roma'
busca = minha_string.find('rainha')
print(busca)
print('\n')

#Substituir parte de uma str: método replace
minha_string = 'o rei de Roma foi pra Rússia'
minha_string = minha_string.replace('o rei', 'a rainha')
print(minha_string)