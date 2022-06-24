'''
repetitiva_mientras_3.py
script en Python que simule el sistema de validacion
de datos de una plataforma digital. Se le solicitara
al usuario su nombre y contrasenia mientras la
informacion proporiconada no coincida con la
informacion previamente resgistrada.
'''

import os

USER = 'Santiauo0698'
PASSWORD = 'Santiauo9806'

user=''
password=''

while USER != user or PASSWORD != password:
    os.system('cls')
    print('             Hola')
    user = input('Usuario: ')
    password = input('Contrasenia: ')

    if USER != user or PASSWORD != password:
        print('''Incorrecto
Intenta de nuevo''')
        input('presiona enter para volver a intentar')
else:
    print('Bienvenido')

#Usuario nuevo
'''
Script en Python usuario nuevo
Nombre y apellido, telefono, mail, curriculum (link o archivo) y
puesto de trabajo solicitado.
Y que responda con un mail al operador con la informacion ingresada.
'''
USER_N = ''
PASSWORD_N = ''

USER_N = input('Introduzca su nombre de ususario: ')
MAIL_N_1 = input('Introduzca su contrasenia nueva: ')

while PASSWORD_N_1 = PASSWORD_N_2:
    MAIL_N_2 = input('Introduzca su contrasenia de vuelta: ')
