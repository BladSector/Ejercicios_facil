'''
Crear un programa para calcular la nota final de un estudiante de base a tres \
examénes, los examénes cuentan con un porcentaje distinto de la nota final. \
Nota 1 cuenta como un 20% de la nota final, nota 2 cuenta como un 30%, y de \
la nota final de la nota 3 cunta como el 50% de la nota final.
'''

print('Para calcular su nota final ingrese sus promedios en decimales \
(usar "." en vez de ",") de los tres examenes ya rendidos.')

print('Su promedio será la suma del porcentaje correspondiente a cada examen. ')

print('El primer examen cuenta con un 20% de la nota final, el segundo con un \
30% y el tercero con un 50%. Suerte!.')

# Notas ingresadas por el estudiante y errores de limites⬇
nota_1 = float(input('Primer examen: '))

while nota_1 < 0 or nota_1 > 10:
    print("La nota tiene que ser de 0 al 10")
    nota_1 = float(input('Primer examen: '))

nota_2 = float(input('Segundo examen: '))

while nota_2 < 0 or nota_2 > 10:
    print("La nota tiene que ser de 0 al 10")
    nota_2 = float(input('Segundo examen: '))

nota_3 = float(input('Tercer examen: '))

while nota_3 < 0 or nota_3 > 10:
    print("La nota tiene que ser de 0 al 10")
    nota_3 = float(input('Tercer examen: '))

# Notas promedio de cada examen ⬇
nota_1_promedio = nota_1*0.2
nota_2_promedio = nota_2*0.3
nota_3_promedio = nota_3*0.5

# Resultado de nota final ⬇
nota_final = nota_1_promedio + nota_2_promedio + nota_3_promedio

# Resultado del examen final y sus promedios de cada examen ⬇
print('')
print('Su promedio en cada examen')
print('')
print(f'Primer examen: {nota_1_promedio:.1f}')
print(f'Segundo examen: {nota_2_promedio:.1f}')
print(f'Tercer examen: {nota_3_promedio:.1f}')
print('')
print(f'Sumando las notas de promedio de cada examen su nota final es: \
{nota_final:.1f}')

# Informacion sobre el resultado
if nota_final <= 5.999:
    print('Lo siento. Has desaprobado.')
if nota_final >= 6.000:
    print('Felicitaciones. Aprobaste.')
