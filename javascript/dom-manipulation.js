// GitHub Copilot Tutorial - DOM Manipulation Example
// Esta aplicación demuestra manipulación del DOM, eventos y localStorage

// Clase para gestionar tareas
class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentFilter = 'all';
        this.init();
    }

    // Inicializar la aplicación
    init() {
        // Cargar tareas desde localStorage
        this.loadTasks();
        
        // Configurar event listeners
        this.setupEventListeners();
        
        // Renderizar tareas iniciales
        this.renderTasks();
        
        // Actualizar contador
        this.updateCounter();
    }

    // Configurar todos los event listeners
    setupEventListeners() {
        // Event listener para formulario de nueva tarea
        
        // Event listeners para filtros
        
        // Event listener para limpiar completadas
        
    }

    // Añadir nueva tarea
    addTask(title) {
        // Crear objeto tarea con id único, título y estado
        
        // Añadir a array de tareas
        
        // Guardar en localStorage
        
        // Re-renderizar vista
        
    }

    // Alternar estado completado de tarea
    toggleTask(id) {
        // Encontrar tarea por id y cambiar estado isCompleted
        
        // Guardar cambios en localStorage
        
        // Re-renderizar vista
        
    }

    // Eliminar tarea
    deleteTask(id) {
        // Filtrar array para remover tarea con id específico
        
        // Guardar cambios en localStorage
        
        // Re-renderizar vista
        
    }

    // Filtrar tareas según criterio actual
    getFilteredTasks() {
        // Retornar todas las tareas, solo pendientes o solo completadas
        // según el filtro actual
        
    }

    // Renderizar lista de tareas en el DOM
    renderTasks() {
        // Obtener tareas filtradas
        
        // Limpiar contenedor de tareas
        
        // Crear elementos DOM para cada tarea
        
        // Añadir event listeners a botones de cada tarea
        
    }

    // Crear elemento DOM para una tarea individual
    createTaskElement(task) {
        // Crear elemento li con clases apropiadas
        
        // Añadir HTML interno con checkbox, texto y botón eliminar
        
        // Retornar elemento creado
        
    }

    // Actualizar contador de tareas pendientes
    updateCounter() {
        // Contar tareas pendientes
        
        // Actualizar texto del contador en el DOM
        
    }

    // Cambiar filtro activo
    setFilter(filter) {
        // Actualizar filtro actual
        
        // Actualizar clases CSS de botones de filtro
        
        // Re-renderizar tareas
        
    }

    // Limpiar todas las tareas completadas
    clearCompleted() {
        // Filtrar para mantener solo tareas pendientes
        
        // Guardar cambios en localStorage
        
        // Re-renderizar vista
        
    }

    // Guardar tareas en localStorage
    saveTasks() {
        // Convertir array de tareas a JSON y guardar en localStorage
        
    }

    // Cargar tareas desde localStorage
    loadTasks() {
        // Obtener datos de localStorage y parsear JSON
        
        // Manejar caso donde no hay datos guardados
        
    }

    // Generar ID único para nuevas tareas
    generateId() {
        // Retornar timestamp + número aleatorio como ID único
        
    }
}

// Inicializar aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    // Crear instancia del gestor de tareas
    
});

// Función de utilidad para formatear fecha
function formatDate(date) {
    // Retornar fecha en formato legible
    
}

// Función para mostrar notificaciones (opcional)
function showNotification(message, type = 'info') {
    // Crear y mostrar notificación temporal
    
}