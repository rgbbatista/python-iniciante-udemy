#usando módulo random

import random
#agora podemos chamar métodos que gera  núm aleatórios
'''método randint'''
numero = random.randint(0,10)
print(numero)
print('\n')

#forçar o python a dar sempre o mesmo núm
'''método seed'''
'''
random.seed(1)
numero = random.randint(0,10)
print(numero)
print('\n')'''

#para selecionar um num de uma lista
'''método choice'''
lista = [12,45,118]
numero1 = random.choice(lista)
print(numero1)
