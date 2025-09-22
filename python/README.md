# Ejemplos de GitHub Copilot para Python

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con Python.

## 📚 Contenido

1. [Ejemplo Básico: Análisis de Datos](#ejemplo-1-análisis-de-datos)
2. [Ejemplo Intermedio: API REST con Flask](#ejemplo-2-api-rest-con-flask)
3. [Ejemplo Avanzado: Machine Learning](#ejemplo-3-machine-learning-básico)

## Prerequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Visual Studio Code con extensión de Python
- GitHub Copilot habilitado

```bash
# Instalar dependencias
pip install flask pandas numpy scikit-learn matplotlib requests
```

## 📊 Ejemplo 1: Análisis de Datos

### Objetivo
Crear scripts para análisis de datos usando pandas y matplotlib con ayuda de GitHub Copilot.

### Instrucciones paso a paso

1. **Crea un nuevo archivo**: `data_analysis.py`
2. **Escribe comentarios descriptivos** para que Copilot genere el código:

```python
# Importar librerías necesarias para análisis de datos
# Crear función para leer datos desde un archivo CSV
# Función para calcular estadísticas básicas de un dataset
# Función para crear gráficos de los datos
```

### 💡 Tips para este ejemplo
- Usa comentarios específicos como "# Crear gráfico de barras para mostrar ventas por mes"
- Copilot puede generar código complejo de pandas con una descripción clara
- Prueba describir visualizaciones: "# Crear histograma de distribución de edades"

---

## 🌐 Ejemplo 2: API REST con Flask

### Objetivo
Crear una API REST simple para gestionar libros usando Flask y demostrar el uso de decoradores, rutas y JSON.

### Instrucciones paso a paso

1. **Crea la aplicación Flask**:
```python
# Crear aplicación Flask para gestionar una biblioteca de libros
# Definir modelo de datos para libros con id, titulo, autor, año
```

2. **Define las rutas de la API**:
```python
# Ruta GET para obtener todos los libros
# Ruta GET para obtener un libro por ID
# Ruta POST para crear un nuevo libro
# Ruta PUT para actualizar un libro existente
# Ruta DELETE para eliminar un libro
```

3. **Añade validaciones**:
```python
# Función para validar datos de entrada de libro
# Manejo de errores y códigos de estado HTTP
```

### 🔧 Funcionalidades a implementar
- CRUD completo para libros
- Validación de datos de entrada
- Manejo de errores HTTP
- Documentación de endpoints
- Búsqueda de libros por autor o título

---

## 🤖 Ejemplo 3: Machine Learning Básico

### Objetivo
Crear un sistema de predicción simple usando scikit-learn, demostrando clasificación y regresión.

### Instrucciones paso a paso

1. **Preparación de datos**:
```python
# Cargar dataset de ejemplo (iris o boston housing)
# Función para limpiar y preparar datos
# Dividir datos en entrenamiento y prueba
```

2. **Entrenamiento de modelos**:
```python
# Crear modelo de clasificación con RandomForest
# Crear modelo de regresión lineal
# Entrenar modelos con datos de entrenamiento
```

3. **Evaluación y predicción**:
```python
# Evaluar precisión de modelos
# Función para hacer predicciones con nuevos datos
# Crear visualizaciones de resultados
```

### 📊 Algoritmos a explorar
- Clasificación: Random Forest, SVM, K-Nearest Neighbors
- Regresión: Linear Regression, Polynomial Regression
- Clustering: K-Means
- Métricas: Accuracy, Precision, Recall, F1-Score

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **Web Scraping**
   ```python
   # Crear scraper para extraer datos de sitios web usando BeautifulSoup
   ```

2. **Procesamiento de Imágenes**
   ```python
   # Procesar imágenes usando OpenCV para detección de objetos
   ```

3. **Base de Datos**
   ```python
   # Conectar con SQLite y realizar operaciones CRUD usando SQLAlchemy
   ```

4. **Testing**
   ```python
   # Crear tests unitarios usando pytest para validar funciones
   ```

5. **Automatización**
   ```python
   # Crear scripts de automatización para tareas repetitivas del sistema
   ```

## 💡 Tips específicos para Python y Copilot

1. **Docstrings descriptivos**: Usa docstrings para que Copilot entienda mejor la función
2. **Type hints**: Incluye type hints para mejores sugerencias
3. **Imports específicos**: Menciona las librerías que quieres usar
4. **Patrones Pythónicos**: Describe el uso de list comprehensions, decoradores, etc.
5. **Manejo de errores**: Especifica qué tipo de errores manejar

### Ejemplos de comentarios efectivos:
```python
# Función que recibe una lista de números y retorna solo los pares usando list comprehension
# Decorador para medir el tiempo de ejecución de una función
# Clase que implementa el patrón Singleton para conexión a base de datos
# Función async que hace peticiones HTTP concurrentes usando aiohttp
```

---

¡Explora cada ejemplo y experimenta con diferentes comentarios para descubrir todo lo que Python y Copilot pueden hacer juntos! 🐍✨