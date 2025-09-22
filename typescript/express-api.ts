// GitHub Copilot Tutorial - Express API with TypeScript
// API REST completamente tipada con validaciones y manejo de errores

import express, { Request, Response, NextFunction } from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import { IsString, IsNumber, IsBoolean, IsOptional, Min, Max, Length, validate } from 'class-validator';
import { Transform, plainToClass } from 'class-transformer';
import 'reflect-metadata';

// Interfaces y tipos base
interface ApiResponse<T> {
    success: boolean;
    data?: T;
    error?: string;
    message?: string;
    pagination?: PaginationInfo;
}

interface PaginationInfo {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
}

interface RequestWithUser extends Request {
    user?: User;
}

// DTOs para validación
class CreateUserDto {
    @IsString()
    @Length(2, 50)
    name!: string;

    @IsString()
    @Length(5, 100)
    email!: string;

    @IsNumber()
    @Min(18)
    @Max(120)
    age!: number;

    @IsOptional()
    @IsString()
    department?: string;
}

class UpdateUserDto {
    @IsOptional()
    @IsString()
    @Length(2, 50)
    name?: string;

    @IsOptional()
    @IsNumber()
    @Min(18)
    @Max(120)
    age?: number;

    @IsOptional()
    @IsString()
    department?: string;
}

class CreateProductDto {
    @IsString()
    @Length(1, 100)
    name!: string;

    @IsString()
    @Length(10, 500)
    description!: string;

    @IsNumber()
    @Min(0)
    price!: number;

    @IsString()
    category!: string;

    @IsOptional()
    @IsBoolean()
    available?: boolean;
}

// Modelos de dominio
class User {
    id!: number;
    name!: string;
    email!: string;
    age!: number;
    department?: string;
    createdAt!: Date;
    updatedAt!: Date;

    constructor(data: Partial<User>) {
        Object.assign(this, data);
    }
}

class Product {
    id!: number;
    name!: string;
    description!: string;
    price!: number;
    category!: string;
    available!: boolean;
    createdAt!: Date;
    updatedAt!: Date;

    constructor(data: Partial<Product>) {
        Object.assign(this, data);
    }
}

// Errores personalizados tipados
class AppError extends Error {
    constructor(
        public statusCode: number,
        public message: string,
        public isOperational: boolean = true
    ) {
        super(message);
        Error.captureStackTrace(this, this.constructor);
    }
}

class ValidationError extends AppError {
    constructor(message: string) {
        super(400, message);
    }
}

class NotFoundError extends AppError {
    constructor(resource: string) {
        super(404, `${resource} not found`);
    }
}

// Servicios tipados
class UserService {
    private users: User[] = [];
    private currentId = 1;

    async findAll(page: number = 1, limit: number = 10): Promise<{
        users: User[];
        pagination: PaginationInfo;
    }> {
        // Implementar paginación y retorno tipado
        
    }

    async findById(id: number): Promise<User> {
        // Buscar usuario por ID con manejo de errores tipado
        
    }

    async create(userData: CreateUserDto): Promise<User> {
        // Crear nuevo usuario con validación
        
    }

    async update(id: number, userData: UpdateUserDto): Promise<User> {
        // Actualizar usuario existente
        
    }

    async delete(id: number): Promise<void> {
        // Eliminar usuario con validación de existencia
        
    }

    async findByEmail(email: string): Promise<User | null> {
        // Buscar usuario por email
        
    }
}

class ProductService {
    private products: Product[] = [];
    private currentId = 1;

    async findAll(filters?: {
        category?: string;
        available?: boolean;
        minPrice?: number;
        maxPrice?: number;
    }): Promise<Product[]> {
        // Implementar filtros tipados
        
    }

    async findById(id: number): Promise<Product> {
        // Buscar producto por ID
        
    }

    async create(productData: CreateProductDto): Promise<Product> {
        // Crear nuevo producto
        
    }

    async update(id: number, productData: Partial<CreateProductDto>): Promise<Product> {
        // Actualizar producto
        
    }

    async delete(id: number): Promise<void> {
        // Eliminar producto
        
    }
}

// Controladores tipados
class UserController {
    constructor(private userService: UserService) {}

    getUsers = async (req: Request, res: Response<ApiResponse<User[]>>, next: NextFunction): Promise<void> => {
        // Implementar GET /users con paginación
        
    };

    getUserById = async (req: Request, res: Response<ApiResponse<User>>, next: NextFunction): Promise<void> => {
        // Implementar GET /users/:id
        
    };

    createUser = async (req: Request, res: Response<ApiResponse<User>>, next: NextFunction): Promise<void> => {
        // Implementar POST /users con validación
        
    };

    updateUser = async (req: Request, res: Response<ApiResponse<User>>, next: NextFunction): Promise<void> => {
        // Implementar PUT /users/:id
        
    };

    deleteUser = async (req: Request, res: Response<ApiResponse<null>>, next: NextFunction): Promise<void> => {
        // Implementar DELETE /users/:id
        
    };
}

// Middleware tipados
const validateDto = <T extends object>(DtoClass: new () => T) => {
    return async (req: Request, res: Response, next: NextFunction): Promise<void> => {
        // Middleware para validar DTOs usando class-validator
        
    };
};

const asyncHandler = (fn: Function) => {
    return (req: Request, res: Response, next: NextFunction) => {
        // Wrapper para manejar errores async
        
    };
};

const errorHandler = (err: Error, req: Request, res: Response<ApiResponse<null>>, next: NextFunction): void => {
    // Middleware de manejo de errores tipado
    
};

const notFoundHandler = (req: Request, res: Response<ApiResponse<null>>): void => {
    // Handler para rutas no encontradas
    
};

// Función para crear y configurar la aplicación
function createApp(): express.Application {
    const app = express();
    
    // Servicios
    const userService = new UserService();
    const productService = new ProductService();
    
    // Controladores
    const userController = new UserController(userService);
    
    // Middleware básico
    app.use(helmet());
    app.use(cors());
    app.use(morgan('combined'));
    app.use(express.json());
    
    // Rutas de usuarios
    app.get('/api/users', asyncHandler(userController.getUsers));
    app.get('/api/users/:id', asyncHandler(userController.getUserById));
    app.post('/api/users', validateDto(CreateUserDto), asyncHandler(userController.createUser));
    app.put('/api/users/:id', validateDto(UpdateUserDto), asyncHandler(userController.updateUser));
    app.delete('/api/users/:id', asyncHandler(userController.deleteUser));
    
    // Rutas de productos (implementar similar a usuarios)
    
    // Middleware de manejo de errores
    app.use(notFoundHandler);
    app.use(errorHandler);
    
    return app;
}

// Función para iniciar servidor
function startServer(port: number = 3000): void {
    const app = createApp();
    
    app.listen(port, () => {
        console.log(`🚀 Servidor TypeScript ejecutándose en http://localhost:${port}`);
        console.log(`📚 API endpoints disponibles:`);
        console.log(`   GET    /api/users`);
        console.log(`   GET    /api/users/:id`);
        console.log(`   POST   /api/users`);
        console.log(`   PUT    /api/users/:id`);
        console.log(`   DELETE /api/users/:id`);
    });
}

// Exportar todo para testing y reutilización
export {
    createApp,
    startServer,
    UserService,
    ProductService,
    UserController,
    CreateUserDto,
    UpdateUserDto,
    CreateProductDto,
    AppError,
    ValidationError,
    NotFoundError
};

export type {
    ApiResponse,
    PaginationInfo,
    RequestWithUser
};

// Iniciar servidor si es archivo principal
if (require.main === module) {
    startServer();
}