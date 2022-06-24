'Desafio entregable Santiago Lopez'

'''
1) Escribí un programa que lea dos números por teclado y permita elegir entre 4
opciones en un menú:
1.Mostrar una suma de los dos números
2.Mostrar una resta de los dos números (el primero menos el segundo)
3.Mostrar una multiplicación de los dos números
4.Si elige esta opción se interrumpirá la impresión del menú y el programa
finalizará
5.En caso de no introducir una opción válida, el programa informará de que no
es correcta.
'''
import os # ← Codigo para refresh de pagina (import os - os.system)
os.system('cls')  # ← Codigo para refresh de pagina (import os - os.system)

                          #Respuesta 1

                #Introduccion de numeros del usuario ↓
print('''Hola!
Introduzca dos numeros cualquiera sin limite.
Al introducirlo tendra varias opciones para eleguir.
''')
numero_1 = int(input('Introduzca un numero: '))
numero_2 = int(input('Introduzca otro numero: '))


                #Opciones a eleguir del usuario ↓
def menu():# ← Definicion de "menu" asi ahorramos script
    print(f'''Eliga una opcion
    {suma}) Se sumara sus numeros
    {resta}) Se restaran sus numeros
    {mult}) Se multiplicaran sus numeros
    {salir}) Salida
    ''')

                #Definicion de opciones ↓
suma = 1
resta = 2
mult = 3
salir = 4
                #Calculo de cada opcion ↓
suma_r = numero_1 + numero_2
resta_r = numero_1 - numero_2
multiplicacion_r = numero_1 * numero_2

                # Ciclo del menu ↓
continuar = True
while continuar:
    os.system('cls')# ← Codigo para refresh de pagina (import os - os.system)
    print(f'Numero 1: {numero_1}') # ← Numero eleguido por el usuario 1
    print(f'Numero 2: {numero_2}') # ← Numero eleguido por el usuario 2
    print('')
    menu() # ← "menu"
    opc_usuario = int(input(f'Su eleccion: '))# ← La opcion eleguida del usuario

#Suma de los dos numeros ↓
    if opc_usuario == suma:
      print('')
      print(f'{numero_1} + {numero_2} = {suma_r} ')
      print('')
      print(f'La suma de sus dos numeros es: {suma_r}')
      input('''
        Pulsa Enter para volver
        ''')
#Resta de los dos numeros ↓
    elif opc_usuario == resta:
      print('')
      print(f'{numero_1} - {numero_2} = {resta_r} ')
      print('')
      print(f'La resta de sus dos numeros es: {resta_r}')
      input('''
       Pulsa Enter para volver
        ''')
#Multiplicacion de los dos numeros ↓
    elif opc_usuario == mult:
      print('')
      print(f'{numero_1} x {numero_2} = {multiplicacion_r} ')
      print('')
      print(f'La multiplicacion entre sus dos numeros es: {multiplicacion_r}')
      input('''
        Pulsa Enter para volver
        ''')
#Finalizacion de Programa ↓
    elif opc_usuario == salir:
        print('saliendo')
        continuar = False
#Opcion no valida ↓
    else:
        print('Opcion no valida')
        input('Presiona ENTER para volver')
