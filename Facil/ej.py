import os

lista_numeros = [1,2,3,9]

numero = int(input('Ingrese un numero del 0 al 9: '))


while numero < 0 or numero > 9:
  os.system('cls')
  print('Valor incorrecto.')
  numero = int(input('Ingrese un numero del 0 al 9: '))
  if numero >= 0 and numero <= 9:
    False
# 'in' sirve para comprobar si el valor esta dentro de una lista
if numero in lista_numeros:
  print(f'El {numero} se encuentra en la lista. Gracias')
else:
    print(f'El {numero} no se encuentra en la lista. Lo siento')
