# Workflows del Proyecto

## Workflow 1: Clonar el repositorio

### Objetivo

Obtener una copia local del proyecto.

### Requisitos

- Git instalado.
- Visual Studio Code instalado.
- Python 3.14.5 instalado.

### Pasos

1. Abrir una terminal.

2. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

3. Ingresar a la carpeta del proyecto:

```bash
cd "Trabajo final fundamentos ciencias de datos"
```

4. Abrir el proyecto en Visual Studio Code:

```bash
code .
```

### Resultado esperado

El proyecto queda disponible localmente con todos sus archivos.

---

## Workflow 2: Configuración y programación

### Objetivo

Preparar el entorno para desarrollar y modificar el proyecto.

### Pasos

#### 1. Seleccionar el intérprete de Python

En Visual Studio Code:

- Ctrl + Shift + P
- Python: Select Interpreter

Seleccionar:

```text
C:\Users\Usuario\AppData\Local\Python\pythoncore-3.14-64\python.exe
```

#### 2. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

#### 3. Verificar instalación

```bash
python -m pip list
```

#### 4. Modificar código

Archivo principal:

```text
Main.py
```

Archivos de documentación:

```text
README.md
DATABASE.md
WORKFLOWS.md
```

#### 5. Guardar cambios

Guardar los cambios realizados en el proyecto.

### Resultado esperado

El entorno queda listo para desarrollar nuevas funcionalidades y análisis.

---

## Workflow 3: Ejecución del proyecto

### Objetivo

Ejecutar el análisis completo de los datos académicos.

### Requisitos

- Dependencias instaladas.
- Archivo Notas 10.xlsx disponible en la carpeta raíz.

### Pasos

#### 1. Abrir terminal

Ubicarse en la carpeta del proyecto.

#### 2. Verificar ubicación

```bash
pwd
```

Debe mostrar:

```text
Trabajo final fundamentos ciencias de datos
```

#### 3. Ejecutar el programa

```bash
python Main.py
```

#### 4. Procesos realizados automáticamente

El programa:

1. Carga el archivo Excel.
2. Verifica dimensiones y variables.
3. Genera estadísticas descriptivas.
4. Calcula el promedio académico.
5. Identifica la especialidad técnica.
6. Genera visualizaciones.
7. Ejecuta ANOVA.
8. Ejecuta Kruskal-Wallis.
9. Genera resultados para interpretación.

### Resultado esperado

Obtención de resultados estadísticos sobre el rendimiento académico de los estudiantes según la especialidad técnica.

---

## Resumen General

```text
Clonar repositorio
        ↓
Abrir proyecto
        ↓
Configurar Python
        ↓
Instalar dependencias
        ↓
Programar / Modificar código
        ↓
Ejecutar Main.py
        ↓
Generar análisis estadístico
        ↓
Interpretar resultados
```
## Workflow 4: Actualización del repositorio

### Guardar cambios

```bash
git add .
git commit -m "Actualización del análisis"
git push
```

### Resultado esperado

Los cambios quedan almacenados en GitHub.