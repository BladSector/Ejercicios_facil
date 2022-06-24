"""
Estructura secuencial simple 3
script en Python que solicite la calificacion y cantidad de asitencias
a un curso. Si la calificacion es mayor o igual que 60 y
la cantidad de asitencias es mayor que 20 entonces que le indique
que ah aprobado el curso
"""
import os

print(" Este programa te indicara si tu calificaion \
con las asistencias estan satisfactorias para aprobar el curso")

calificacion_1 = int(input("ingrese su calificacion: "))
#Ingreso de la nota del estudiante y errores de limites
while calificacion_1 > 100:
        print("La calificacion no puede ser mas de 100 ")
        input('')
        os.system('cls')
        print(" Este programa te indicara si tu calificaion con las asistencias \
estan satisfactorias para aprobar el curso")
        calificacion_1 = int(input("ingrese su calificacion: "))

while calificacion_1 < 0:
        print('La calificacion no puede ser menos de 0')
        input('')
        os.system('cls')
        print(" Este programa te indicara si tu calificaion con las asistencias \
estan satisfactorias para aprobar el curso")
        calificacion_1 = int(input("ingrese su calificacion: "))
        asistencias_1 = int(input("ingrese sus asistencias: "))

while asistencias_1 < 0:
    print("Las asistencias no puede ser menor que 0 ")
    input('')
    os.system('cls')
    print(" Este programa te indicara si tu calificaion con las asistencias \
estan satisfactorias para aprobar el curso")
    print(f"ingrese su calificacion: {calificacion_1} ")
    asistencias_1 = int(input("ingrese sus asistencias: "))

while asistencias_1 > 30:
    print("Las asistencias no puede se mayor a 30 ")
    input('')
    os.system('cls')
    print(" Este programa te indicara si tu calificaion con las asistencias \
estan satisfactorias para aprobar el curso")
    print(f"ingrese su calificacion: {calificacion_1} ")
    asistencias_1 = int(input("ingrese sus asistencias: "))






print("Que tenga un buen dia.")

'''The barrels must be made of unobtanium to sustain that rate of fire in real life. Yes it’s a simulation, but
the bullet physics are awesome just to see how far ahead you would have to shoot a moving moving that far away and
still have to compensate for the pull of gravity on each round. Amazing physics demo
'''
