using System;
using System.Collections.Generic;
using System.Linq;

namespace CopilotTutorial.TaskManager
{
    // Crear una clase Task con propiedades: Id, Title, Description, IsCompleted, DueDate
    public class TaskItem
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
        public DateTime DueDate { get; set; }
        public DateTime CreatedDate { get; set; }

        public TaskItem()
        {
            CreatedDate = DateTime.Now;
            IsCompleted = false;
        }
    }

    // Interfaz ITaskManager con métodos para añadir, eliminar, completar y listar tareas
    public interface ITaskManager
    {
        void AddTask(string title, string description, DateTime dueDate);
        void RemoveTask(int taskId);
        void CompleteTask(int taskId);
        List<TaskItem> GetAllTasks();
        List<TaskItem> GetPendingTasks();
        List<TaskItem> GetCompletedTasks();
        List<TaskItem> SearchTasksByTitle(string searchTerm);
    }

    // Clase TaskManager que implementa ITaskManager usando una lista para almacenar tareas
    public class TaskManager : ITaskManager
    {
        private List<TaskItem> _tasks;
        private int _nextId;

        public TaskManager()
        {
            _tasks = new List<TaskItem>();
            _nextId = 1;
        }

        public void AddTask(string title, string description, DateTime dueDate)
        {
            if (string.IsNullOrWhiteSpace(title))
                throw new ArgumentException("El título no puede estar vacío");

            var task = new TaskItem
            {
                Id = _nextId++,
                Title = title,
                Description = description,
                DueDate = dueDate
            };

            _tasks.Add(task);
        }

        public void RemoveTask(int taskId)
        {
            var task = _tasks.FirstOrDefault(t => t.Id == taskId);
            if (task == null)
                throw new ArgumentException($"No se encontró una tarea con ID {taskId}");

            _tasks.Remove(task);
        }

        public void CompleteTask(int taskId)
        {
            var task = _tasks.FirstOrDefault(t => t.Id == taskId);
            if (task == null)
                throw new ArgumentException($"No se encontró una tarea con ID {taskId}");

            task.IsCompleted = true;
        }

        public List<TaskItem> GetAllTasks()
        {
            return _tasks.ToList();
        }

        public List<TaskItem> GetPendingTasks()
        {
            return _tasks.Where(t => !t.IsCompleted).ToList();
        }

        public List<TaskItem> GetCompletedTasks()
        {
            return _tasks.Where(t => t.IsCompleted).ToList();
        }

        public List<TaskItem> SearchTasksByTitle(string searchTerm)
        {
            if (string.IsNullOrWhiteSpace(searchTerm))
                return new List<TaskItem>();

            return _tasks.Where(t => t.Title.Contains(searchTerm, StringComparison.OrdinalIgnoreCase)).ToList();
        }

        // Método adicional para obtener tareas que vencen pronto
        public List<TaskItem> GetTasksDueSoon(int days = 7)
        {
            var cutoffDate = DateTime.Now.AddDays(days);
            return _tasks.Where(t => !t.IsCompleted && t.DueDate <= cutoffDate && t.DueDate >= DateTime.Now).ToList();
        }

        // Método para obtener estadísticas de tareas
        public TaskStatistics GetStatistics()
        {
            return new TaskStatistics
            {
                TotalTasks = _tasks.Count,
                CompletedTasks = _tasks.Count(t => t.IsCompleted),
                PendingTasks = _tasks.Count(t => !t.IsCompleted),
                OverdueTasks = _tasks.Count(t => !t.IsCompleted && t.DueDate < DateTime.Now)
            };
        }
    }

    // Clase para almacenar estadísticas de tareas
    public class TaskStatistics
    {
        public int TotalTasks { get; set; }
        public int CompletedTasks { get; set; }
        public int PendingTasks { get; set; }
        public int OverdueTasks { get; set; }
    }
}