"""
estructura selectiva simple 2
script en Python que genere un numero aleatorio entre 1 y 10
y le pda al ususario que intente adivinarlo. Si adivina el numero
que lo felicite por su logro.
"""
#agrga el modulo random a mi programa y con ello me permite generar
#numeros aleatorios
import random
secreto = random.randint(1,10)
print("Estoy pensando en un numero del 1 al 10. intenta adivinar cual elegui")
numero = int(input("¿cual numero decis que estoy pensando? "))
if numero == secreto:
    print("felicidades, le pegaste. En algun momento ese 10% iba a suceder")
else:
    print(f"Mi numero secreto era {secreto}")
if numero != secreto:
    print("Segui intentando bro")
"""
selectiva doble 1
Y en caso contrario (else) le indica cual era el numero secreto.
"""
