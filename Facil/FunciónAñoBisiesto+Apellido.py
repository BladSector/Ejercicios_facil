'''
Formato: El documento debe presentarse en Google Docs bajo el siguiente formato:
“FunciónAñoBisiesto+Apellido”. Colabs.
Sugerencia: En el formulario debe estar el print de pantalla de la consola con
el ejercicio resuelto, como así también el código tipeado.

Consigna: Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número debe indicar que se ingrese un número.


#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de
100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de
posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto,
1900 no es bisiesto.
'''
import os


def MENU ():
    print('''-------Bienvenido a "Año Bisiesto's"-------

    Su mejor solucion para saber cuales son años bisiestos y cuales no.''')

#Comienzo de script en pantalla. Menu y opciones
MENU()
print('''    1)Averiguar sobre uno o varios años.
    2)Averiguar sobre una franja de años.
    ''')
try:
    OPC_M = int(input('''    Preseione 1 o 2: '''))
except ValueError:
    print("La opción que ingreso no es un numero")
    input('Presiona ENTER')
    exit()

#Si el usuario ingresa fuera del rango de las opciones 1 y 2
while OPC_M <= 0 or OPC_M >= 3:
    input('Opcion no valida. Presiona ENTER. ')
    os.system('cls')
    MENU ()
    print('''    1)Averiguar sobre uno o varios años.
    2)Averiguar sobre una franja de años.
        ''')
    try:
        OPC_M = int(input('''    Preseione 1 o 2: '''))
    except ValueError:
        print("La opción que ingreso no es un numero")
        input('Presiona ENTER')
        exit()

#Si el usuario elige la opcion 1
while OPC_M == 1:
    os.system('cls')
    MENU()
    print('')
    try:
        ANIO = int(input('''   -Si desea volver al menu escirbir "0"
    Introduzca el año que desea: '''))
    except ValueError:
        print("La opción que ingreso no es un numero")
        input('Presione ENTER')
        exit()
    #Opcion de volver al Menu
    if ANIO == 0:
        os.system('cls')
        MENU ()
        print('''    1)Averiguar sobre uno o varios años.
    2)Averiguar sobre una franja de años.
            ''')
        try:
            OPC_M = int(input('''    Preseione 1 o 2: '''))
        except ValueError:
            print("La opción que ingreso no es un numero")
            input('Presione ENTER')
            exit()

    #Calculo si el dato ingresado es anio bisiesto o no
    elif ANIO % 4 != 0:
        print("    ¡No es bisiesto! >:(")
        print('')
        OPC_MENU = input('''    Presione enter para volver introducir otro año.
    ''')

    elif ANIO % 4 == 0 and ANIO % 100 != 0:
        print("    ¡Es bisiesto! :)")
        print('')
        OPC_MENU = input('''    Presione enter para volver introducir otro año.
    ''')


    elif ANIO % 4 == 0 and ANIO % 100 == 0 and ANIO % 400 != 0:
        print("    ¡No es bisiesto! >:(")
        print('')
        OPC_MENU = input('''    Presione enter para volver introducir otro año.
    ''')

    elif ANIO % 4 == 0 and ANIO % 100 == 0 and ANIO % 400 == 0:
        print("    ¡Es bisiesto! :)")
        print('')
        OPC_MENU = input('''    Presione enter para volver introducir otro año.
    ''')

#Si el ususario elige la opcion 2
while OPC_M == 2:
    os.system('cls')
    MENU()
    print('')
    print('   -Si desea volver al Menu escriba un "0" en cada opcion')
    print('')
    try:
        ANIO_P = int(input('    Introduzca desde que año desea saber: '))
        ANIO_F = int(input('    Introduzca el año donde desea terminar: '))
    except ValueError:
        print("La opción que ingreso no es un numero")
        input('Presione ENTER')
        exit()
    print('')
    print('    Los años bisiestos dentro de su rango son:')
    print('')
    #Opcion de volver al Menu
    if ANIO_P == 0:
        os.system('cls')
        MENU ()
        print('''    1)Averiguar sobre uno o varios años.
    2)Averiguar sobre una franja de años.
        ''')
        try:
            OPC_M = int(input('''    Preseione 1 o 2: '''))
        except ValueError:
            print("La opción que ingreso no es un numero")
            input('Presione ENTER')
            exit()
    #Calculo de la franja de numeros que ingresa el usuario
    #Y mostrar solo los anios bisiestos
    else:
        def ES_BISIESTO(ANIOS):
            return not ANIOS % 4 and (ANIOS % 100 or not ANIOS % 400)

        for ANIOS in range(ANIO_P, ANIO_F):
            if ES_BISIESTO(ANIOS):
                print(   ANIOS, end=', ')
        input('''

    Presione enter para volver a introducir una franja de años ''')
