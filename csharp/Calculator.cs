using System;

namespace CopilotTutorial
{
    // Crear una clase Calculator con métodos para operaciones básicas
    public class Calculator
    {
        // Método para sumar dos números
        public int Add(int a, int b)
        {
            return a + b;
        }

        // Método para restar dos números
        public int Subtract(int a, int b)
        {
            return a - b;
        }

        // Método para multiplicar dos números
        public int Multiply(int a, int b)
        {
            return a * b;
        }

        // Método para dividir dos números con validación de división por cero
        public double Divide(double a, double b)
        {
            if (b == 0)
                throw new DivideByZeroException("No se puede dividir por cero");
            return a / b;
        }

        // Método que calcula el promedio de una lista de números
        public double CalculateAverage(int[] numbers)
        {
            if (numbers == null || numbers.Length == 0)
                throw new ArgumentException("La lista no puede estar vacía");
            
            int sum = 0;
            foreach (int number in numbers)
            {
                sum += number;
            }
            
            return (double)sum / numbers.Length;
        }

        // Método que calcula la potencia de un número
        public double Power(double baseNumber, int exponent)
        {
            return Math.Pow(baseNumber, exponent);
        }

        // Método que calcula la raíz cuadrada de un número
        public double SquareRoot(double number)
        {
            if (number < 0)
                throw new ArgumentException("No se puede calcular la raíz cuadrada de un número negativo");
            return Math.Sqrt(number);
        }
    }
}