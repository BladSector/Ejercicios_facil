'''
seletiva multiple 2.py
script en Python que muestre un menu con los nombres de distintos/
paises de america y si el usuario selecciona alguna de las opciones/
se les mostrara el nombre de la capital de ese pais.
'''

MEXICO = 'mexico'
URUGUAY = 2
ARGENTINA = 3
COLOMBIA = 4
ECUADOR = 5

print('          Capitales de America          ')
print('''
 1) Mexico
 2) Uruguay
 3) Argentina
 4) Colombia
 5) Ecuador
 ''')

opc = (input('Selecciona una opcion: '))

if opc == MEXICO:
    print(' Ciudad de Mexico')
elif opc == URUGUAY:
    print(' Montevideo')
elif opc == ARGENTINA:
    print(' Buenos Aires')
elif opc == COLOMBIA:
    print(' Bogota')
elif opc == ECUADOR:
    print(' Quito')
else:
    print(' Opcion no valida.')
