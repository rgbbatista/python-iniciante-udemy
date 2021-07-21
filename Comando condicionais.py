# comando if
'''x=1
y=100

if x > y:
    print('x é maior que y')
if y > x:
    print('y é maior que x')'''

#comando else
'''
x=1
y=2

if x > y:
    print('x é maior que y')
else:
    print('x não é maior que y')'''

#cuidado com a indentação
'''
a = -5
b = 4
if b > a:
    if b > 0:
        print('b é maior que a\nb é ´positivo')
    else:
        print('b não é maior que a nem positivo')
else:
     print('b menor que a')'''
#Comando elif
x = 1
y = 2
#é executada a primeira condição verdadeira que encontrar
if x == y:
    print('números iguais')
elif x < y:
    print('x menor que y')
elif y > x:
    print('y maior que x')
else:
    print('números diferentes')
