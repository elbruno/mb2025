// GitHub Copilot Tutorial - TypeScript Calculator
// Calculadora type-safe con manejo de errores

// Tipo union para operadores matemáticos válidos
type MathOperator = '+' | '-' | '*' | '/' | '%' | '^';

// Interface para el resultado de una operación
interface CalculationResult {
    result: number;
    error?: string;
    operation: string;
}

// Interface para el historial de operaciones
interface CalculationHistory {
    timestamp: Date;
    operation: string;
    result: number;
    inputs: number[];
}

// Type guard para validar números
function isValidNumber(value: unknown): value is number {
    // Validar que el valor sea un número válido y finito
    
}

// Type guard para validar operadores
function isValidOperator(operator: string): operator is MathOperator {
    // Validar que el operador esté en la lista de operadores válidos
    
}

// Clase Calculator con tipos estrictos
class TypeSafeCalculator {
    private history: CalculationHistory[] = [];
    private precision: number = 2;

    constructor(precision: number = 2) {
        // Inicializar calculadora con precisión específica
        
    }

    // Método genérico para operaciones básicas
    calculate(a: number, operator: MathOperator, b: number): CalculationResult {
        // Validar inputs usando type guards
        
        // Realizar operación según el operador
        
        // Agregar al historial
        
        // Retornar resultado formateado
        
    }

    // Método específico para suma con overloads
    add(a: number, b: number): number;
    add(numbers: number[]): number;
    add(aOrNumbers: number | number[], b?: number): number {
        // Implementar suma con múltiples signatures
        
    }

    // Método para operaciones avanzadas
    power(base: number, exponent: number): CalculationResult {
        // Calcular potencia con validaciones
        
    }

    // Método para raíz cuadrada
    sqrt(value: number): CalculationResult {
        // Calcular raíz cuadrada con validación de números negativos
        
    }

    // Método para factorial
    factorial(n: number): CalculationResult {
        // Calcular factorial con validación de enteros positivos
        
    }

    // Método para obtener historial tipado
    getHistory(): Readonly<CalculationHistory[]> {
        // Retornar copia readonly del historial
        
    }

    // Método para limpiar historial
    clearHistory(): void {
        // Limpiar array de historial
        
    }

    // Método para estadísticas del historial
    getStatistics(): {
        totalOperations: number;
        averageResult: number;
        mostUsedOperation: MathOperator | null;
        lastCalculation: CalculationHistory | null;
    } {
        // Calcular estadísticas del historial
        
    }

    // Método privado para agregar al historial
    private addToHistory(operation: string, result: number, inputs: number[]): void {
        // Agregar nueva entrada al historial
        
    }

    // Método privado para formatear resultado
    private formatResult(value: number): number {
        // Formatear resultado según precisión configurada
        
    }

    // Método para exportar historial como JSON
    exportHistory(): string {
        // Serializar historial a JSON
        
    }

    // Método para importar historial desde JSON
    importHistory(jsonData: string): boolean {
        // Deserializar y validar historial desde JSON
        
    }
}

// Función utilitaria para crear calculadora con configuración específica
function createCalculator(config: {
    precision?: number;
    maxHistorySize?: number;
}): TypeSafeCalculator {
    // Crear instancia de calculadora con configuración
    
}

// Función para validar expresión matemática como string
function parseExpression(expression: string): {
    isValid: boolean;
    tokens: (number | MathOperator)[];
    error?: string;
} {
    // Parsear y validar expresión matemática
    
}

// Función para evaluar expresión parseada
function evaluateExpression(tokens: (number | MathOperator)[]): CalculationResult {
    // Evaluar expresión usando orden de operaciones
    
}

// Clase para manejar conversiones de unidades
class UnitConverter {
    // Conversiones de temperatura
    static celsiusToFahrenheit(celsius: number): number {
        // Convertir Celsius a Fahrenheit
        
    }

    static fahrenheitToCelsius(fahrenheit: number): number {
        // Convertir Fahrenheit a Celsius
        
    }

    // Conversiones de distancia
    static metersToFeet(meters: number): number {
        // Convertir metros a pies
        
    }

    static feetToMeters(feet: number): number {
        // Convertir pies a metros
        
    }
}

// Ejemplo de uso
function demonstrateCalculator(): void {
    // Crear instancia de calculadora
    
    // Realizar operaciones básicas
    
    // Mostrar historial y estadísticas
    
    // Usar convertidor de unidades
    
}

// Ejecutar demostración si es archivo principal
if (require.main === module) {
    demonstrateCalculator();
}

export {
    TypeSafeCalculator,
    UnitConverter,
    createCalculator,
    parseExpression,
    evaluateExpression,
    isValidNumber,
    isValidOperator
};

export type {
    MathOperator,
    CalculationResult,
    CalculationHistory
};