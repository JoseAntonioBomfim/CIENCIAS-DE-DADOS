import math

a = 4
b = 10
c = 6

b_2 = b*b
delta = b_2 -4 * a *c
raiz = math.sqrt(delta)
parteDeCima_posisitivo = -b + raiz
parteDeCima_negativo = -b - raiz
parteDebaixo = 2*a
x1 = parteDeCima_posisitivo/parteDebaixo
x2 = parteDeCima_negativo/parteDebaixo

print('variavel 1 :', x1, 'variavel 2:', x2)