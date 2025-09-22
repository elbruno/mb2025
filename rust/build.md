# Instrucciones de construcción para Rust

## Prerequisitos
- Rust 1.70.0 o superior (instalado con rustup)
- Cargo (incluido con Rust)

## Instalación de Rust
```bash
# Instalar Rust usando rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Recargar el shell o ejecutar
source $HOME/.cargo/env

# Verificar instalación
rustc --version
cargo --version
```

## Compilación y ejecución

### Ejemplo 1: Calculadora CLI
```bash
# Compilar y ejecutar directamente
cargo run --bin calculator -- --first 10 --second 5 --operation add

# Compilar en modo debug
cargo build

# Compilar en modo release (optimizado)
cargo build --release

# Ejecutar binario compilado
./target/debug/calculator --help
```

### Ejemplo 2: Procesador de Archivos
```bash
# Instalar dependencias adicionales
cargo add serde_json csv tokio --features full

# Compilar y ejecutar
cargo run --bin file-processor

# Con argumentos específicos
cargo run --bin file-processor -- input.csv output.json
```

### Ejemplo 3: Servidor Web (requiere dependencias adicionales)
```bash
# Añadir dependencias para servidor web
cargo add actix-web tokio --features full

# Ejecutar servidor
cargo run --bin web-server
```

## Comandos útiles de Cargo
```bash
# Verificar que el código compila sin generar binarios
cargo check

# Ejecutar tests
cargo test

# Ejecutar tests con output verbose
cargo test -- --nocapture

# Formatear código
cargo fmt

# Linting con Clippy
cargo clippy

# Generar documentación
cargo doc --open

# Verificar dependencias outdated
cargo outdated

# Limpiar archivos compilados
cargo clean
```

## Configuración de desarrollo
```bash
# Instalar herramientas adicionales útiles
cargo install cargo-watch cargo-outdated

# Auto-compilar en cambios
cargo watch -x check

# Auto-ejecutar tests en cambios
cargo watch -x test
```

## Testing
```bash
# Ejecutar todos los tests
cargo test

# Ejecutar tests específicos
cargo test test_basic_operations

# Ejecutar tests con property-based testing
cargo test property_tests

# Coverage de tests (requiere cargo-tarpaulin)
cargo install cargo-tarpaulin
cargo tarpaulin --out Html
```

## Performance y optimización
```bash
# Build optimizado para release
cargo build --release

# Profiling con perf (Linux)
cargo build --release
perf record ./target/release/calculator
perf report

# Benchmark tests
cargo bench
```