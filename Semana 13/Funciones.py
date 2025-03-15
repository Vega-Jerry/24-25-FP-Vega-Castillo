# Definir las ciudades y semanas
ciudades = ['Quito', 'Guayaquil', 'Cuenca']
semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

# Definir las temperaturas para cada ciudad y semana
temperaturas = {
    'Quito': {
        'Semana 1': {'Lunes': 5, 'Martes': 10, 'Miércoles': 9, 'Jueves': 20, 'Viernes': 18, 'Sábado': 15, 'Domingo': 12},
        'Semana 2': {'Lunes': 20, 'Martes': 22, 'Miércoles': 20, 'Jueves': 18, 'Viernes': 15, 'Sábado': 12, 'Domingo': 10},
        'Semana 3': {'Lunes': 18, 'Martes': 20, 'Miércoles': 18, 'Jueves': 15, 'Viernes': 12, 'Sábado': 10, 'Domingo': 8},
        'Semana 4': {'Lunes': 20, 'Martes': 18, 'Miércoles': 15, 'Jueves': 12, 'Viernes': 10, 'Sábado': 8, 'Domingo': 5}
    },
    'Guayaquil': {
        'Semana 1': {'Lunes': 25, 'Martes': 28, 'Miércoles': 30, 'Jueves': 28, 'Viernes': 25, 'Sábado': 22, 'Domingo': 20},
        'Semana 2': {'Lunes': 28, 'Martes': 30, 'Miércoles': 28, 'Jueves': 25, 'Viernes': 22, 'Sábado': 20, 'Domingo': 18},
        'Semana 3': {'Lunes': 30, 'Martes': 28, 'Miércoles': 25, 'Jueves': 22, 'Viernes': 20, 'Sábado': 18, 'Domingo': 15},
        'Semana 4': {'Lunes': 28, 'Martes': 25, 'Miércoles': 22, 'Jueves': 20, 'Viernes': 18, 'Sábado': 15, 'Domingo': 12}
    },
    'Cuenca': {
        'Semana 1': {'Lunes': 18, 'Martes': 20, 'Miércoles': 22, 'Jueves': 20, 'Viernes': 18, 'Sábado': 15, 'Domingo': 12},
        'Semana 2': {'Lunes': 20, 'Martes': 22, 'Miércoles': 20, 'Jueves': 18, 'Viernes': 15, 'Sábado': 12, 'Domingo': 10},
        'Semana 3': {'Lunes': 22, 'Martes': 20, 'Miércoles': 18, 'Jueves': 15, 'Viernes': 12, 'Sábado': 10, 'Domingo': 8},
        'Semana 4': {'Lunes': 20, 'Martes': 18, 'Miércoles': 15, 'Jueves': 12, 'Viernes': 10, 'Sábado': 8, 'Domingo': 5}
    }
}

# Función para calcular el promedio de temperaturas para cada ciudad
def calcular_promedio(temperaturas):
    promedios = {}
    for ciudad, semanas in temperaturas.items():
        total = 0
        cantidad_dias = 0
        for semana, dias in semanas.items():
            for temperatura in dias.values():
                total += temperatura
                cantidad_dias += 1
        promedio = total / cantidad_dias
        promedios[ciudad] = promedio
    return promedios

# Calcular y mostrar los promedios de temperaturas para cada ciudad
promedios = calcular_promedio(temperaturas)
for ciudad, promedio in promedios.items():
    print(f'La temperatura promedio en {ciudad} es de {promedio:.2f}°C')
