"""
estructura selectiva simple E
"""
calificacion = int(input("¿cual es tu clasificaion? "))
if calificacion < 0:
    print("No se puede ingresar numeros negativos")
if calificacion > 100:
    print("No se puede ingresar una calificacion mayor a 100")

residuo = calificacion % 10
if residuo < 6 and calificacion >= 0 and calificacion <= 100:
    print("tu calificacion no amerita redondeo")

if residuo >= 6 and calificacion >= 0 and calificacion <= 100:
    calificacion_1 = calificacion + (10 - residuo)
    mensaje = f"Tu calificacion es : {calificacion_1}"
    print(mensaje)

print("Que tengas un buen dia")
