# Diccionario de Datos

## Descripción general

La base de datos contiene información académica de 197 estudiantes de grado décimo.

El objetivo de la base es analizar la relación entre la especialidad técnica cursada y el rendimiento académico de los estudiantes.

Archivo fuente:

```text
Notas 10.xlsx
```

Número de registros:

```text
197 estudiantes
```

Número de variables originales:

```text
22 columnas
```

---

# Descripción de variables

| Variable | Descripción | Tipo |
|-----------|------------|------|
| Column1 | Identificador del estudiante | Numérica |
| Column2 | Nombre completo del estudiante | Texto |
| LENG | Calificación de Lengua Castellana | Numérica |
| TRIG | Calificación de Trigonometría | Numérica |
| BIOLO | Calificación de Biología | Numérica |
| FISI | Calificación de Física | Numérica |
| QUIM | Calificación de Química | Numérica |
| FILO | Calificación de Filosofía | Numérica |
| CPOL | Calificación de Ciencias Políticas | Numérica |
| INGL | Calificación de Inglés | Numérica |
| EFIS | Calificación de Educación Física | Numérica |
| REL | Calificación de Religión | Numérica |
| EYV | Calificación de Ética y Valores | Numérica |
| INFO | Calificación de Informática | Numérica |

---

# Variables de especialidad técnica

Las siguientes variables fueron codificadas mediante One-Hot Encoding.

Cada estudiante pertenece a una única especialidad técnica.

Los valores posibles son:

- 1 = Pertenece a la especialidad.
- 0 = No pertenece a la especialidad.

| Variable | Descripción |
|-----------|------------|
| Electricidad | Especialidad de Electricidad |
| Electronica | Especialidad de Electrónica |
| Electromecanica | Especialidad de Electromecánica |
| Diseño corte y confeccion | Especialidad de Diseño Corte y Confección |
| Soldadura | Especialidad de Soldadura |
| Ebanisteria | Especialidad de Ebanistería |
| Diseño arquitectonico | Especialidad de Diseño Arquitectónico |
| Mecanica | Especialidad de Mecánica |

---

# Variables derivadas

Durante el análisis se construyen variables adicionales.

## Promedio

Corresponde al promedio de las asignaturas académicas del estudiante.

Se calcula mediante:

Promedio = promedio(LENG, TRIG, BIOLO, FISI, QUIM, FILO, CPOL, INGL, EFIS, REL, EYV, INFO)

Tipo:

```text
Numérica continua
```

---

## Tecnica

Variable categórica creada a partir de las columnas One-Hot Encoding.

Representa la especialidad técnica a la que pertenece cada estudiante.

Valores posibles:

- Electricidad
- Electrónica
- Electromecánica
- Diseño Corte y Confección
- Soldadura
- Ebanistería
- Diseño Arquitectónico
- Mecánica

Tipo:

```text
Categórica nominal
```

---

# Calidad de los datos

La base de datos presenta:

- 197 registros válidos.
- No se identificaron valores faltantes.
- Todas las calificaciones son numéricas.
- Las variables técnicas están correctamente codificadas.

---

# Uso en el proyecto

Esta base será utilizada para:

1. Análisis descriptivo.
2. Visualización de distribuciones.
3. Comparación de grupos académicos.
4. Prueba ANOVA.
5. Prueba Kruskal-Wallis.
6. Modelos de estimación mediante regresión lineal.

