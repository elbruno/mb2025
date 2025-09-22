# Crear aplicación Flask para gestionar una biblioteca de libros
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir modelo de datos para libros con id, titulo, autor, año
class Book:
    """Modelo de datos para representar un libro"""
    
    def __init__(self, title, author, year, isbn=None, genre=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.genre = genre
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convierte el objeto libro a diccionario"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
            'genre': self.genre,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

# Base de datos en memoria (lista de libros)
books_db = []

# Crear algunos libros de ejemplo
sample_books = [
    Book("Cien años de soledad", "Gabriel García Márquez", 1967, "978-0307474728", "Realismo mágico"),
    Book("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "978-0142437230", "Clásico"),
    Book("1984", "George Orwell", 1949, "978-0451524935", "Distopía"),
    Book("El Principito", "Antoine de Saint-Exupéry", 1943, "978-0156012195", "Fábula"),
]

books_db.extend(sample_books)

# Función para validar datos de entrada de libro
def validate_book_data(data):
    """Valida los datos de entrada para crear o actualizar un libro"""
    errors = []
    
    # Validar campos requeridos
    required_fields = ['title', 'author', 'year']
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"El campo '{field}' es requerido")
    
    # Validar año
    if 'year' in data:
        try:
            year = int(data['year'])
            current_year = datetime.now().year
            if year < 1000 or year > current_year + 1:
                errors.append(f"El año debe estar entre 1000 y {current_year + 1}")
        except (ValueError, TypeError):
            errors.append("El año debe ser un número entero válido")
    
    # Validar título y autor no estén vacíos
    if 'title' in data and len(data['title'].strip()) < 2:
        errors.append("El título debe tener al menos 2 caracteres")
    
    if 'author' in data and len(data['author'].strip()) < 2:
        errors.append("El autor debe tener al menos 2 caracteres")
    
    # Validar ISBN si se proporciona
    if 'isbn' in data and data['isbn']:
        isbn = data['isbn'].replace('-', '').replace(' ', '')
        if not (isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13)):
            errors.append("El ISBN debe tener 10 o 13 dígitos")
    
    return errors

# Función para buscar libro por ID
def find_book_by_id(book_id):
    """Busca un libro por su ID"""
    for book in books_db:
        if book.id == book_id:
            return book
    return None

# Ruta principal de la API
@app.route('/')
def home():
    """Página de inicio de la API"""
    return jsonify({
        'message': 'Bienvenido a la API de Biblioteca',
        'version': '1.0',
        'endpoints': {
            'GET /api/books': 'Obtener todos los libros',
            'GET /api/books/<id>': 'Obtener libro por ID',
            'POST /api/books': 'Crear nuevo libro',
            'PUT /api/books/<id>': 'Actualizar libro',
            'DELETE /api/books/<id>': 'Eliminar libro',
            'GET /api/books/search': 'Buscar libros por autor o título'
        }
    })

