#!/usr/bin/env python3
# Test simple de Python sin dependencias externas

# Crear una función simple usando GitHub Copilot
def calculate_fibonacci(n):
    """Calcula la secuencia de Fibonacci hasta n términos"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Función para validar email usando expresiones regulares
import re

def validate_email(email):
    """Valida si un email tiene formato correcto"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Función para procesar lista de números
def process_numbers(numbers):
    """Procesa una lista de números y retorna estadísticas básicas"""
    if not numbers:
        return {}
    
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers),
        'even_count': len([n for n in numbers if n % 2 == 0]),
        'odd_count': len([n for n in numbers if n % 2 != 0])
    }

def main():
    print("🐍 Test simple de Python con GitHub Copilot")
    print("=" * 50)
    
    # Test Fibonacci
    print("\n📊 Secuencia de Fibonacci (10 términos):")
    fib_result = calculate_fibonacci(10)
    print(f"  {fib_result}")
    
    # Test validación de email
    print("\n✉️ Validación de emails:")
    test_emails = ["usuario@ejemplo.com", "email.invalido", "otro@test.es"]
    for email in test_emails:
        is_valid = validate_email(email)
        status = "✅ Válido" if is_valid else "❌ Inválido"
        print(f"  {email}: {status}")
    
    # Test procesamiento de números
    print("\n🔢 Estadísticas de números:")
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = process_numbers(test_numbers)
    print(f"  Números: {test_numbers}")
    for key, value in stats.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()