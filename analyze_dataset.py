import pandas as pd

# Carga el archivo CSV
# Reemplaza 'dataset.csv' con el nombre real del archivo que descargaste
df = pd.read_csv('hotaling_cocktails - Cocktails.csv')

# Muestra las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Resumen del dataset
print("\nInformación del dataset:")
print(df.info())

# Estadísticas básicas
print("\nEstadísticas descriptivas:")
print(df.describe())