# Ruta GET para obtener todos los libros
@app.route('/api/books', methods=['GET'])
def get_all_books():
    """Obtiene todos los libros de la biblioteca"""
    try:
        # Parámetros de consulta opcionales
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Validar parámetros de paginación
        if page < 1:
            page = 1
        if per_page < 1 or per_page > 100:
            per_page = 10
        
        # Calcular índices para paginación
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        
        # Obtener libros paginados
        paginated_books = books_db[start_index:end_index]
        
        return jsonify({
            'books': [book.to_dict() for book in paginated_books],
            'total': len(books_db),
            'page': page,
            'per_page': per_page,
            'pages': (len(books_db) + per_page - 1) // per_page
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Ruta GET para obtener un libro por ID
@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    """Obtiene un libro específico por su ID"""
    try:
        book = find_book_by_id(book_id)
        
        if book is None:
            return jsonify({'error': f'Libro con ID {book_id} no encontrado'}), 404
        
        return jsonify({'book': book.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Ruta POST para crear un nuevo libro
@app.route('/api/books', methods=['POST'])
def create_book():
    """Crea un nuevo libro en la biblioteca"""
    try:
        # Validar que se envió JSON
        if not request.is_json:
            return jsonify({'error': 'Content-Type debe ser application/json'}), 400
        
        data = request.get_json()
        
        # Validar datos de entrada
        errors = validate_book_data(data)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400
        
        # Verificar si ya existe un libro con el mismo título y autor
        for existing_book in books_db:
            if (existing_book.title.lower() == data['title'].lower() and 
                existing_book.author.lower() == data['author'].lower()):
                return jsonify({'error': 'Ya existe un libro con el mismo título y autor'}), 409
        
        # Crear nuevo libro
        new_book = Book(
            title=data['title'].strip(),
            author=data['author'].strip(),
            year=int(data['year']),
            isbn=data.get('isbn', '').strip() if data.get('isbn') else None,
            genre=data.get('genre', '').strip() if data.get('genre') else None
        )
        
        # Añadir a la base de datos
        books_db.append(new_book)
        
        return jsonify({
            'message': 'Libro creado exitosamente',
            'book': new_book.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Ruta PUT para actualizar un libro existente
@app.route('/api/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    """Actualiza un libro existente"""
    try:
        # Buscar el libro
        book = find_book_by_id(book_id)
        if book is None:
            return jsonify({'error': f'Libro con ID {book_id} no encontrado'}), 404
        
        # Validar que se envió JSON
        if not request.is_json:
            return jsonify({'error': 'Content-Type debe ser application/json'}), 400
        
        data = request.get_json()
        
        # Validar datos de entrada
        errors = validate_book_data(data)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400
        
        # Actualizar campos
        book.title = data['title'].strip()
        book.author = data['author'].strip()
        book.year = int(data['year'])
        book.isbn = data.get('isbn', '').strip() if data.get('isbn') else None
        book.genre = data.get('genre', '').strip() if data.get('genre') else None
        book.updated_at = datetime.now().isoformat()
        
        return jsonify({
            'message': 'Libro actualizado exitosamente',
            'book': book.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Ruta DELETE para eliminar un libro
@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Elimina un libro de la biblioteca"""
    try:
        book = find_book_by_id(book_id)
        if book is None:
            return jsonify({'error': f'Libro con ID {book_id} no encontrado'}), 404
        
        # Eliminar libro de la base de datos
        books_db.remove(book)
        
        return jsonify({
            'message': 'Libro eliminado exitosamente',
            'deleted_book': book.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Ruta para buscar libros por autor o título
@app.route('/api/books/search', methods=['GET'])
def search_books():
    """Busca libros por título, autor o género"""
    try:
        # Obtener parámetros de búsqueda
        query = request.args.get('q', '').strip().lower()
        author = request.args.get('author', '').strip().lower()
        genre = request.args.get('genre', '').strip().lower()
        year_from = request.args.get('year_from', type=int)
        year_to = request.args.get('year_to', type=int)
        
        if not any([query, author, genre, year_from, year_to]):
            return jsonify({'error': 'Se requiere al menos un parámetro de búsqueda'}), 400
        
        # Filtrar libros
        filtered_books = []
        
        for book in books_db:
            match = True
            
            # Búsqueda por texto general (título o autor)
            if query:
                if not (query in book.title.lower() or query in book.author.lower()):
                    match = False
            
            # Búsqueda por autor específico
            if author and author not in book.author.lower():
                match = False
            
            # Búsqueda por género
            if genre and (not book.genre or genre not in book.genre.lower()):
                match = False
            
            # Filtro por rango de años
            if year_from and book.year < year_from:
                match = False
            
            if year_to and book.year > year_to:
                match = False
            
            if match:
                filtered_books.append(book)
        
        return jsonify({
            'books': [book.to_dict() for book in filtered_books],
            'total': len(filtered_books),
            'search_params': {
                'query': query,
                'author': author,
                'genre': genre,
                'year_from': year_from,
                'year_to': year_to
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor', 'details': str(e)}), 500

# Manejo de errores 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint no encontrado'}), 404

# Manejo de errores 405
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Método no permitido para este endpoint'}), 405

# Función principal
if __name__ == '__main__':
    print("🚀 Iniciando API de Biblioteca...")
    print("📚 Endpoints disponibles:")
    print("  GET    /api/books          - Obtener todos los libros")
    print("  GET    /api/books/<id>     - Obtener libro por ID")
    print("  POST   /api/books          - Crear nuevo libro")
    print("  PUT    /api/books/<id>     - Actualizar libro")
    print("  DELETE /api/books/<id>     - Eliminar libro")
    print("  GET    /api/books/search   - Buscar libros")
    print("\n💡 Ejemplo de uso:")
    print("  curl -X GET http://localhost:5000/api/books")
    print("  curl -X POST http://localhost:5000/api/books -H 'Content-Type: application/json' -d '{\"title\":\"Nuevo Libro\",\"author\":\"Autor\",\"year\":2023}'")
    
    app.run(debug=True, host='0.0.0.0', port=5000)