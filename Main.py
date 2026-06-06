import pandas as pd

# Cargar datos
df = pd.read_excel("Notas 10.xlsx")

# Información general
print("Dimensiones del dataset:")
print(df.shape)

print("\nColumnas:")
print(df.columns)

print("\nPrimeras 5 filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print(df.columns.tolist())

# Materias académicas
materias = [
    'LENG ', 'TRIG', 'BIOLO', 'FISI', 'QUIM ',
    'FILO ', 'CPOL ', 'INGL ', 'EFIS ', 'REL ',
    'EYV ', 'INFO '
]

# Promedio general por estudiante
df['Promedio_General'] = df[materias].mean(axis=1)

# Columnas de técnicas
tecnicas = [
    'Electricidad ',
    'Electronica',
    'Electromecanica',
    'Diseño corte y confeccion',
    'Soldadura ',
    'Ebanisteria',
    'Diseño arquitectonico',
    'Mecanica'
]

# Convertir One-Hot a una sola columna categórica
df['Tecnica'] = df[tecnicas].idxmax(axis=1)

conteo_tecnicas = df['Tecnica'].value_counts()

print(conteo_tecnicas)

# Estadística descriptiva por técnica
estadisticas = df.groupby('Tecnica')['Promedio_General'].agg([
    'count',
    'mean',
    'median',
    'std',
    'min',
    'max'
]).round(3)

# Renombrar columnas
estadisticas.columns = [
    'N',
    'Media',
    'Mediana',
    'Desv_Estandar',
    'Minimo',
    'Maximo'
]

print(estadisticas)

#Gráfico de cajas
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df,
    x='Tecnica',
    y='Promedio_General'
)

plt.xticks(rotation=45)
plt.title('Distribución del promedio general por técnica')
plt.xlabel('Técnica')
plt.ylabel('Promedio General')

plt.show()
# Cantidad de estudiantes por técnica
print(df[tecnicas].sum())

# Promedio de las materias
df['Promedio_General'] = df[materias].mean(axis=1)

# Técnica de cada estudiante
df['Tecnica'] = df[tecnicas].idxmax(axis=1)

# Estadísticas descriptivas
print(
    df.groupby('Tecnica')['Promedio_General']
      .describe()
      .round(3)
)
# Promedio por estudiante
df['Promedio_General'] = df[materias].mean(axis=1)
from scipy.stats import f_oneway

# Crear un grupo de notas por técnica
grupos = [
    df[df['Tecnica'] == tecnica]['Promedio_General']
    for tecnica in df['Tecnica'].unique()
]

# ANOVA
F, p = f_oneway(*grupos)

print(f"Estadístico F: {F:.4f}")
print(f"Valor p: {p:.6f}")

#Interpretación
alpha = 0.05

if p < alpha:
    print("\nSe rechaza H0")
    print("Existen diferencias significativas entre al menos dos técnicas.")
else:
    print("\nNo se rechaza H0")
    print("No existen diferencias significativas entre las técnicas.")

# Validar supuestos de ANOVA  
from scipy.stats import shapiro

for tecnica in df['Tecnica'].unique():
    grupo = df[df['Tecnica'] == tecnica]['Promedio_General']

    stat, p_val = shapiro(grupo)

    print(f"\n{tecnica}")
    print(f"p = {p_val:.4f}")

    from scipy.stats import levene

grupos = [
    df[df['Tecnica'] == tecnica]['Promedio_General']
    for tecnica in df['Tecnica'].unique()
]

stat, p = levene(*grupos)

print("Prueba de Levene")
print(f"p = {p:.4f}")

from scipy.stats import kruskal

# Crear los grupos
grupos = [
    df[df['Tecnica'] == tecnica]['Promedio_General']
    for tecnica in df['Tecnica'].unique()
]

# Prueba de Kruskal-Wallis
H, p = kruskal(*grupos)

print(f"Estadístico H: {H:.4f}")
print(f"Valor p: {p:.6f}")

# Interpretación
alpha = 0.05

if p < alpha:
    print("\nSe rechaza H0")
    print("Existen diferencias significativas entre al menos dos técnicas.")
else:
    print("\nNo se rechaza H0")
    print("No existen diferencias significativas entre las técnicas.")

    # Resultados de Kruskal-Wallis
H = 11.0188
