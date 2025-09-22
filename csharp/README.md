# Ejemplos de GitHub Copilot para C#

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con C#.

## 📚 Contenido

1. [Ejemplo Básico: Calculadora](#ejemplo-1-calculadora-básica)
2. [Ejemplo Intermedio: Gestor de Tareas](#ejemplo-2-gestor-de-tareas)
3. [Ejemplo Avanzado: API REST](#ejemplo-3-api-rest-con-aspnet-core)

## Prerequisitos

- .NET 6.0 o superior
- Visual Studio 2022 o Visual Studio Code con extensión de C#
- GitHub Copilot habilitado

## 🧮 Ejemplo 1: Calculadora Básica

### Objetivo
Crear una calculadora simple usando GitHub Copilot para generar métodos matemáticos.

### Instrucciones paso a paso

1. **Crea un nuevo archivo**: `Calculator.cs`
2. **Escribe un comentario descriptivo** y deja que Copilot genere el código:

```csharp
// Crear una clase Calculator con métodos para operaciones básicas
```

3. **Continúa describiendo la funcionalidad**:

```csharp
// Método para sumar dos números
// Método para restar dos números
// Método para multiplicar dos números
// Método para dividir dos números con validación de división por cero
```

### 💡 Tips para este ejemplo
- Usa comentarios específicos como "// Método que suma dos números enteros y retorna el resultado"
- Copilot generará automáticamente los métodos con validaciones básicas
- Prueba variaciones como "// Método que calcula el promedio de una lista de números"

---

## 📋 Ejemplo 2: Gestor de Tareas

### Objetivo
Crear un sistema simple de gestión de tareas que demuestre el uso de clases, interfaces y LINQ.

### Instrucciones paso a paso

1. **Define el modelo de datos**:
```csharp
// Crear una clase Task con propiedades: Id, Title, Description, IsCompleted, DueDate
```

2. **Crea la interfaz del gestor**:
```csharp
// Interfaz ITaskManager con métodos para añadir, eliminar, completar y listar tareas
```

3. **Implementa el gestor**:
```csharp
// Clase TaskManager que implementa ITaskManager usando una lista para almacenar tareas
```

### 🎯 Funcionalidades a implementar
- Añadir nueva tarea
- Marcar tarea como completada
- Eliminar tarea
- Listar tareas pendientes
- Listar tareas completadas
- Buscar tareas por título

---

## 🌐 Ejemplo 3: API REST con ASP.NET Core

### Objetivo
Crear una API REST simple para gestionar productos, demostrando el uso de controladores, servicios y Entity Framework.

### Instrucciones paso a paso

1. **Crea el proyecto**:
```bash
dotnet new webapi -n ProductApi
cd ProductApi
```

2. **Define el modelo Product**:
```csharp
// Modelo Product con propiedades: Id, Name, Description, Price, CategoryId
```

3. **Crea el controlador**:
```csharp
// Controller ProductsController con endpoints CRUD para gestionar productos
```

4. **Implementa el servicio**:
```csharp
// Servicio ProductService con lógica de negocio para operaciones CRUD
```

### 🔧 Configuración adicional
```bash
# Instalar Entity Framework
dotnet add package Microsoft.EntityFrameworkCore.InMemory
```

### 📊 Endpoints a implementar
- `GET /api/products` - Obtener todos los productos
- `GET /api/products/{id}` - Obtener producto por ID
- `POST /api/products` - Crear nuevo producto
- `PUT /api/products/{id}` - Actualizar producto
- `DELETE /api/products/{id}` - Eliminar producto

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **Sistema de Autenticación JWT**
   ```csharp
   // Crear servicio de autenticación JWT con login y registro de usuarios
   ```

2. **Cache Redis**
   ```csharp
   // Implementar caching con Redis para mejorar performance de la API
   ```

3. **Validaciones con FluentValidation**
   ```csharp
   // Crear validadores para los modelos usando FluentValidation
   ```

4. **Tests Unitarios**
   ```csharp
   // Crear tests unitarios para los servicios usando xUnit y Moq
   ```

## 💡 Tips específicos para C# y Copilot

1. **Usa atributos descriptivos**: `[HttpGet]`, `[Route]`, etc.
2. **Comenta interfaces primero**: Copilot genera mejores implementaciones
3. **Menciona patrones**: "// Implementar patrón Repository"
4. **Especifica librerías**: "// Usar Entity Framework para persistencia"
5. **Describe validaciones**: "// Validar que el email tenga formato correcto"

---

¡Explora cada ejemplo y experimenta con diferentes comentarios para ver cómo Copilot adapta sus sugerencias! 🎯