'''
anidamiento estructural.py
script en Python que simula un juego de preguntas y respuestas,
si el usuario contesta correctamente una pregunta puede continuar
con la siguiente, en caso contrario se le indica que ha perdido.
Si contesta bien todas las preguntas se le dejara entrar.
'''

print('''Te voy hacer unas cuantas preguntas y tendras que responder.
Si respondes correctamente podras entrar. Por favor escribir todo con mayuscula''')

respuesta_1 = input('''Como te llamas?
''')

respuesta_2 = input('''Cuando naciste?
Responder como en el ejemplo: 11/11/1111
 ''')

respuesta_3 = input('''Cual es el sentido de la vida?
''')

if respuesta_1 == 'SANTIAGO' and respuesta_2 == '21/06/1998' and respuesta_3 == 'SE LA DA CADA UNO':
    print ('Bienvenido')
else:
    print('No has podido acceder')
