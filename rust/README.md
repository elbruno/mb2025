# Ejemplos de GitHub Copilot para Rust

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con Rust.

## 📚 Contenido

1. [Ejemplo Básico: Calculadora CLI](#ejemplo-1-calculadora-de-línea-de-comandos)
2. [Ejemplo Intermedio: Procesamiento de Archivos](#ejemplo-2-procesamiento-de-archivos-y-manejo-de-errores)
3. [Ejemplo Avanzado: Servidor Web](#ejemplo-3-servidor-web-con-actix-web)

## Prerequisitos

- Rust 1.70.0 o superior
- Cargo (incluido con Rust)
- Visual Studio Code con extensión rust-analyzer
- GitHub Copilot habilitado

```bash
# Instalar Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verificar instalación
rustc --version
cargo --version
```

## 🧮 Ejemplo 1: Calculadora de Línea de Comandos

### Objetivo
Crear una calculadora robusta con manejo de errores, parsing de argumentos y testing.

### Configuración inicial
```bash
cargo new calculator-cli
cd calculator-cli
cargo add clap --features derive
cargo add anyhow
```

### Instrucciones paso a paso

1. **Define estructuras y enums**:
```rust
// Enum para operaciones matemáticas
// Struct para configuración de la calculadora
// Custom error types con thiserror
```

2. **Implementa parsing de argumentos**:
```rust
// Uso de clap para argumentos de línea de comandos
// Validación de entrada del usuario
// Help messages descriptivos
```

3. **Crea módulo de operaciones**:
```rust
// Implementación de operaciones básicas y avanzadas
// Manejo de overflow y división por cero
// Funciones para operaciones en lotes
```

4. **Añade testing comprehensivo**:
```rust
// Unit tests para cada operación
// Integration tests para CLI
// Property-based testing con quickcheck
```

### 💡 Tips para este ejemplo
- Usa `Result<T, E>` para manejo de errores explícito
- Copilot generará automáticamente match patterns apropiados
- Aprovecha el system de traits para código reutilizable

### 🎯 Características Rust a explorar
- Ownership y borrowing
- Pattern matching con `match`
- Error handling con `Result` y `Option`
- Traits y implementaciones
- Macros para código repetitivo

---

## 📁 Ejemplo 2: Procesamiento de Archivos y Manejo de Errores

### Objetivo
Crear una herramienta para procesar archivos CSV/JSON con transformaciones y validaciones.

### Configuración inicial
```bash
cargo new file-processor
cd file-processor
cargo add serde --features derive
cargo add serde_json
cargo add csv
cargo add tokio --features full
cargo add anyhow
cargo add thiserror
```

### Instrucciones paso a paso

1. **Define modelos de datos**:
```rust
// Structs con derive(Serialize, Deserialize)
// Custom validation con serde
// Type-safe configuration
```

2. **Implementa lectores de archivos**:
```rust
// Async file reading con tokio
// Streaming de archivos grandes
// Multiple format support (CSV, JSON, XML)
```

3. **Crea pipeline de transformación**:
```rust
// Iterator chains para procesamiento eficiente
// Custom transformations con closures
// Parallel processing con rayon
```

4. **Añade logging y métricas**:
```rust
// Structured logging con tracing
// Progress bars con indicatif
// Performance metrics
```

### 🔧 Funcionalidades a implementar
- Lectura async de múltiples formatos
- Validación de datos con serde
- Transformaciones customizables
- Export a diferentes formatos
- Progress tracking en tiempo real
- Error recovery y retry logic

### 📊 Arquitectura modular
```
src/
├── main.rs          # Entry point y CLI
├── config.rs        # Configuration types
├── readers/         # File format readers
├── processors/      # Data transformation
├── writers/         # Output formatters
├── errors.rs        # Error types
└── utils.rs         # Helper functions
```

---

## 🌐 Ejemplo 3: Servidor Web con Actix-web

### Objetivo
Crear una API REST completa con autenticación, base de datos y documentación automática.

### Configuración inicial
```bash
cargo new web-server
cd web-server
cargo add actix-web
cargo add actix-web-middleware-prometheus
cargo add serde --features derive
cargo add serde_json
cargo add sqlx --features runtime-tokio-rustls,postgres,chrono,uuid
cargo add tokio --features full
cargo add uuid --features v4,serde
cargo add chrono --features serde
cargo add jsonwebtoken
cargo add bcrypt
cargo add validator --features derive
```

### Instrucciones paso a paso

1. **Configura la aplicación web**:
```rust
// Actix-web server con middleware
// CORS y security headers
// Request/response logging
```

2. **Implementa modelos de base de datos**:
```rust
// Structs con SQLx annotations
// Migration scripts
// Connection pooling
```

3. **Crea handlers HTTP**:
```rust
// RESTful endpoints con validación
// JWT authentication middleware
// Request/response DTOs
```

4. **Añade testing de integración**:
```rust
// Test database setup
// HTTP client testing
// Mock services para testing
```

### 🚀 Funcionalidades avanzadas
- JWT authentication con refresh tokens
- Rate limiting por usuario/IP
- WebSocket support para real-time
- Background job processing
- Prometheus metrics integration
- OpenAPI documentation automática
- Database migrations automáticas
- Graceful shutdown handling

### 🔄 Patrones Rust para web
- Actor pattern con Actix
- Middleware personalizado
- Dependency injection con containers
- Type-safe SQL con SQLx macros
- Error handling con custom types

### 🗄️ Endpoints a implementar
- `POST /auth/login` - Autenticación de usuario
- `POST /auth/register` - Registro de usuario
- `GET /users` - Lista de usuarios (protegido)
- `POST /users` - Crear usuario (admin)
- `GET /users/{id}` - Obtener usuario específico
- `PUT /users/{id}` - Actualizar usuario
- `DELETE /users/{id}` - Eliminar usuario
- `GET /health` - Health check endpoint
- `GET /metrics` - Prometheus metrics

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **CLI Tool avanzado**
   ```rust
   // Tool de sistema con subcomandos
   // Configuration file support
   // Plugin architecture
   ```

2. **Concurrent programming**
   ```rust
   // Multi-threaded applications
   // Async/await patterns
   // Channel communication
   ```

3. **WebAssembly integration**
   ```rust
   // Compile Rust to WASM
   // JavaScript interop
   // Browser applications
   ```

4. **Performance optimization**
   ```rust
   // Zero-copy parsing
   // SIMD operations
   // Memory profiling
   ```

5. **Systems programming**
   ```rust
   // Network protocols
   // OS integration
   // Hardware interfaces
   ```

## 💡 Tips específicos para Rust y Copilot

1. **Usa nombres descriptivos**: `parse_user_input` en lugar de `parse`
2. **Especifica ownership**: Comenta "// Takes ownership" o "// Borrows immutably"
3. **Menciona error handling**: "// Returns Result<T, MyError>"
4. **Describe lifetimes**: "// Function with lifetime 'a"
5. **Indica async context**: "// Async function that..."

### 🎯 Mejores prácticas para Copilot + Rust
- Usa type annotations explícitas para mejor inference
- Aprovecha `derive` macros para boilerplate code
- Comenta invariants y assumptions importantes
- Usa `clippy` para suggestions de mejora
- Implementa `Display` y `Debug` para mejor debugging

### 🔧 Configuración Cargo.toml recomendada
```toml
[profile.dev]
opt-level = 0
debug = true
overflow-checks = true

[profile.release]
opt-level = 3
debug = false
lto = true
codegen-units = 1
panic = "abort"
```

### 🧪 Testing patterns
```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_basic_functionality() {
        // Arrange, Act, Assert pattern
    }
    
    #[tokio::test]
    async fn test_async_functionality() {
        // Async test with tokio
    }
}
```

---

¡Explora cada ejemplo y descubre la potencia de Rust + GitHub Copilot para sistemas seguros y eficientes! 🦀⚡