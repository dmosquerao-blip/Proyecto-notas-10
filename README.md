# Análisis del Rendimiento Académico según la Especialidad Técnica

## Descripción del proyecto

Este proyecto tiene como objetivo analizar si existen diferencias significativas en el rendimiento académico de los estudiantes de grado décimo según la especialidad técnica cursada.

La base de datos contiene las calificaciones de 197 estudiantes en diferentes asignaturas académicas, así como la especialidad técnica a la que pertenece cada estudiante.

## Objetivo general

Determinar si la especialidad técnica cursada por los estudiantes influye significativamente en su rendimiento académico promedio.

## Objetivos específicos

* Calcular el promedio académico general de cada estudiante.
* Realizar un análisis descriptivo de las calificaciones.
* Comparar los promedios académicos entre las diferentes especialidades técnicas.
* Aplicar pruebas estadísticas para evaluar diferencias significativas entre grupos.
* Construir modelos de estimación para analizar la relación entre la especialidad técnica y el rendimiento académico.

## Base de datos

La información se encuentra en el archivo:

text
Notas 10.xlsx


La base contiene:

* Identificador del estudiante.
* Nombre del estudiante.
* Calificaciones de las asignaturas.
* Especialidad técnica codificada mediante variables binarias (One-Hot Encoding).

## Especialidades técnicas analizadas

* Electricidad
* Electrónica
* Electromecánica
* Diseño corte y confección
* Soldadura
* Ebanistería
* Diseño arquitectónico
* Mecánica

## Metodología

### 1. Carga y exploración de datos

* Lectura del archivo Excel mediante Pandas.
* Verificación de tipos de datos.
* Identificación de variables académicas y técnicas.

### 2. Construcción de variables

* Cálculo del promedio académico general para cada estudiante.
* Identificación de la especialidad técnica correspondiente.

### 3. Análisis descriptivo

* Estadísticas descriptivas.
* Distribuciones por técnica.
* Visualización mediante diagramas de caja (boxplots).

### 4. Análisis inferencial

* Prueba ANOVA
* Verificación de supuestos estadísticos.
* Comparación de grupos mediante pruebas no paramétricas (Kruskal-Wallis).


## Herramientas utilizadas

* Python 3.14.5
* Pandas
* NumPy
* SciPy
* Matplotlib
* Seaborn
* Scikit-Learn

## Estructura del proyecto

text
Trabajo final fundamentos ciencias de datos/
│
├── Main.py
├── Notas 10.xlsx
├── README.md
├── DATABASE.md
├── WORKFLOWS.md
├── requirements.txt
├── .gitignore
├── .env.example
└── Trabajo final fcd.code-workspace


## Ejecución

Instalar dependencias:

bash
python -m pip install -r requirements.txt


Ejecutar el proyecto:

bash
python Main.py


## Tipo de proyecto

Este trabajo corresponde principalmente a un problema de estimación, ya que busca analizar y modelar una variable cuantitativa continua (el promedio académico de los estudiantes) a partir de variables explicativas asociadas a la especialidad técnica cursada.

