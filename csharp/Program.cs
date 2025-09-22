using System;
using CopilotTutorial;
using CopilotTutorial.TaskManager;

namespace CopilotTutorial
{
    // Programa principal para demostrar los ejemplos de GitHub Copilot
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== GitHub Copilot Tutorial - Ejemplos en C# ===\n");

            // Demostrar la calculadora
            DemonstrateCalculator();

            Console.WriteLine("\n" + new string('=', 50) + "\n");

            // Demostrar el gestor de tareas
            DemonstrateTaskManager();

            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }

        // Método para demostrar la funcionalidad de la calculadora
        static void DemonstrateCalculator()
        {
            Console.WriteLine("🧮 EJEMPLO 1: CALCULADORA");
            Console.WriteLine("========================\n");

            var calculator = new Calculator();

            try
            {
                // Demostrar operaciones básicas
                Console.WriteLine($"Suma: 10 + 5 = {calculator.Add(10, 5)}");
                Console.WriteLine($"Resta: 10 - 5 = {calculator.Subtract(10, 5)}");
                Console.WriteLine($"Multiplicación: 10 * 5 = {calculator.Multiply(10, 5)}");
                Console.WriteLine($"División: 10 / 5 = {calculator.Divide(10, 5)}");

                // Demostrar cálculo de promedio
                int[] numbers = { 10, 20, 30, 40, 50 };
                Console.WriteLine($"Promedio de [10, 20, 30, 40, 50] = {calculator.CalculateAverage(numbers):F2}");

                // Demostrar potencia y raíz cuadrada
                Console.WriteLine($"2 elevado a la 8 = {calculator.Power(2, 8)}");
                Console.WriteLine($"Raíz cuadrada de 16 = {calculator.SquareRoot(16)}");

                // Demostrar manejo de errores
                Console.WriteLine("\nProbando división por cero...");
                try
                {
                    calculator.Divide(10, 0);
                }
                catch (DivideByZeroException ex)
                {
                    Console.WriteLine($"Error capturado: {ex.Message}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }

        // Método para demostrar la funcionalidad del gestor de tareas
        static void DemonstrateTaskManager()
        {
            Console.WriteLine("📋 EJEMPLO 2: GESTOR DE TAREAS");
            Console.WriteLine("==============================\n");

            var taskManager = new TaskManager();

            // Añadir algunas tareas de ejemplo
            taskManager.AddTask("Estudiar C#", "Completar tutorial de GitHub Copilot", DateTime.Now.AddDays(3));
            taskManager.AddTask("Hacer ejercicio", "Correr 30 minutos en el parque", DateTime.Now.AddDays(1));
            taskManager.AddTask("Comprar víveres", "Ir al supermercado por la tarde", DateTime.Now.AddDays(-1)); // Tarea vencida
            taskManager.AddTask("Reunión de trabajo", "Presentar proyecto final", DateTime.Now.AddDays(7));

            // Mostrar todas las tareas
            Console.WriteLine("📝 Todas las tareas:");
            var allTasks = taskManager.GetAllTasks();
            foreach (var task in allTasks)
            {
                string status = task.IsCompleted ? "✅" : "⏳";
                Console.WriteLine($"  {status} [{task.Id}] {task.Title} - Vence: {task.DueDate:dd/MM/yyyy}");
            }

            // Completar una tarea
            Console.WriteLine("\n✅ Completando tarea 'Hacer ejercicio'...");
            taskManager.CompleteTask(2);

            // Mostrar tareas pendientes
            Console.WriteLine("\n⏳ Tareas pendientes:");
            var pendingTasks = taskManager.GetPendingTasks();
            foreach (var task in pendingTasks)
            {
                Console.WriteLine($"  📌 [{task.Id}] {task.Title}");
            }

            // Mostrar tareas completadas
            Console.WriteLine("\n✅ Tareas completadas:");
            var completedTasks = taskManager.GetCompletedTasks();
            foreach (var task in completedTasks)
            {
                Console.WriteLine($"  ✔️ [{task.Id}] {task.Title}");
            }

            // Buscar tareas
            Console.WriteLine("\n🔍 Buscando tareas con 'trabajo':");
            var searchResults = taskManager.SearchTasksByTitle("trabajo");
            foreach (var task in searchResults)
            {
                Console.WriteLine($"  🎯 [{task.Id}] {task.Title}");
            }

            // Mostrar estadísticas
            Console.WriteLine("\n📊 Estadísticas:");
            var stats = taskManager.GetStatistics();
            Console.WriteLine($"  Total de tareas: {stats.TotalTasks}");
            Console.WriteLine($"  Completadas: {stats.CompletedTasks}");
            Console.WriteLine($"  Pendientes: {stats.PendingTasks}");
            Console.WriteLine($"  Vencidas: {stats.OverdueTasks}");

            // Mostrar tareas que vencen pronto
            Console.WriteLine("\n⚠️ Tareas que vencen en los próximos 7 días:");
            var dueSoon = taskManager.GetTasksDueSoon();
            foreach (var task in dueSoon)
            {
                var daysUntilDue = (task.DueDate - DateTime.Now).Days;
                Console.WriteLine($"  🕒 [{task.Id}] {task.Title} - Vence en {daysUntilDue} día(s)");
            }
        }
    }
}