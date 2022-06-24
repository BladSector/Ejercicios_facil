"""
secuancial_e.py
script de ptyhon que calcule el area de un triangulo. \
El ususario debera ingresar tanto el valor de la base como el de la \
altura y el programa mostrara el valor del area. \
"""
print("Este prgrama nos va a ayudar a calcular el area de un triangulo")
valor_1 = float(input("ingresar el valor de la base en cm: "))
valor_2 = float(input("y el valor de la altura tambien en cm:  "))

resultado = (valor_1 * valor_2) / 2
print(f"el area del triangulo es {resultado} cm2")
print(f" ({valor_1} cm de base * {valor_2} cm de altura) / {2} = {resultado} cm2 de area")
