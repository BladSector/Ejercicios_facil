'''
6) Realiza una función separar() que tome una lista de números enteros y
devuelva dos listas ordenadas. La primera con los números pares, y la segunda
con los números impares:

🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]

'''

numeros = range(0,21)

def separar(LISTA):
    for lista in LISTA:
        if lista % 2 == 0:
            PARES.append(lista)
        else:
            IMPARES.append(lista)

    return PARES, IMPARES

PARES = []
IMPARES= []

PARES, IMPARES = separar(numeros) # Porque no me toma 'split()'? y 'separar' si?
print(f'    Los numeros pares: {PARES}')
print(f'    Los numeros impares: {IMPARES}')
print('')

input('    Presiona ENTER para salir.')
exit()
