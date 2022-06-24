'''
argumentos.py
script en python que implemente un procedicmiento para imprimir un menu
generico. El procedimiento debera recibir el titulo del menu como primer
argumento, seguido de las opciones a imprimir y finalmente un parametro
con nombre para el mensaje de error en caso de una opcion no valida.
'''

def menu(titulo, *args, **kwargs):
    print(f'    {titulo}')
    for i in range(len(args)):
        print(f'{i+1}) {args[i]}')
    opc = int(input('Selecciona una opcion: '))
    if 1 <= opc <= len(args):
        print(f'Seleccionaste la opcion {args[opc-1]}')
    else:
        print('Opcion no valida')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')

menu('Operaciones aritmeticas', 'Suma', 'Resta', 'Mulitplicaion',
error = 'No existe tal opcion')

print('Nos vemos...')
