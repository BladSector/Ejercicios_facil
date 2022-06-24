'''
funciones_e.py
Script en Python que implemente un programa para realizar las siguientes
conversiones:
-segundos a minutos: recibe segundos y devuelve minutos y segundos
-segundos a horas: recibe segundos y los regresa en horas, minutos y segundos
-minutos a segundos: recibe minutos y segundos y regresa segundos
-minutos a horas: recibe minutos y segundos y regresa horas, minutos y segundos
Ademas debera implementarseun metodo para imprimir el menu de opciones y
la ejecucion del programa debe comenzar desde el procedimiento "main".
El programa debe seguir en ejecucion mientras el usuario no decida
salir.
'''
import os

SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORAS = 60

SEGUNDOS_A_MINUTOS = 1
SEGUNDOS_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 0

def segundos_a_minutos(segundos):
    mins = segundos // SEGUNDOS_POR_MINUTO
    segs = segundos % SEGUNDOS_POR_MINUTO
    return mins, segs

def minutos_a_segundos(minutos):
    segs = minutos * SEGUNDOS_POR_MINUTO
    return segs

def minutos_a_horas(minutos):
    hrs = minutos // MINUTOS_POR_HORAS
    mins = minutos % MINUTOS_POR_HORAS
    return hrs, mins

def segundos_a_horas(segundos):
    mins, segs = segundos_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)
    return hrs, mins, segs

def menu():
    print(f'''        Conversiones
        {SEGUNDOS_A_MINUTOS})Segundos a minutos
        {SEGUNDOS_A_HORAS})Segundos a horas
        {MINUTOS_A_SEGUNDOS})Minutos a segundos
        {MINUTOS_A_HORAS})Minutos a horas
        {SALIR})Salir
        ''')
def main():
    continuar = True
    while continuar:
        os.system('cls')
        menu()
        opc = int(input('    Selecciona una opcion: '))
        os.system('cls')
        if opc == SEGUNDOS_A_MINUTOS:
            s = int(input('    Cantidad de segundos a convertir a minutos: '))
            if s > 0:
                mins, segs = segundos_a_minutos(s)
                print(f'    El equivalente es {mins}m :{segs}s ')
                print('')
                input('Presione ENTER para volver.')
            else:
                print('    No se puede introducir numeros negativos.')
                print('')
                input('Presione ENTER para volver.')
        elif opc == SEGUNDOS_A_HORAS:
            s = int(input('    Cantidad de segundos a convertir a horas: '))
            if s > 0:
                hrs, mins, segs = segundos_a_horas(s)
                print(f'    El equivalente es {hrs}h :{mins}m :{segs}s ')
                print('')
                input('Presione ENTER para volver.')
            else:
                print('    No se puede introducir numeros negativos.')
                print('')
                input('Presione ENTER para volver.')
        elif opc == MINUTOS_A_SEGUNDOS:
            m = int(input('    Cantidad de minutos a convertir a segundos: '))
            if m > 0:
                segs = minutos_a_segundos(m)
                print(f'    El equivalente es {segs}s ')
                print('')
                input('Presione ENTER para volver.')
            else:
                print('    No se puede introducir numeros negativos.')
                print('')
                input('Presione ENTER para volver.')
        elif opc == MINUTOS_A_HORAS:
            m = int(input('    Cantidad de minutos a convertir a horas: '))
            if m > 0:
                hrs, mins = minutos_a_horas(m)
                print(f'    El equivalente es {hrs}h :{mins}m ')
                print('')
                input('Presione ENTER para volver.')
            else:
                print('    No se puede introducir numeros negativos.')
                print('')
                input('Presione ENTER para volver.')
        elif opc == SALIR:
            print('    Nos vemos...')
            continuar = False
        else:
            print('    Opcion no valida')
            input('Presione ENTER para continuar')

if __name__ == '__main__':
    main()
