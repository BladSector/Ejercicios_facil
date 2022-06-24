'''
funciones_4.py
script en python que implemente una funcion para calcular el area de un
triangulo.  Dicha funcion debera recibir como argumento el valor de la base
y la altura y regresara el area calculada.
'''

def area_triangulo(altura, base):
    return base * altura / 2
print('Programa que calcula el area de un triangulo')
print('Ingresa los siguientes valores')
altura = float(input('Altura: '))
base = float(input('Base: '))

print(f'Area = {area_triangulo(altura, base)}')
