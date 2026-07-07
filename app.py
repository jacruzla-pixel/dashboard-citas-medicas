# 1. INSTALAR LIBRERÍAS (solo la primera vez)
# !pip install faker

# 2. IMPORTAR LIBRERÍAS
import pandas as pd
import numpy as np
from faker import Faker

# 3. CONFIGURAR FAKER EN ESPAÑOL
fake = Faker('es_ES')

# 4. GENERAR LOS 5000 REGISTROS
n = 5000

categorias_riesgo = ['Bajo', 'Moderado', 'Alto', 'Crítico']
estados = ['Atendido', 'En seguimiento', 'Pendiente', 'Finalizado']

datos = []

for i in range(n):

    riesgo = np.random.choice(
        categorias_riesgo,
        p=[0.35, 0.35, 0.20, 0.10]
    )

    # Puntaje de estrés según el riesgo
    if riesgo == 'Bajo':
        puntaje = np.random.randint(10, 36)
    elif riesgo == 'Moderado':
        puntaje = np.random.randint(36, 66)
    elif riesgo == 'Alto':
        puntaje = np.random.randint(66, 86)
    else:
        puntaje = np.random.randint(86, 101)

    datos.append([
        i + 1,
        fake.date_between('-1y', 'today'),
        riesgo,
        np.random.choice(estados),
        puntaje
    ])

# 5. CREAR EL DATAFRAME Y EXPORTAR A CSV
df = pd.DataFrame(
    datos,
    columns=[
        'id',
        'fecha',
        'categoria_riesgo',
        'estado_seguimiento',
        'puntaje_estres'
    ]
)

df.to_csv('salud_mental.csv', index=False)

# 6. MOSTRAR LAS PRIMERAS FILAS PARA VERIFICAR
df.head()
