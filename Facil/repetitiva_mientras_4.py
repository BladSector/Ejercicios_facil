'''
repetitiva_mientras_4
script de Python que muestre un menu con distintos
personajes de un videojuego. Si el usuario selleciona
alguno de los personajes, se le mostrara'n sus
caracteri'sticas. El menu' sera' ci'clico y se
mostrara' mientras el usuario no indique que desea
salir.
'''

import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4

#Bandera
continuar = True

while continuar:
    os.system('cls')
    print(f'''          Personajes
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    ''')
    opciones = int(input('Seleccionar tu personajes: '))

    if opciones == MAGO:
        print('''
        Fuerza: 6
        Energia: 20
        Especial: 17
        ''')
        input('')
    elif opciones == GUERRERO:
        print('''
        Fuerza: 16
        Energia: 10
        Especial: 12
        ''')
        input('')
    elif opciones == SACERDOTISA:
        print('''
        Fuerza: 9
        Energia: 15
        Especial: 20
        ''')
        input('')
    elif opciones == SALIR:
        continuar == False
        input('presiona enter para continuar')
    else:
        print('Opcion no valida')
        input('presiona enter para continuar')
