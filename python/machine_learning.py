# Cargar dataset de ejemplo (iris o boston housing)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_boston, make_classification
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

class MLTutorial:
    """Clase para demostrar conceptos básicos de Machine Learning con GitHub Copilot"""
    
    def __init__(self):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.models = {}
        self.predictions = {}
        self.scaler = StandardScaler()
    
    # Función para limpiar y preparar datos
    def load_and_prepare_data(self, dataset_type='iris'):
        """Carga y prepara datos para machine learning"""
        print(f"🔄 Cargando dataset: {dataset_type}")
        
        if dataset_type == 'iris':
            # Cargar dataset de clasificación Iris
            data = load_iris()
            self.X = pd.DataFrame(data.data, columns=data.feature_names)
            self.y = pd.Series(data.target)
            self.target_names = data.target_names
            self.problem_type = 'classification'
            
        elif dataset_type == 'boston':
            # Cargar dataset de regresión Boston Housing
            data = load_boston()
            self.X = pd.DataFrame(data.data, columns=data.feature_names)
            self.y = pd.Series(data.target)
            self.problem_type = 'regression'
            
        elif dataset_type == 'synthetic':
            # Crear dataset sintético para clasificación
            X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, 
                                     n_redundant=10, n_classes=3, random_state=42)
            self.X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
            self.y = pd.Series(y)
            self.problem_type = 'classification'
        
        print(f"✅ Dataset cargado: {self.X.shape[0]} muestras, {self.X.shape[1]} características")
        print(f"📊 Tipo de problema: {self.problem_type}")
        
        # Mostrar información básica del dataset
        self.explore_data()
        
        return self.X, self.y
    
    def explore_data(self):
        """Explora y muestra información básica del dataset"""
        print("\n=== EXPLORACIÓN DE DATOS ===")
        print(f"Dimensiones: {self.X.shape}")
        print(f"Tipos de datos:\n{self.X.dtypes}")
        print(f"Valores nulos: {self.X.isnull().sum().sum()}")
        
        if self.problem_type == 'classification':
            print(f"Distribución de clases:\n{self.y.value_counts()}")
        else:
            print(f"Estadísticas de la variable objetivo:\n{self.y.describe()}")
        
        # Mostrar primeras filas
        print(f"\nPrimeras 5 filas:")
        combined_data = self.X.copy()
        combined_data['target'] = self.y
        print(combined_data.head())
    
    # Dividir datos en entrenamiento y prueba
    def split_data(self, test_size=0.2, random_state=42):
        """Divide los datos en conjuntos de entrenamiento y prueba"""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, 
            stratify=self.y if self.problem_type == 'classification' else None
        )
        
        print(f"\n📊 División de datos completada:")
        print(f"  Entrenamiento: {self.X_train.shape[0]} muestras")
        print(f"  Prueba: {self.X_test.shape[0]} muestras")
        
        # Escalar características si es necesario
        if self.problem_type == 'regression' or 'boston' in str(type(self.X)):
            self.X_train_scaled = self.scaler.fit_transform(self.X_train)
            self.X_test_scaled = self.scaler.transform(self.X_test)
            print("✅ Escalado de características aplicado")
        
        return self.X_train, self.X_test, self.y_train, self.y_test
    
    # Crear modelo de clasificación con RandomForest
    def create_classification_models(self):
        """Crea y entrena modelos de clasificación"""
        if self.problem_type != 'classification':
            print("❌ Este método solo funciona con problemas de clasificación")
            return
        
        print("\n🤖 Entrenando modelos de clasificación...")
        
        # Random Forest Classifier
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(self.X_train, self.y_train)
        self.models['RandomForest'] = rf_model
        
        # Support Vector Machine
        svm_model = SVC(kernel='rbf', random_state=42)
        svm_model.fit(self.X_train, self.y_train)
        self.models['SVM'] = svm_model
        
        # K-Nearest Neighbors
        knn_model = KNeighborsClassifier(n_neighbors=5)
        knn_model.fit(self.X_train, self.y_train)
        self.models['KNN'] = knn_model
        
        # Logistic Regression
        lr_model = LogisticRegression(random_state=42, max_iter=1000)
        lr_model.fit(self.X_train, self.y_train)
        self.models['LogisticRegression'] = lr_model
        
        print(f"✅ {len(self.models)} modelos entrenados")
        return self.models
    
    # Crear modelo de regresión lineal
    def create_regression_models(self):
        """Crea y entrena modelos de regresión"""
        if self.problem_type != 'regression':
            print("❌ Este método solo funciona con problemas de regresión")
            return
        
        print("\n🤖 Entrenando modelos de regresión...")
        
        # Linear Regression
        lr_model = LinearRegression()
        lr_model.fit(self.X_train_scaled, self.y_train)
        self.models['LinearRegression'] = lr_model
        
        # Random Forest Regressor
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_model.fit(self.X_train, self.y_train)
        self.models['RandomForestRegressor'] = rf_model
        
        print(f"✅ {len(self.models)} modelos entrenados")
        return self.models
    
    # Evaluar precisión de modelos
    def evaluate_models(self):
        """Evalúa el rendimiento de los modelos entrenados"""
        print(f"\n📊 EVALUACIÓN DE MODELOS ({self.problem_type.upper()})")
        print("=" * 50)
        
        for model_name, model in self.models.items():
            if self.problem_type == 'classification':
                # Usar datos originales para la mayoría de modelos
                X_test_to_use = self.X_test
                if model_name == 'LogisticRegression':
                    # Para regresión logística, usar datos escalados si están disponibles
                    X_test_to_use = getattr(self, 'X_test_scaled', self.X_test)
                
                y_pred = model.predict(X_test_to_use)
                self.predictions[model_name] = y_pred
                
                accuracy = accuracy_score(self.y_test, y_pred)
                precision = precision_score(self.y_test, y_pred, average='weighted')
                recall = recall_score(self.y_test, y_pred, average='weighted')
                f1 = f1_score(self.y_test, y_pred, average='weighted')
                
                print(f"\n🎯 {model_name}:")
                print(f"  Precisión: {accuracy:.4f}")
                print(f"  Precision: {precision:.4f}")
                print(f"  Recall: {recall:.4f}")
                print(f"  F1-Score: {f1:.4f}")
                
            else:  # regression
                # Usar datos escalados para modelos que los necesiten
                X_test_to_use = self.X_test_scaled if model_name == 'LinearRegression' else self.X_test
                
                y_pred = model.predict(X_test_to_use)
                self.predictions[model_name] = y_pred
                
                mse = mean_squared_error(self.y_test, y_pred)
                rmse = np.sqrt(mse)
                r2 = r2_score(self.y_test, y_pred)
                
                print(f"\n🎯 {model_name}:")
                print(f"  MSE: {mse:.4f}")
                print(f"  RMSE: {rmse:.4f}")
                print(f"  R²: {r2:.4f}")
    
    # Función para hacer predicciones con nuevos datos
    def make_predictions(self, new_data, model_name='RandomForest'):
        """Hace predicciones con nuevos datos usando un modelo específico"""
        if model_name not in self.models:
            print(f"❌ Modelo '{model_name}' no encontrado")
            return None
        
        model = self.models[model_name]
        
        # Preparar datos según el tipo de modelo
        if isinstance(new_data, pd.DataFrame):
            data_to_predict = new_data
        else:
            data_to_predict = pd.DataFrame([new_data], columns=self.X.columns)
        
        # Aplicar escalado si es necesario
        if model_name == 'LinearRegression' and hasattr(self, 'X_train_scaled'):
            data_to_predict = self.scaler.transform(data_to_predict)
        
        predictions = model.predict(data_to_predict)
        
        if self.problem_type == 'classification':
            # Obtener probabilidades si están disponibles
            if hasattr(model, 'predict_proba'):
                probabilities = model.predict_proba(data_to_predict)
                return predictions, probabilities
        
        return predictions
    
    # Crear visualizaciones de resultados
    def create_visualizations(self):
        """Crea visualizaciones de los resultados del machine learning"""
        if self.problem_type == 'classification':
            self._create_classification_visualizations()
        else:
            self._create_regression_visualizations()
    
    def _create_classification_visualizations(self):
        """Crea visualizaciones para problemas de clasificación"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análisis de Clasificación', fontsize=16, fontweight='bold')
        
        # 1. Matriz de confusión para el mejor modelo
        best_model_name = max(self.models.keys(), 
                             key=lambda x: accuracy_score(self.y_test, self.predictions[x]))
        
        cm = confusion_matrix(self.y_test, self.predictions[best_model_name])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0, 0])
        axes[0, 0].set_title(f'Matriz de Confusión - {best_model_name}')
        axes[0, 0].set_xlabel('Predicción')
        axes[0, 0].set_ylabel('Real')
        
        # 2. Comparación de métricas
        metrics = []
        models = []
        for model_name in self.models.keys():
            y_pred = self.predictions[model_name]
            accuracy = accuracy_score(self.y_test, y_pred)
            precision = precision_score(self.y_test, y_pred, average='weighted')
            recall = recall_score(self.y_test, y_pred, average='weighted')
            f1 = f1_score(self.y_test, y_pred, average='weighted')
            
            metrics.extend([accuracy, precision, recall, f1])
            models.extend([model_name] * 4)
        
        metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score'] * len(self.models)
        
        df_metrics = pd.DataFrame({
            'Modelo': models,
            'Métrica': metric_names,
            'Valor': metrics
        })
        
        sns.barplot(data=df_metrics, x='Métrica', y='Valor', hue='Modelo', ax=axes[0, 1])
        axes[0, 1].set_title('Comparación de Métricas por Modelo')
        axes[0, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 3. Distribución de clases
        self.y.value_counts().plot(kind='bar', ax=axes[1, 0], color='skyblue')
        axes[1, 0].set_title('Distribución de Clases en el Dataset')
        axes[1, 0].set_xlabel('Clase')
        axes[1, 0].set_ylabel('Frecuencia')
        
        # 4. Importancia de características (si está disponible)
        if 'RandomForest' in self.models:
            rf_model = self.models['RandomForest']
            importances = rf_model.feature_importances_
            feature_importance = pd.DataFrame({
                'feature': self.X.columns,
                'importance': importances
            }).sort_values('importance', ascending=False).head(10)
            
            sns.barplot(data=feature_importance, x='importance', y='feature', ax=axes[1, 1])
            axes[1, 1].set_title('Top 10 Características Más Importantes')
            axes[1, 1].set_xlabel('Importancia')
        
        plt.tight_layout()
        plt.show()
    
    def _create_regression_visualizations(self):
        """Crea visualizaciones para problemas de regresión"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análisis de Regresión', fontsize=16, fontweight='bold')
        
        # 1. Valores reales vs predicciones
        best_model_name = max(self.models.keys(), 
                             key=lambda x: r2_score(self.y_test, self.predictions[x]))
        
        y_pred = self.predictions[best_model_name]
        axes[0, 0].scatter(self.y_test, y_pred, alpha=0.6)
        axes[0, 0].plot([self.y_test.min(), self.y_test.max()], 
                       [self.y_test.min(), self.y_test.max()], 'r--', lw=2)
        axes[0, 0].set_xlabel('Valores Reales')
        axes[0, 0].set_ylabel('Predicciones')
        axes[0, 0].set_title(f'Reales vs Predicciones - {best_model_name}')
        
        # 2. Residuos
        residuals = self.y_test - y_pred
        axes[0, 1].scatter(y_pred, residuals, alpha=0.6)
        axes[0, 1].axhline(y=0, color='r', linestyle='--')
        axes[0, 1].set_xlabel('Predicciones')
        axes[0, 1].set_ylabel('Residuos')
        axes[0, 1].set_title('Gráfico de Residuos')
        
        # 3. Comparación de métricas
        metrics_comparison = []
        for model_name in self.models.keys():
            y_pred = self.predictions[model_name]
            mse = mean_squared_error(self.y_test, y_pred)
            rmse = np.sqrt(mse)
            r2 = r2_score(self.y_test, y_pred)
            
            metrics_comparison.append({
                'Modelo': model_name,
                'MSE': mse,
                'RMSE': rmse,
                'R²': r2
            })
        
        df_metrics = pd.DataFrame(metrics_comparison)
        
        # Normalizar métricas para comparación visual
        df_plot = df_metrics.set_index('Modelo')[['RMSE', 'R²']].copy()
        df_plot['RMSE_norm'] = 1 - (df_plot['RMSE'] / df_plot['RMSE'].max())  # Invertir RMSE
        
        df_plot[['RMSE_norm', 'R²']].plot(kind='bar', ax=axes[1, 0])
        axes[1, 0].set_title('Comparación de Modelos (Normalizado)')
        axes[1, 0].set_ylabel('Score (mayor es mejor)')
        axes[1, 0].legend(['RMSE (invertido)', 'R²'])
        
        # 4. Distribución de la variable objetivo
        axes[1, 1].hist(self.y, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
        axes[1, 1].set_title('Distribución de la Variable Objetivo')
        axes[1, 1].set_xlabel('Valor')
        axes[1, 1].set_ylabel('Frecuencia')
        
        plt.tight_layout()
        plt.show()
    
    # Implementar clustering con K-Means
    def perform_clustering(self, n_clusters=3):
        """Realiza clustering K-Means en los datos"""
        print(f"\n🔄 Realizando clustering con K-Means (k={n_clusters})")
        
        # Usar datos escalados para clustering
        X_scaled = self.scaler.fit_transform(self.X)
        
        # Aplicar K-Means
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(X_scaled)
        
        # Añadir etiquetas de cluster al dataframe
        clustered_data = self.X.copy()
        clustered_data['Cluster'] = cluster_labels
        
        print(f"✅ Clustering completado")
        print(f"Distribución de clusters: {pd.Series(cluster_labels).value_counts().sort_index()}")
        
        # Visualizar clusters si es posible
        if self.X.shape[1] >= 2:
            plt.figure(figsize=(10, 6))
            scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis')
            plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                       c='red', marker='x', s=200, linewidths=3, label='Centroides')
            plt.title(f'Clustering K-Means (k={n_clusters})')
            plt.xlabel(f'{self.X.columns[0]} (escalado)')
            plt.ylabel(f'{self.X.columns[1]} (escalado)')
            plt.colorbar(scatter)
            plt.legend()
            plt.show()
        
        return clustered_data, kmeans

