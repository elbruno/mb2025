# Ejemplos de GitHub Copilot para Java

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con Java.

## 📚 Contenido

1. [Ejemplo Básico: Sistema de Inventario](#ejemplo-1-sistema-de-inventario)
2. [Ejemplo Intermedio: API REST con Spring Boot](#ejemplo-2-api-rest-con-spring-boot)
3. [Ejemplo Avanzado: Microservicios](#ejemplo-3-microservicios-básicos)

## Prerequisitos

- Java 11 o superior
- Maven 3.6+ o Gradle
- IDE: IntelliJ IDEA, Eclipse, o Visual Studio Code con Extension Pack for Java
- GitHub Copilot habilitado

```bash
# Verificar instalación de Java
java -version
javac -version

# Verificar Maven
mvn -version
```

## 📦 Ejemplo 1: Sistema de Inventario

### Objetivo
Crear un sistema de gestión de inventario usando POO, colecciones y streams de Java con ayuda de GitHub Copilot.

### Instrucciones paso a paso

1. **Crea las clases del modelo**:
```java
// Crear clase Product con propiedades id, name, price, quantity, category
// Crear enumeración Category para categorizar productos
// Implementar métodos equals, hashCode y toString
```

2. **Implementa el gestor de inventario**:
```java
// Crear clase InventoryManager con lista de productos
// Métodos para añadir, eliminar, buscar y actualizar productos
// Utilizar streams para filtrar y procesar productos
```

3. **Añade funcionalidades avanzadas**:
```java
// Implementar búsqueda por múltiples criterios
// Generar reportes de inventario
// Calcular estadísticas de productos
```

### 💡 Tips para este ejemplo
- Usa comentarios como "// Método que busca productos por rango de precio usando streams"
- Copilot puede generar implementaciones completas de interfaces
- Describe patrones: "// Implementar patrón Builder para crear productos"

---

## 🌐 Ejemplo 2: API REST con Spring Boot

### Objetivo
Crear una API REST completa usando Spring Boot, JPA, y validaciones con Bean Validation.

### Configuración inicial
```bash
# Crear proyecto Spring Boot
curl https://start.spring.io/starter.zip \
  -d dependencies=web,jpa,h2,validation \
  -d type=maven-project \
  -d javaVersion=11 \
  -d packageName=com.tutorial.copilot \
  -d artifactId=copilot-api \
  -o copilot-api.zip

unzip copilot-api.zip
cd copilot-api
```

### Instrucciones paso a paso

1. **Define las entidades JPA**:
```java
// Crear entidad User con anotaciones JPA
// Entidad con validaciones Bean Validation
// Relaciones OneToMany y ManyToOne
```

2. **Implementa repositorios**:
```java
// Crear repositorio JpaRepository para User
// Métodos de consulta personalizados con @Query
// Consultas derivadas de nombres de métodos
```

3. **Crea los controladores REST**:
```java
// Controller con endpoints CRUD para usuarios
// Validación de entrada con @Valid
// Manejo de excepciones con @ControllerAdvice
```

4. **Añade servicios**:
```java
// Capa de servicio con lógica de negocio
// Transacciones con @Transactional
// Mapeo entre entidades y DTOs
```

### 🔧 Funcionalidades a implementar
- CRUD completo para usuarios
- Paginación y ordenamiento
- Búsqueda con criterios múltiples
- Validaciones personalizadas
- Manejo de errores HTTP
- Documentación con OpenAPI/Swagger

---

## 🏗️ Ejemplo 3: Microservicios Básicos

### Objetivo
Crear un sistema de microservicios simple con Spring Cloud, demostrando comunicación entre servicios y configuración distribuida.

### Arquitectura
```
├── config-server     # Servidor de configuración
├── eureka-server     # Service Discovery
├── user-service      # Microservicio de usuarios
├── product-service   # Microservicio de productos
└── gateway-service   # API Gateway
```

### Instrucciones paso a paso

1. **Configurar Eureka Server**:
```java
// Aplicación Spring Boot con @EnableEurekaServer
// Configuración para service discovery
```

2. **Crear microservicios**:
```java
// Microservicio con @EnableEurekaClient
// Cliente REST con OpenFeign
// Circuit breaker con Hystrix
```

3. **Implementar API Gateway**:
```java
// Gateway con Spring Cloud Gateway
// Rutas dinámicas y filtros
// Load balancing automático
```

### 📊 Conceptos a explorar
- Service Discovery con Eureka
- Configuration Server
- Circuit Breaker pattern
- Distributed tracing
- API Gateway routing

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **Sistema de Autenticación JWT**
   ```java
   // Implementar autenticación JWT con Spring Security
   ```

2. **Procesamiento de Archivos**
   ```java
   // Leer y procesar archivos CSV/Excel con Apache POI
   ```

3. **Tests Unitarios y de Integración**
   ```java
   // Crear tests con JUnit 5, Mockito y TestContainers
   ```

4. **Programación Reactiva**
   ```java
   // API reactiva con Spring WebFlux y Project Reactor
   ```

5. **Mensajería Asíncrona**
   ```java
   // Implementar messaging con RabbitMQ o Apache Kafka
   ```

## 💡 Tips específicos para Java y Copilot

1. **Anotaciones descriptivas**: Usa anotaciones estándar como `@Component`, `@Service`, `@Repository`
2. **Javadoc completo**: Copilot genera mejor código con documentación clara
3. **Nombres descriptivos**: Usa convenciones de nombres Java estándar
4. **Patrones de diseño**: Menciona patrones específicos en comentarios
5. **Frameworks**: Especifica qué framework usar (Spring, Hibernate, etc.)

### Ejemplos de comentarios efectivos:
```java
// Clase que implementa el patrón Repository para gestionar entidades User
// Método que encuentra usuarios activos usando Spring Data JPA criteria
// Controlador REST que maneja operaciones CRUD con validaciones Bean Validation
// Servicio transaccional que procesa pagos con rollback automático
// Cliente Feign para comunicación síncrona entre microservicios
```

### Estructura de proyecto recomendada:
```
src/main/java/com/tutorial/copilot/
├── controller/     # Controladores REST
├── service/        # Lógica de negocio
├── repository/     # Acceso a datos
├── model/          # Entidades/DTOs
├── config/         # Configuraciones
├── exception/      # Manejo de excepciones
└── util/           # Utilidades
```

---

¡Explora cada ejemplo y experimenta con diferentes comentarios para descubrir todo el potencial de Java con GitHub Copilot! ☕✨