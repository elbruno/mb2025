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
        const taskForm = document.getElementById('taskForm');
        const taskInput = document.getElementById('taskInput');
        
        taskForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const title = taskInput.value.trim();
            if (title) {
                this.addTask(title);
                taskInput.value = '';
            }
        });
        
        // Event listeners para filtros
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.setFilter(btn.dataset.filter);
            });
        });
        
        // Event listener para limpiar completadas
        const clearBtn = document.getElementById('clearCompleted');
        clearBtn.addEventListener('click', () => {
            this.clearCompleted();
        });
    }

    // Añadir nueva tarea
    addTask(title) {
        // Crear objeto tarea con id único, título y estado
        const task = {
            id: this.generateId(),
            title: title,
            isCompleted: false,
            createdAt: new Date().toISOString()
        };
        
        // Añadir a array de tareas
        this.tasks.push(task);
        
        // Guardar en localStorage
        this.saveTasks();
        
        // Re-renderizar vista
        this.renderTasks();
        this.updateCounter();
        
        // Mostrar notificación
        this.showNotification('Tarea añadida correctamente', 'success');
    }

    // Alternar estado completado de tarea
    toggleTask(id) {
        // Encontrar tarea por id y cambiar estado isCompleted
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.isCompleted = !task.isCompleted;
            
            // Guardar cambios en localStorage
            this.saveTasks();
            
            // Re-renderizar vista
            this.renderTasks();
            this.updateCounter();
        }
    }

    // Eliminar tarea
    deleteTask(id) {
        // Filtrar array para remover tarea con id específico
        this.tasks = this.tasks.filter(t => t.id !== id);
        
        // Guardar cambios en localStorage
        this.saveTasks();
        
        // Re-renderizar vista
        this.renderTasks();
        this.updateCounter();
        
        // Mostrar notificación
        this.showNotification('Tarea eliminada', 'info');
    }

    // Filtrar tareas según criterio actual
    getFilteredTasks() {
        // Retornar todas las tareas, solo pendientes o solo completadas
        // según el filtro actual
        switch (this.currentFilter) {
            case 'pending':
                return this.tasks.filter(task => !task.isCompleted);
            case 'completed':
                return this.tasks.filter(task => task.isCompleted);
            default:
                return this.tasks;
        }
    }

    // Renderizar lista de tareas en el DOM
    renderTasks() {
        // Obtener tareas filtradas
        const filteredTasks = this.getFilteredTasks();
        
        // Limpiar contenedor de tareas
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = '';
        
        // Crear elementos DOM para cada tarea
        filteredTasks.forEach(task => {
            const taskElement = this.createTaskElement(task);
            taskList.appendChild(taskElement);
        });
        
        // Actualizar botón de limpiar completadas
        const clearBtn = document.getElementById('clearCompleted');
        const completedCount = this.tasks.filter(t => t.isCompleted).length;
        clearBtn.disabled = completedCount === 0;
        clearBtn.textContent = `Limpiar Completadas (${completedCount})`;
    }

    // Crear elemento DOM para una tarea individual
    createTaskElement(task) {
        // Crear elemento li con clases apropiadas
        const li = document.createElement('li');
        li.className = `task-item ${task.isCompleted ? 'completed' : ''}`;
        
        // Añadir HTML interno con checkbox, texto y botón eliminar
        li.innerHTML = `
            <input type="checkbox" class="task-checkbox" ${task.isCompleted ? 'checked' : ''}>
            <span class="task-text">${this.escapeHtml(task.title)}</span>
            <button class="task-delete">Eliminar</button>
        `;
        
        // Añadir event listeners
        const checkbox = li.querySelector('.task-checkbox');
        const deleteBtn = li.querySelector('.task-delete');
        
        checkbox.addEventListener('change', () => {
            this.toggleTask(task.id);
        });
        
        deleteBtn.addEventListener('click', () => {
            this.deleteTask(task.id);
        });
        
        // Retornar elemento creado
        return li;
    }

    // Actualizar contador de tareas pendientes
    updateCounter() {
        // Contar tareas pendientes
        const pendingCount = this.tasks.filter(t => !t.isCompleted).length;
        
        // Actualizar texto del contador en el DOM
        const counter = document.getElementById('taskCounter');
        counter.textContent = `${pendingCount} tarea${pendingCount !== 1 ? 's' : ''} pendiente${pendingCount !== 1 ? 's' : ''}`;
    }

    // Cambiar filtro activo
    setFilter(filter) {
        // Actualizar filtro actual
        this.currentFilter = filter;
        
        // Actualizar clases CSS de botones de filtro
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
        
        // Re-renderizar tareas
        this.renderTasks();
    }

    // Limpiar todas las tareas completadas
    clearCompleted() {
        // Filtrar para mantener solo tareas pendientes
        const beforeCount = this.tasks.length;
        this.tasks = this.tasks.filter(t => !t.isCompleted);
        const removedCount = beforeCount - this.tasks.length;
        
        // Guardar cambios en localStorage
        this.saveTasks();
        
        // Re-renderizar vista
        this.renderTasks();
        this.updateCounter();
        
        // Mostrar notificación
        if (removedCount > 0) {
            this.showNotification(`${removedCount} tarea${removedCount > 1 ? 's' : ''} eliminada${removedCount > 1 ? 's' : ''}`, 'info');
        }
    }

    // Guardar tareas en localStorage
    saveTasks() {
        // Convertir array de tareas a JSON y guardar en localStorage
        try {
            localStorage.setItem('copilot-tasks', JSON.stringify(this.tasks));
        } catch (error) {
            console.error('Error guardando tareas:', error);
            this.showNotification('Error al guardar tareas', 'error');
        }
    }

    // Cargar tareas desde localStorage
    loadTasks() {
        // Obtener datos de localStorage y parsear JSON
        try {
            const saved = localStorage.getItem('copilot-tasks');
            if (saved) {
                this.tasks = JSON.parse(saved);
            }
        } catch (error) {
            console.error('Error cargando tareas:', error);
            this.tasks = [];
            this.showNotification('Error al cargar tareas guardadas', 'error');
        }
    }

    // Generar ID único para nuevas tareas
    generateId() {
        // Retornar timestamp + número aleatorio como ID único
        return Date.now() + Math.random().toString(36).substr(2, 9);
    }

    // Función de utilidad para escapar HTML
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Función para mostrar notificaciones
    showNotification(message, type = 'info') {
        // Crear y mostrar notificación temporal
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 20px;
            border-radius: 6px;
            color: white;
            font-weight: 500;
            z-index: 1000;
            animation: slideIn 0.3s ease-out;
            background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
        `;
        
        document.body.appendChild(notification);
        
        // Remover después de 3 segundos
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }
}

// Inicializar aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    // Crear instancia del gestor de tareas
    new TaskManager();
});

// Añadir estilos de animación para notificaciones
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(100%);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOut {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
`;
document.head.appendChild(style);