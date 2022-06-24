import os
ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def menu_ciclico():
  print(f'''Subtitulos
  {ESP}) Espaniol
  {ING}) Ingles
  {NO_SUBS}) Sin subtitulos
  {SALIR}) Salir
  ''')

continuar = True
while continuar:
  os.system('cls')
  menu_ciclico()
  opc_usuario = int(input(f'Selecciona una opcion: '))
  os.system('cls')
  if opc_usuario == ESP:
    print('Subtitulos en Espaniol')
  elif opc_usuario == ING:
    print('Subtitulos en Inlges')
  elif opc_usuario == NO_SUBS:
    print('Subtitulos desactivados')
  elif opc_usuario == SALIR:
    print('saliendo')
    continuar = False
  else:
    continuar = False
    print('opcion no valida') 