# Función principal para demostrar machine learning
def main():
    """Función principal que demuestra todas las capacidades de ML"""
    print("🤖 DEMO: MACHINE LEARNING CON GITHUB COPILOT")
    print("=" * 50)
    
    # Ejemplo 1: Clasificación con dataset Iris
    print("\n📊 EJEMPLO 1: CLASIFICACIÓN (Dataset Iris)")
    print("-" * 40)
    
    ml_classifier = MLTutorial()
    ml_classifier.load_and_prepare_data('iris')
    ml_classifier.split_data()
    ml_classifier.create_classification_models()
    ml_classifier.evaluate_models()
    
    # Hacer una predicción de ejemplo
    print("\n🔮 Predicción de ejemplo:")
    sample_data = [5.1, 3.5, 1.4, 0.2]  # Medidas de una flor
    prediction, probabilities = ml_classifier.make_predictions(sample_data, 'RandomForest')
    print(f"  Datos de entrada: {sample_data}")
    print(f"  Predicción: Clase {prediction[0]}")
    print(f"  Probabilidades: {probabilities[0]}")
    
    ml_classifier.create_visualizations()
    
    # Ejemplo 2: Regresión con dataset Boston Housing
    print("\n🏠 EJEMPLO 2: REGRESIÓN (Dataset Boston Housing)")
    print("-" * 40)
    
    ml_regressor = MLTutorial()
    ml_regressor.load_and_prepare_data('boston')
    ml_regressor.split_data()
    ml_regressor.create_regression_models()
    ml_regressor.evaluate_models()
    ml_regressor.create_visualizations()
    
    # Ejemplo 3: Clustering
    print("\n🎯 EJEMPLO 3: CLUSTERING")
    print("-" * 40)
    
    clustered_data, kmeans_model = ml_classifier.perform_clustering(n_clusters=3)
    print(f"Primeras 5 filas con clusters asignados:\n{clustered_data.head()}")

if __name__ == "__main__":
    main()