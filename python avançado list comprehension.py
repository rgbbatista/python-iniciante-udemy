#list comprehension

x = [1, 2, 3, 4, 5]
y = []

#para obter o quadrado da lista x em y
for i in x:
    y.append(i**2)
print(x)
print(y)
print()
'''usando a list comprehension'''

# z = [2, 3, 4, 5, 6]
# w = [valor_a_adicionar laço condição]
print('usando a list comprehension , valor e laço')

z = [2, 3, 4, 5, 6]
w = [i**2 for i in z]
print(z)
print(w)
print()

print('usando a list comprehension , valor , laço e condição')
print('imprimir somente os números ímpares da lista abaixo')

a = [12, 15, 1145, 5469, 4, 1, 48, 5]
b = [i for i in a if i%2==1]#se o resto da div por 2 for =1

print(a)
print(b)
