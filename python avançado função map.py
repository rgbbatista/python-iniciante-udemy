#Função map
'''Função mao :pega uma função e aplica a todos os
elementos de uma lista.

para ex van,os ver a função dobro'''

def dobro(x):
    return x*2
valor = 2
print(dobro(valor))
print()
'''para vários elementos ao mesmo tempo usando map'''

#primeira forma de fazer: usando for
def dobro(x):
    return x*2
valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)
for v in valor_dobrado:
      print(v)
print()

#segunda forma de fazer: convertendo em uma lista
def dobro(x):
    return x*2
valor = [1, 2, 3, 4, 5]
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)
print()
