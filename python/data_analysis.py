# Importar librerías necesarias para análisis de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

# Configurar estilo de gráficos
plt.style.use('seaborn')
sns.set_palette("husl")

class DataAnalyzer:
    """Clase para realizar análisis de datos con pandas y matplotlib"""
    
    def __init__(self):
        self.data = None
    
    # Crear función para leer datos desde un archivo CSV
    def load_data_from_csv(self, file_path):
        """Carga datos desde un archivo CSV"""
        try:
            self.data = pd.read_csv(file_path)
            print(f"Datos cargados exitosamente: {self.data.shape[0]} filas, {self.data.shape[1]} columnas")
            return self.data
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {file_path}")
            return None
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return None
    
    # Función para generar datos de ejemplo
    def generate_sample_data(self, num_records=1000):
        """Genera datos de ejemplo para demostración"""
        np.random.seed(42)
        
        # Generar datos de ventas ficticios
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        
        data = []
        products = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Tablet']
        categories = ['Electrónicos', 'Accesorios', 'Computadoras']
        
        for i in range(num_records):
            record = {
                'fecha': np.random.choice(dates),
                'producto': np.random.choice(products),
                'categoria': np.random.choice(categories),
                'precio': np.random.uniform(50, 2000),
                'cantidad': np.random.randint(1, 10),
                'descuento': np.random.uniform(0, 0.3),
                'cliente_edad': np.random.randint(18, 80),
                'cliente_genero': np.random.choice(['M', 'F'])
            }
            record['total'] = record['precio'] * record['cantidad'] * (1 - record['descuento'])
            data.append(record)
        
        self.data = pd.DataFrame(data)
        print(f"Datos de ejemplo generados: {len(data)} registros")
        return self.data
    
    # Función para calcular estadísticas básicas de un dataset
    def calculate_basic_statistics(self):
        """Calcula y muestra estadísticas básicas del dataset"""
        if self.data is None:
            print("No hay datos cargados")
            return None
        
        print("=== ESTADÍSTICAS BÁSICAS ===")
        print(f"Dimensiones del dataset: {self.data.shape}")
        print(f"Tipos de datos:\n{self.data.dtypes}")
        print(f"\nValores nulos por columna:\n{self.data.isnull().sum()}")
        print(f"\nEstadísticas descriptivas:\n{self.data.describe()}")
        
        # Estadísticas específicas para columnas numéricas
        numeric_columns = self.data.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            print(f"\n--- {col.upper()} ---")
            print(f"Media: {self.data[col].mean():.2f}")
            print(f"Mediana: {self.data[col].median():.2f}")
            print(f"Desviación estándar: {self.data[col].std():.2f}")
            print(f"Rango: {self.data[col].max() - self.data[col].min():.2f}")
        
        return self.data.describe()
    
    # Función para crear gráficos de los datos
    def create_data_visualizations(self):
        """Crea diferentes tipos de visualizaciones de los datos"""
        if self.data is None:
            print("No hay datos cargados")
            return
        
        # Configurar subplots
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Análisis Visual de Datos de Ventas', fontsize=16, fontweight='bold')
        
        # 1. Crear gráfico de barras para mostrar ventas por producto
        product_sales = self.data.groupby('producto')['total'].sum().sort_values(ascending=False)
        axes[0, 0].bar(product_sales.index, product_sales.values, color='skyblue')
        axes[0, 0].set_title('Ventas Totales por Producto')
        axes[0, 0].set_xlabel('Producto')
        axes[0, 0].set_ylabel('Ventas ($)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # 2. Crear histograma de distribución de edades
        axes[0, 1].hist(self.data['cliente_edad'], bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
        axes[0, 1].set_title('Distribución de Edades de Clientes')
        axes[0, 1].set_xlabel('Edad')
        axes[0, 1].set_ylabel('Frecuencia')
        
        # 3. Gráfico de dispersión precio vs cantidad
        axes[0, 2].scatter(self.data['precio'], self.data['cantidad'], alpha=0.6, color='coral')
        axes[0, 2].set_title('Relación Precio vs Cantidad')
        axes[0, 2].set_xlabel('Precio ($)')
        axes[0, 2].set_ylabel('Cantidad')
        
        # 4. Gráfico de líneas de ventas por mes
        self.data['fecha'] = pd.to_datetime(self.data['fecha'])
        monthly_sales = self.data.groupby(self.data['fecha'].dt.to_period('M'))['total'].sum()
        axes[1, 0].plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', color='purple')
        axes[1, 0].set_title('Ventas Mensuales')
        axes[1, 0].set_xlabel('Mes')
        axes[1, 0].set_ylabel('Ventas ($)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 5. Gráfico de torta para distribución por categoría
        category_distribution = self.data['categoria'].value_counts()
        axes[1, 1].pie(category_distribution.values, labels=category_distribution.index, autopct='%1.1f%%')
        axes[1, 1].set_title('Distribución por Categoría')
        
        # 6. Boxplot de precios por categoría
        categories = self.data['categoria'].unique()
        price_data = [self.data[self.data['categoria'] == cat]['precio'] for cat in categories]
        box_plot = axes[1, 2].boxplot(price_data, labels=categories, patch_artist=True)
        axes[1, 2].set_title('Distribución de Precios por Categoría')
        axes[1, 2].set_xlabel('Categoría')
        axes[1, 2].set_ylabel('Precio ($)')
        
        # Colorear los boxplots
        colors = ['lightblue', 'lightgreen', 'lightcoral']
        for patch, color in zip(box_plot['boxes'], colors):
            patch.set_facecolor(color)
        
        plt.tight_layout()
        plt.show()
    
    # Función para análisis de correlación
    def analyze_correlations(self):
        """Analiza correlaciones entre variables numéricas"""
        if self.data is None:
            print("No hay datos cargados")
            return
        
        # Seleccionar solo columnas numéricas
        numeric_data = self.data.select_dtypes(include=[np.number])
        
        # Calcular matriz de correlación
        correlation_matrix = numeric_data.corr()
        
        # Crear heatmap de correlaciones
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                   square=True, linewidths=0.5)
        plt.title('Matriz de Correlación', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
        
        print("=== ANÁLISIS DE CORRELACIONES ===")
        print(correlation_matrix)
        
        return correlation_matrix
    
    # Función para detectar valores atípicos
    def detect_outliers(self, column_name):
        """Detecta valores atípicos usando el método IQR"""
        if self.data is None or column_name not in self.data.columns:
            print(f"Columna '{column_name}' no encontrada")
            return None
        
        Q1 = self.data[column_name].quantile(0.25)
        Q3 = self.data[column_name].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = self.data[(self.data[column_name] < lower_bound) | 
                           (self.data[column_name] > upper_bound)]
        
        print(f"=== DETECCIÓN DE VALORES ATÍPICOS EN '{column_name}' ===")
        print(f"Q1: {Q1:.2f}")
        print(f"Q3: {Q3:.2f}")
        print(f"IQR: {IQR:.2f}")
        print(f"Límite inferior: {lower_bound:.2f}")
        print(f"Límite superior: {upper_bound:.2f}")
        print(f"Número de valores atípicos: {len(outliers)}")
        
        if len(outliers) > 0:
            print(f"Porcentaje de valores atípicos: {len(outliers)/len(self.data)*100:.2f}%")
        
        return outliers

# Función principal para demostrar el análisis de datos
def main():
    """Función principal que demuestra todas las capacidades del analizador"""
    print("=== DEMO: ANÁLISIS DE DATOS CON GITHUB COPILOT ===\n")
    
    # Crear instancia del analizador
    analyzer = DataAnalyzer()
    
    # Generar datos de ejemplo
    print("1. Generando datos de ejemplo...")
    analyzer.generate_sample_data(1000)
    
    # Mostrar primeras filas
    print("\n2. Primeras 5 filas del dataset:")
    print(analyzer.data.head())
    
    # Calcular estadísticas básicas
    print("\n3. Calculando estadísticas básicas...")
    analyzer.calculate_basic_statistics()
    
    # Crear visualizaciones
    print("\n4. Creando visualizaciones...")
    analyzer.create_data_visualizations()
    
    # Analizar correlaciones
    print("\n5. Analizando correlaciones...")
    analyzer.analyze_correlations()
    
    # Detectar valores atípicos
    print("\n6. Detectando valores atípicos en precios...")
    outliers = analyzer.detect_outliers('precio')
    if len(outliers) > 0:
        print(f"Ejemplos de valores atípicos:\n{outliers[['producto', 'precio']].head()}")

if __name__ == "__main__":
    main()