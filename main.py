import pandas as pd

# Nombre del archivo CSV
NAME_CSV = 'Coloca el nombre aquí'

# Datos para el DataFrame df2
data = {
    'Ubicación': [
        'Depósito Cochabamba',
        'Oficina de Ventas Cochabamba',
        'Depósito La Paz B',
        'Oficina De Ventas La Paz',
        'Depósito Einhell',
        'Oficina de Ventas Santa Cruz',
        'Tienda Einhell'
    ],
    'Número de depósitos': [
        'PTA-DE-CB-1',
        'PTA-OV-CB-1',
        'PTA-DE-AC-1',
        'PTA-SV-AC-1',
        'PTA-DE-LB-1',
        'PTA-OV-LB-1',
        'PTA-SV-LB-1'
    ],
    'Preferido': [
        'T',
        'T',
        'T',
        'T',
        'T',
        'T',
        'T'
    ]
}

# Crear el DataFrame df2
df2 = pd.DataFrame(data)

# Suponiendo que df1 es un DataFrame que leerás desde un archivo CSV
df1 = pd.read_csv(f'{NAME_CSV}.csv')


# key temporal para hacer el merge
df1['key'] = 1
df2['key'] = 1

# Combinar los dos DataFrames
df_combinado = pd.merge(df1, df2, on='key').drop('key', axis=1)

# Si necesitas exportar el DataFrame combinado a un archivo CSV
df_combinado.to_csv('tabla_combinada.csv', index=False, encoding='latin1', sep=';')

print(df_combinado)
