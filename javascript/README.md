# Ejemplos de GitHub Copilot para JavaScript

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con JavaScript.

## 📚 Contenido

1. [Ejemplo Básico: Manipulación del DOM](#ejemplo-1-manipulación-del-dom-y-eventos)
2. [Ejemplo Intermedio: API REST con Node.js](#ejemplo-2-api-rest-con-nodejs-y-express)
3. [Ejemplo Avanzado: Aplicación React](#ejemplo-3-aplicación-react-con-gestión-de-estado)

## Prerequisitos

- Node.js 16.0 o superior
- npm o yarn
- Visual Studio Code con extensión de JavaScript/TypeScript
- GitHub Copilot habilitado

```bash
# Verificar versiones
node --version
npm --version
```

## 🎨 Ejemplo 1: Manipulación del DOM y Eventos

### Objetivo
Crear una aplicación web interactiva que demuestre manipulación del DOM, eventos y almacenamiento local.

### Instrucciones paso a paso

1. **Crea la estructura HTML**:
```html
<!-- Crear página HTML con formulario para gestión de tareas -->
```

2. **Implementa funciones de manipulación del DOM**:
```javascript
// Función para añadir tarea al DOM
// Función para marcar tarea como completada
// Función para eliminar tarea del DOM
```

3. **Agrega manejo de eventos**:
```javascript
// Event listener para el formulario de nueva tarea
// Event listeners para botones de completar y eliminar
// Event listener para filtrar tareas
```

4. **Implementa persistencia local**:
```javascript
// Función para guardar tareas en localStorage
// Función para cargar tareas desde localStorage
// Función para sincronizar DOM con localStorage
```

### 💡 Tips para este ejemplo
- Usa comentarios específicos como "// Función que añade nueva tarea al final de la lista"
- Copilot generará automáticamente los selectores DOM apropiados
- Prueba variaciones como "// Función que filtra tareas por estado completado"

### 🎯 Funcionalidades a implementar
- Añadir nueva tarea
- Marcar tarea como completada/pendiente
- Eliminar tarea
- Filtrar tareas (todas, pendientes, completadas)
- Persistencia en localStorage
- Contador de tareas pendientes

---

## 🌐 Ejemplo 2: API REST con Node.js y Express

### Objetivo
Crear una API REST para gestionar libros usando Express.js, demostrando middleware, routing y validaciones.

### Configuración inicial
```bash
npm init -y
npm install express cors helmet morgan joi
npm install -D nodemon
```

### Instrucciones paso a paso

1. **Configura el servidor Express**:
```javascript
// Crear servidor Express con middleware básico
// Configurar CORS, helmet y morgan para logging
```

2. **Define el modelo de datos**:
```javascript
// Modelo Book con propiedades: id, title, author, year, genre, available
// Array en memoria para almacenar libros
```

3. **Implementa las rutas CRUD**:
```javascript
// GET /api/books - Obtener todos los libros
// GET /api/books/:id - Obtener libro por ID
// POST /api/books - Crear nuevo libro
// PUT /api/books/:id - Actualizar libro
// DELETE /api/books/:id - Eliminar libro
```

4. **Añade validaciones**:
```javascript
// Middleware de validación usando Joi
// Validar datos de entrada en POST y PUT
// Manejo de errores personalizado
```

### 🔧 Funcionalidades a implementar
- CRUD completo para libros
- Validación de datos de entrada
- Manejo de errores HTTP
- Middleware de logging
- Búsqueda de libros por autor o género
- Paginación de resultados

### 📊 Endpoints a implementar
- `GET /api/books` - Obtener todos los libros
- `GET /api/books/:id` - Obtener libro por ID
- `POST /api/books` - Crear nuevo libro
- `PUT /api/books/:id` - Actualizar libro
- `DELETE /api/books/:id` - Eliminar libro
- `GET /api/books/search?author=&genre=` - Buscar libros

---

## ⚛️ Ejemplo 3: Aplicación React con Gestión de Estado

### Objetivo
Crear una aplicación React completa con hooks, gestión de estado global y comunicación con API.

### Configuración inicial
```bash
npx create-react-app copilot-react-app
cd copilot-react-app
npm install axios react-router-dom @reduxjs/toolkit react-redux
```

### Instrucciones paso a paso

1. **Configura la estructura de componentes**:
```javascript
// Componente principal App con React Router
// Componentes para Home, ProductList, ProductForm, ProductDetail
```

2. **Implementa gestión de estado con Redux Toolkit**:
```javascript
// Store de Redux con slice para productos
// Actions para CRUD de productos
// Selectors para obtener datos del estado
```

3. **Crea componentes reutilizables**:
```javascript
// Componente ProductCard para mostrar producto
// Componente SearchBar para filtrar productos
// Componente Modal para confirmaciones
```

4. **Integra comunicación con API**:
```javascript
// Service para llamadas HTTP con axios
// Hooks personalizados para operaciones CRUD
// Manejo de estados de carga y errores
```

### 🚀 Funcionalidades a implementar
- Lista de productos con búsqueda y filtros
- Formulario para crear/editar productos
- Vista detalle de producto
- Gestión de estado global con Redux
- Navegación con React Router
- Manejo de estados de carga y errores
- Responsive design

### 🔄 Hooks y patrones a explorar
- useState, useEffect, useContext
- Custom hooks para lógica reutilizable
- useSelector y useDispatch de React Redux
- Lazy loading de componentes
- Error boundaries

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **Autenticación JWT**
   ```javascript
   // Implementar login/logout con JWT tokens
   // Guardar tokens en localStorage o cookies
   ```

2. **WebSockets en tiempo real**
   ```javascript
   // Chat en tiempo real usando Socket.IO
   // Notificaciones push en tiempo real
   ```

3. **PWA (Progressive Web App)**
   ```javascript
   // Service Worker para cache offline
   // Manifest.json para instalación
   ```

4. **Testing con Jest**
   ```javascript
   // Tests unitarios para componentes React
   // Tests de integración para API endpoints
   ```

5. **GraphQL con Apollo Client**
   ```javascript
   // Cliente GraphQL para consultas y mutaciones
   // Cache inteligente con Apollo Client
   ```

## 💡 Tips específicos para JavaScript y Copilot

1. **Usa JSDoc para mejor contexto**: `/** @param {string} title */`
2. **Especifica el entorno**: "// Node.js server" o "// React component"
3. **Menciona librerías**: "// Using Express.js" o "// React hook with useState"
4. **Describe el patrón**: "// Async/await pattern" o "// Higher-order component"
5. **Incluye tipos en comentarios**: "// Function returns Promise<User[]>"

### 🎯 Mejores prácticas para Copilot + JavaScript
- Usa nombres descriptivos para variables y funciones
- Especifica si es código frontend o backend
- Menciona frameworks/librerías en comentarios
- Describe el propósito de la función antes de implementarla
- Usa arrow functions y destructuring para código moderno

---

¡Explora cada ejemplo y experimenta con diferentes comentarios para descubrir todo el potencial de JavaScript con GitHub Copilot! 🚀✨