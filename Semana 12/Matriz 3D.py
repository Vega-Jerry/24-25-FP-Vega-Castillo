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

# Imprimir la información para cada ciudad
for ciudad in ciudades:
    print(f'{ciudad}:')
    for semana in temperaturas[ciudad]:
        print(f'  {semana}:')
        temperaturas_semana = []
        for dia, temperatura in temperaturas[ciudad][semana].items():
            print(f'    {dia}: {temperatura}°C')
            temperaturas_semana.append(temperatura)
        promedio_semana = sum(temperaturas_semana) / len(temperaturas_semana)
        print(f'    Promedio de temperatura de la semana: {promedio_semana:.2f}°C')
    print()

