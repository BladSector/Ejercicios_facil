'''
selectiva multiple 1.py
script en Python que solicite al usuario una calificacion y una/
cantidad de asistencias a un curso. Si la calificaion y la/
cantidad de asistencias son aprobatorias entonces se le felicita/
por su logro; en caso contrario se le indicara en que fallo. La/
 calififcaion minima aprobatoria sera de 60 y la cantidad minima de/
 asistencias sera 24.
'''

MIN_CAL = 60
MIN_ASI = 24

print('Por favor ingresa los siguientes datos: ')
cal = int(input('Calificaion: '))
asi =int(input('Asistencias: '))

if cal >= MIN_CAL and asi >= MIN_ASI:
    print('Felicidades aprobaste este curso!')
elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f'Calificacion insuficiente. El minimo es {MIN_CAL}')
elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f'Asistencias insuficientes. El minimo es {MIN_ASI}')
elif cal < MIN_CAL and asi <MIN_ASI:
    print(f'Calificacion y asistencias insuficientes.')

print('Que tenga un buen dia.')
