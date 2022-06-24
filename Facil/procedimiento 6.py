'''
procedimiento 6.py
script en Python que implemente un procedimiento
que reciba el nombre y la edad del usuario y en
el caso que la edad sea mayor o igual que 18 le
indique que ya es mayor de edad; en caso contrario
le indique que es menor de edad
'''
import os
def saludo(USUARIO):
    print(f'Hola {USUARIO}, un gusto. ')

USUARIO = input('''Hola! Como te llamas?
''')

os.system('cls')
try:
    EDAD = int(input('''Cuantos anios tienes?:
'''))
except ValueError:
    print('No as introducido un numero.')
    input('Presiona ENTER.')
    exit()

os.system('cls')
saludo(USUARIO)
if EDAD < 0:
    print('')
    print('Usted no ha nacido todavia.')
elif EDAD > 100:
    print('')
    print('Usted es un ser inmortal')
elif EDAD < 18 and EDAD >= 0:
    print('')
    print(f'Usted con {EDAD} todavia no es mayor de edad.')
elif EDAD >= 18 and EDAD >= 100:
    print('')
    print(f'Usted con {EDAD} ya es mayor de edad.')

input('Presione enter para salir')
