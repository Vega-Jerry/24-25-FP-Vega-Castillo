import random

# Definimos la matriz 3D con temperaturas diarias para 3 ciudades, 7 días de la semana y 4 semanas
ciudades = 3
dias = 7
semanas = 4

# Inicializamos la matriz con valores de temperatura aleatorios
temperaturas = [[[random.randint(15, 30) for _ in range(dias)] for _ in range(semanas)] for _ in range(ciudades)]

# Inicializamos una matriz para almacenar los promedios
promedios = [[0 for _ in range(semanas)] for _ in range(ciudades)]

# Calculamos el promedio de temperaturas para cada ciudad y semana
for ciudad in range(ciudades):
    for semana in range(semanas):
        suma = 0
        for dia in range(dias):
            suma += temperaturas[ciudad][semana][dia]
            # Mostramos la temperatura de cada ciudad por día
            print(f'Ciudad {ciudad + 1}, Semana {semana + 1}, Día {dia + 1}: {temperaturas[ciudad][semana][dia]} °C')
        promedios[ciudad][semana] = suma / dias

# Mostramos el promedio de temperaturas para cada ciudad y semana
for ciudad in range(ciudades):
    for semana in range(semanas):
        print(f'Promedio de temperaturas para Ciudad {ciudad + 1}, Semana {semana + 1}: {promedios[ciudad][semana]:.2f} °C')