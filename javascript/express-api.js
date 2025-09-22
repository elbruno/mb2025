// GitHub Copilot Tutorial - Express.js API Example
// API REST para gestión de libros

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const joi = require('joi');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware básico
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());

// Base de datos en memoria (para el ejemplo)
let books = [
    {
        id: 1,
        title: "El Quijote",
        author: "Miguel de Cervantes",
        year: 1605,
        genre: "Novela",
        available: true
    },
    {
        id: 2,
        title: "Cien años de soledad",
        author: "Gabriel García Márquez",
        year: 1967,
        genre: "Realismo mágico",
        available: true
    }
];

// Esquemas de validación con Joi
const bookSchema = joi.object({
    title: joi.string().min(1).max(200).required(),
    author: joi.string().min(1).max(100).required(),
    year: joi.number().integer().min(1000).max(new Date().getFullYear()).required(),
    genre: joi.string().min(1).max(50).required(),
    available: joi.boolean().default(true)
});

// Middleware para validar ID de libro
const validateBookId = (req, res, next) => {
    // Validar que el ID sea un número entero positivo
    
};

// Middleware para validar datos de libro
const validateBook = (req, res, next) => {
    // Validar datos del libro usando esquema Joi
    
};

// Middleware de manejo de errores
const errorHandler = (err, req, res, next) => {
    // Manejar diferentes tipos de errores y retornar respuesta apropiada
    
};

// Rutas de la API

// GET /api/books - Obtener todos los libros
app.get('/api/books', (req, res) => {
    // Implementar paginación opcional
    // Implementar filtros por género y autor
    // Retornar lista de libros
    
});

// GET /api/books/:id - Obtener libro por ID
app.get('/api/books/:id', validateBookId, (req, res) => {
    // Buscar libro por ID
    // Retornar 404 si no existe
    // Retornar datos del libro
    
});

// POST /api/books - Crear nuevo libro
app.post('/api/books', validateBook, (req, res) => {
    // Generar nuevo ID
    // Crear objeto libro
    // Añadir a array de libros
    // Retornar libro creado con status 201
    
});

// PUT /api/books/:id - Actualizar libro completo
app.put('/api/books/:id', validateBookId, validateBook, (req, res) => {
    // Buscar libro por ID
    // Actualizar todas las propiedades
    // Retornar libro actualizado
    
});

// PATCH /api/books/:id - Actualizar libro parcialmente
app.patch('/api/books/:id', validateBookId, (req, res) => {
    // Buscar libro por ID
    // Validar campos enviados
    // Actualizar solo campos proporcionados
    // Retornar libro actualizado
    
});

// DELETE /api/books/:id - Eliminar libro
app.delete('/api/books/:id', validateBookId, (req, res) => {
    // Buscar índice del libro
    // Eliminar libro del array
    // Retornar status 204
    
});

// GET /api/books/search - Buscar libros
app.get('/api/books/search', (req, res) => {
    // Obtener parámetros de búsqueda (author, genre, title)
    // Filtrar libros según criterios
    // Retornar resultados paginados
    
});

// Ruta para estadísticas
app.get('/api/stats', (req, res) => {
    // Calcular estadísticas: total libros, por género, disponibles
    
});

// Middleware de manejo de rutas no encontradas
app.use('*', (req, res) => {
    res.status(404).json({
        error: 'Ruta no encontrada',
        message: 'La ruta solicitada no existe en esta API'
    });
});

// Middleware de manejo de errores (debe ir al final)
app.use(errorHandler);

// Función auxiliar para generar nuevo ID
function generateId() {
    // Retornar el siguiente ID disponible
    
}

// Función auxiliar para buscar libro por ID
function findBookById(id) {
    // Buscar y retornar libro por ID
    
}

// Función auxiliar para filtrar libros
function filterBooks(books, filters) {
    // Aplicar filtros de búsqueda
    
}

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`🚀 Servidor ejecutándose en http://localhost:${PORT}`);
    console.log(`📚 API endpoints disponibles:`);
    console.log(`   GET    /api/books`);
    console.log(`   GET    /api/books/:id`);
    console.log(`   POST   /api/books`);
    console.log(`   PUT    /api/books/:id`);
    console.log(`   PATCH  /api/books/:id`);
    console.log(`   DELETE /api/books/:id`);
    console.log(`   GET    /api/books/search`);
    console.log(`   GET    /api/stats`);
});

module.exports = app;