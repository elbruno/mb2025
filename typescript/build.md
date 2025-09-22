# Instrucciones de construcción para TypeScript

## Prerequisitos
- Node.js 16.0 o superior
- npm o yarn
- TypeScript instalado globalmente: `npm install -g typescript`

## Instalación de dependencias
```bash
npm install
```

## Compilación y ejecución

### Ejemplo 1: Calculadora Type-Safe
```bash
# Compilar TypeScript a JavaScript
npm run build

# Ejecutar calculadora directamente con ts-node
npm run dev

# O compilar y ejecutar
tsc calculator.ts
node calculator.js
```

### Ejemplo 2: Express API con TypeScript
```bash
# Instalar dependencias
npm install

# Modo desarrollo con auto-reload y TypeScript
npm run dev:watch

# Compilar para producción
npm run build

# Ejecutar version compilada
npm start

# Verificar tipos sin compilar
npm run type-check
```

## Comandos útiles
```bash
# Verificar tipos sin compilar
tsc --noEmit

# Compilar con watch mode
tsc --watch

# Linting (si está configurado)
npm run lint

# Tests con tipos
npm test
```

## Configuración TypeScript
El archivo `tsconfig.json` está configurado con:
- Strict mode habilitado
- Decorators experimentales
- Source maps para debugging
- Verificaciones estrictas de tipos

## Testing con tipos
```bash
# Instalar dependencias de testing
npm install --save-dev jest @types/jest supertest @types/supertest

# Ejecutar tests
npm test
```