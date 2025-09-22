# Instrucciones de construcción para JavaScript

## Prerequisitos
- Node.js 16.0 o superior
- npm o yarn

## Instalación de dependencias
```bash
npm install
```

## Ejecutar ejemplos

### Ejemplo 1: DOM Manipulation (Frontend)
Abrir `index.html` en el navegador o usar un servidor local:
```bash
# Opción 1: Servidor simple con Python
python -m http.server 8000

# Opción 2: Servidor con Node.js (si tienes http-server instalado)
npx http-server -p 8000

# Abrir navegador en http://localhost:8000
```

### Ejemplo 2: Express API (Backend)
```bash
# Instalar dependencias
npm install

# Modo desarrollo con auto-reload
npm run dev

# Modo producción
npm start

# Testing (opcional)
npm test
```

## Endpoints disponibles
- `GET /api/books` - Obtener todos los libros
- `GET /api/books/:id` - Obtener libro por ID
- `POST /api/books` - Crear nuevo libro
- `PUT /api/books/:id` - Actualizar libro
- `DELETE /api/books/:id` - Eliminar libro
- `GET /api/books/search?author=...&genre=...` - Buscar libros

## Testing con curl
```bash
# Obtener todos los libros
curl http://localhost:3000/api/books

# Crear nuevo libro
curl -X POST http://localhost:3000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Nuevo Libro","author":"Autor","year":2023,"genre":"Ficción"}'
```