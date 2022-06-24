"""
estrcuura selectiva simple 5
sript de Pyton que pregunte al usuario cuanto indica el termometro
y si ese valor se encuentra entre 18 y 27 que le indique que
la temperatura es agradable
"""
print("¿Que temperatura hace en este momento?")
temperatura_1 = int(input("En grados Celcius por favor: "))

if temperatura_1 >= 18 and temperatura_1 <=27:
    print("Me alegra informarle que hay una temperatura agradable mi querido usuario")
if temperatura_1 < 18 or temperatura_1 >27:
    print("Su temperatura no es la mas confortante")
    if temperatura_1 < 5:
        print("A su puta madre hace frio")
    if temperatura_1 > 30:
        print("Usted esta siendo incinerado vivo")
print("Que tenga un buen dia mi señor usuario que no sabe cual es una temperatura agradable")
5
