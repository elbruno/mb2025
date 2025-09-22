# Ejemplos de GitHub Copilot para TypeScript

Esta carpeta contiene ejemplos progresivos para aprender a usar GitHub Copilot con TypeScript.

## 📚 Contenido

1. [Ejemplo Básico: Calculadora Type-Safe](#ejemplo-1-calculadora-type-safe)
2. [Ejemplo Intermedio: API Express con TypeScript](#ejemplo-2-api-express-con-typescript)
3. [Ejemplo Avanzado: Full-Stack App](#ejemplo-3-aplicación-full-stack-react--nodejs)

## Prerequisitos

- Node.js 16.0 o superior
- npm o yarn
- Visual Studio Code con extensión de TypeScript
- GitHub Copilot habilitado

```bash
# Instalar TypeScript globalmente
npm install -g typescript ts-node

# Verificar instalación
tsc --version
ts-node --version
```

## 🧮 Ejemplo 1: Calculadora Type-Safe

### Objetivo
Crear una calculadora con tipos estrictos, interfaces y validaciones usando TypeScript.

### Configuración inicial
```bash
npm init -y
npm install -D typescript @types/node ts-node
npx tsc --init
```

### Instrucciones paso a paso

1. **Define interfaces y tipos**:
```typescript
// Interface para operaciones matemáticas
// Type union para operadores válidos
// Interface para resultado de cálculo con error handling
```

2. **Implementa clase Calculator con tipos**:
```typescript
// Clase Calculator con métodos tipados
// Validaciones de entrada con type guards
// Manejo de errores con custom types
```

3. **Crea funciones utilitarias tipadas**:
```typescript
// Función para validar números
// Función para formatear resultados
// Función para historial de operaciones
```

### 💡 Tips para este ejemplo
- Usa tipos específicos como `number | null` en lugar de `any`
- Copilot generará automáticamente interfaces basadas en uso
- Aprovecha IntelliSense mejorado con tipos estrictos

### 🎯 Características TypeScript a explorar
- Interfaces y tipos personalizados
- Type guards y narrowing
- Generic types
- Union y intersection types
- Utility types (Partial, Pick, Omit)

---

## 🌐 Ejemplo 2: API Express con TypeScript

### Objetivo
Crear una API REST type-safe con Express, validaciones y decoradores.

### Configuración inicial
```bash
npm init -y
npm install express cors helmet morgan
npm install -D typescript @types/node @types/express ts-node nodemon
npm install class-validator class-transformer reflect-metadata
```

### Instrucciones paso a paso

1. **Configura TypeScript estricto**:
```typescript
// Configuración tsconfig.json con strict mode
// Setup de paths y module resolution
```

2. **Define modelos con decoradores**:
```typescript
// Modelo User con validaciones class-validator
// Modelo Product con relaciones tipadas
// DTOs para request/response
```

3. **Implementa controladores tipados**:
```typescript
// Controlador base con generic types
// Controladores específicos con type safety
// Middleware personalizado con tipos
```

4. **Crea servicios con dependency injection**:
```typescript
// Service layer con interfaces
// Repository pattern con generics
// Error handling tipado
```

### 🔧 Funcionalidades a implementar
- CRUD con tipos estrictos
- Validación automática de DTOs
- Manejo de errores tipado
- Middleware personalizado
- Documentación automática de tipos
- Testing con tipos

### 📊 Arquitectura TypeScript
```
src/
├── controllers/     # Controladores REST
├── services/        # Lógica de negocio
├── models/          # Modelos y DTOs
├── middleware/      # Middleware personalizado
├── types/           # Definiciones de tipos
├── utils/           # Utilidades tipadas
└── tests/           # Tests con tipos
```

---

## ⚛️ Ejemplo 3: Aplicación Full-Stack React + Node.js

### Objetivo
Crear una aplicación completa full-stack con TypeScript en frontend y backend compartiendo tipos.

### Configuración inicial
```bash
# Backend
mkdir backend && cd backend
npm init -y
npm install express cors helmet morgan jsonwebtoken bcryptjs
npm install -D typescript @types/* ts-node nodemon

# Frontend  
npx create-react-app frontend --template typescript
cd frontend
npm install axios react-router-dom @reduxjs/toolkit react-redux
```

### Instrucciones paso a paso

1. **Configura workspace compartido**:
```typescript
// Shared types package para frontend/backend
// Configuración monorepo con workspaces
// Scripts para desarrollo simultáneo
```

2. **Backend con autenticación tipada**:
```typescript
// JWT tokens con custom payload types
// User authentication con type guards
// Protected routes con middleware tipado
```

3. **Frontend React con hooks tipados**:
```typescript
// Custom hooks con generic types
// Redux store completamente tipado
// API client con tipos automáticos
```

4. **Compartir tipos entre frontend/backend**:
```typescript
// Shared models y DTOs
// API response types
// Form validation types
```

### 🚀 Funcionalidades avanzadas
- Autenticación JWT end-to-end tipada
- Real-time WebSocket con tipos
- File upload con progress tracking
- Infinite scrolling tipado
- Form handling con validation
- Error boundaries tipados

### 🔄 Patrones TypeScript avanzados
- Higher-order components tipados
- Render props con generics
- Custom hooks con complex types
- Context API completamente tipado
- Redux con RTK Query y tipos automáticos

---

## 🚀 Ejercicios Adicionales

### Para practicar más con GitHub Copilot:

1. **GraphQL con TypeScript**
   ```typescript
   // GraphQL resolvers con type safety
   // Code generation automático
   ```

2. **Microservicios tipados**
   ```typescript
   // Servicios independientes con tipos compartidos
   // Message queues con type safety
   ```

3. **Testing avanzado**
   ```typescript
   // Unit tests con type checking
   // Integration tests tipados
   // Mock factories con generics
   ```

4. **Performance optimization**
   ```typescript
   // Lazy loading con tipos
   // Memory optimization patterns
   // Bundle analysis con TypeScript
   ```

5. **DevOps con tipos**
   ```typescript
   // CI/CD pipelines tipados
   // Configuration as code
   // Deployment scripts con type safety
   ```

## 💡 Tips específicos para TypeScript y Copilot

1. **Usa strict mode**: Habilita todas las opciones strict en tsconfig.json
2. **Define interfaces primero**: Copilot genera mejor código con interfaces claras
3. **Aprovecha type inference**: Deja que TypeScript infiera cuando sea obvio
4. **Usa utility types**: Partial, Pick, Omit, Record para manipular tipos
5. **Comenta tipos complejos**: "// Generic function that takes T and returns Promise<T[]>"

### 🎯 Mejores prácticas para Copilot + TypeScript
- Usa nombres descriptivos para tipos e interfaces
- Separa tipos en archivos .d.ts cuando sea apropiado
- Aprovecha discriminated unions para type safety
- Usa const assertions para literal types
- Implementa branded types para seguridad adicional

### 🔧 Configuración recomendada tsconfig.json
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```

---

¡Explora cada ejemplo y descubre cómo TypeScript + GitHub Copilot crean código más seguro y mantenible! 🚀⚡