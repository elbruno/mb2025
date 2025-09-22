package com.tutorial.copilot.service;

import com.tutorial.copilot.model.Category;
import com.tutorial.copilot.model.Product;

import java.math.BigDecimal;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;

// Crear clase InventoryManager con lista de productos
public class InventoryManager {
    private final Map<Long, Product> products;
    private final AtomicLong idGenerator;
    
    public InventoryManager() {
        this.products = new HashMap<>();
        this.idGenerator = new AtomicLong(1);
        initializeSampleData();
    }
    
    // Inicializar con datos de ejemplo
    private void initializeSampleData() {
        addProduct(Product.builder()
                .name("iPhone 14")
                .description("Smartphone Apple con 128GB")
                .price(999.99)
                .quantity(50)
                .category(Category.ELECTRONICS)
                .brand("Apple")
                .build());
                
        addProduct(Product.builder()
                .name("Laptop Dell XPS 13")
                .description("Laptop ultrabook con Intel i7")
                .price(1299.99)
                .quantity(25)
                .category(Category.ELECTRONICS)
                .brand("Dell")
                .build());
                
        addProduct(Product.builder()
                .name("Camiseta Nike")
                .description("Camiseta deportiva Dri-FIT")
                .price(29.99)
                .quantity(100)
                .category(Category.CLOTHING)
                .brand("Nike")
                .build());
                
        addProduct(Product.builder()
                .name("Libro Java Programming")
                .description("Guía completa de programación Java")
                .price(45.99)
                .quantity(30)
                .category(Category.BOOKS)
                .brand("O'Reilly")
                .build());
    }
    
    // Métodos para añadir, eliminar, buscar y actualizar productos
    
    // Método para añadir un nuevo producto
    public Product addProduct(Product product) {
        if (product == null) {
            throw new IllegalArgumentException("El producto no puede ser nulo");
        }
        
        if (product.getId() == null) {
            product.setId(idGenerator.getAndIncrement());
        }
        
        products.put(product.getId(), product);
        System.out.println("Producto añadido: " + product.getName());
        return product;
    }
    
    // Método para eliminar un producto por ID
    public boolean removeProduct(Long productId) {
        if (productId == null) {
            return false;
        }
        
        Product removedProduct = products.remove(productId);
        if (removedProduct != null) {
            System.out.println("Producto eliminado: " + removedProduct.getName());
            return true;
        }
        return false;
    }
    
    // Método para buscar un producto por ID
    public Optional<Product> findProductById(Long productId) {
        return Optional.ofNullable(products.get(productId));
    }
    
    // Método para actualizar un producto existente
    public boolean updateProduct(Long productId, Product updatedProduct) {
        if (productId == null || updatedProduct == null) {
            return false;
        }
        
        if (products.containsKey(productId)) {
            updatedProduct.setId(productId);
            products.put(productId, updatedProduct);
            System.out.println("Producto actualizado: " + updatedProduct.getName());
            return true;
        }
        return false;
    }
    
    // Utilizar streams para filtrar y procesar productos
    
    // Método que busca productos por rango de precio usando streams
    public List<Product> findProductsByPriceRange(BigDecimal minPrice, BigDecimal maxPrice) {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> product.getPrice() != null)
                .filter(product -> product.getPrice().compareTo(minPrice) >= 0)
                .filter(product -> product.getPrice().compareTo(maxPrice) <= 0)
                .sorted(Comparator.comparing(Product::getPrice))
                .collect(Collectors.toList());
    }
    
    // Método para buscar productos por categoría
    public List<Product> findProductsByCategory(Category category) {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> product.getCategory() == category)
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Método para buscar productos por nombre (búsqueda parcial)
    public List<Product> searchProductsByName(String searchTerm) {
        if (searchTerm == null || searchTerm.trim().isEmpty()) {
            return Collections.emptyList();
        }
        
        String lowerSearchTerm = searchTerm.toLowerCase();
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> product.getName() != null)
                .filter(product -> product.getName().toLowerCase().contains(lowerSearchTerm))
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Método para buscar productos por marca
    public List<Product> findProductsByBrand(String brand) {
        if (brand == null || brand.trim().isEmpty()) {
            return Collections.emptyList();
        }
        
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> brand.equalsIgnoreCase(product.getBrand()))
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Implementar búsqueda por múltiples criterios
    public List<Product> searchProducts(String name, Category category, String brand, 
                                       BigDecimal minPrice, BigDecimal maxPrice) {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> name == null || name.trim().isEmpty() || 
                        product.getName().toLowerCase().contains(name.toLowerCase()))
                .filter(product -> category == null || product.getCategory() == category)
                .filter(product -> brand == null || brand.trim().isEmpty() || 
                        brand.equalsIgnoreCase(product.getBrand()))
                .filter(product -> minPrice == null || product.getPrice() == null || 
                        product.getPrice().compareTo(minPrice) >= 0)
                .filter(product -> maxPrice == null || product.getPrice() == null || 
                        product.getPrice().compareTo(maxPrice) <= 0)
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Método para obtener productos con stock bajo
    public List<Product> findLowStockProducts(int threshold) {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> product.isLowStock(threshold))
                .sorted(Comparator.comparing(Product::getQuantity))
                .collect(Collectors.toList());
    }
    
    // Método para obtener productos sin stock
    public List<Product> findOutOfStockProducts() {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> !product.isInStock())
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Generar reportes de inventario
    
    // Método para generar reporte de inventario por categoría
    public Map<Category, List<Product>> generateInventoryReportByCategory() {
        return products.values().stream()
                .filter(Product::isActive)
                .collect(Collectors.groupingBy(Product::getCategory));
    }
    
    // Método para generar reporte de valor de inventario por categoría
    public Map<Category, BigDecimal> generateValueReportByCategory() {
        return products.values().stream()
                .filter(Product::isActive)
                .collect(Collectors.groupingBy(
                        Product::getCategory,
                        Collectors.reducing(BigDecimal.ZERO, Product::getTotalValue, BigDecimal::add)
                ));
    }
    
    // Calcular estadísticas de productos
    
    // Método para calcular estadísticas básicas del inventario
    public InventoryStatistics calculateStatistics() {
        List<Product> activeProducts = products.values().stream()
                .filter(Product::isActive)
                .collect(Collectors.toList());
        
        if (activeProducts.isEmpty()) {
            return new InventoryStatistics();
        }
        
        int totalProducts = activeProducts.size();
        int totalQuantity = activeProducts.stream()
                .mapToInt(product -> product.getQuantity() != null ? product.getQuantity() : 0)
                .sum();
        
        BigDecimal totalValue = activeProducts.stream()
                .map(Product::getTotalValue)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
        
        OptionalDouble averagePrice = activeProducts.stream()
                .filter(product -> product.getPrice() != null)
                .mapToDouble(product -> product.getPrice().doubleValue())
                .average();
        
        long categoriesCount = activeProducts.stream()
                .map(Product::getCategory)
                .distinct()
                .count();
        
        long brandsCount = activeProducts.stream()
                .map(Product::getBrand)
                .filter(Objects::nonNull)
                .distinct()
                .count();
        
        return new InventoryStatistics(
                totalProducts,
                totalQuantity,
                totalValue,
                averagePrice.orElse(0.0),
                (int) categoriesCount,
                (int) brandsCount
        );
    }
    
    // Método para obtener los productos más caros
    public List<Product> getTopExpensiveProducts(int limit) {
        return products.values().stream()
                .filter(Product::isActive)
                .filter(product -> product.getPrice() != null)
                .sorted(Comparator.comparing(Product::getPrice).reversed())
                .limit(limit)
                .collect(Collectors.toList());
    }
    
    // Método para obtener todos los productos activos
    public List<Product> getAllActiveProducts() {
        return products.values().stream()
                .filter(Product::isActive)
                .sorted(Comparator.comparing(Product::getName))
                .collect(Collectors.toList());
    }
    
    // Método para obtener el número total de productos
    public int getTotalProductCount() {
        return products.size();
    }
    
    // Método para obtener el número de productos activos
    public int getActiveProductCount() {
        return (int) products.values().stream()
                .filter(Product::isActive)
                .count();
    }
    
    // Clase interna para estadísticas de inventario
    public static class InventoryStatistics {
        private final int totalProducts;
        private final int totalQuantity;
        private final BigDecimal totalValue;
        private final double averagePrice;
        private final int categoriesCount;
        private final int brandsCount;
        
        public InventoryStatistics() {
            this(0, 0, BigDecimal.ZERO, 0.0, 0, 0);
        }
        
        public InventoryStatistics(int totalProducts, int totalQuantity, BigDecimal totalValue,
                                 double averagePrice, int categoriesCount, int brandsCount) {
            this.totalProducts = totalProducts;
            this.totalQuantity = totalQuantity;
            this.totalValue = totalValue;
            this.averagePrice = averagePrice;
            this.categoriesCount = categoriesCount;
            this.brandsCount = brandsCount;
        }
        
        // Getters
        public int getTotalProducts() { return totalProducts; }
        public int getTotalQuantity() { return totalQuantity; }
        public BigDecimal getTotalValue() { return totalValue; }
        public double getAveragePrice() { return averagePrice; }
        public int getCategoriesCount() { return categoriesCount; }
        public int getBrandsCount() { return brandsCount; }
        
        @Override
        public String toString() {
            return String.format(
                "InventoryStatistics{totalProducts=%d, totalQuantity=%d, totalValue=%s, " +
                "averagePrice=%.2f, categoriesCount=%d, brandsCount=%d}",
                totalProducts, totalQuantity, totalValue, averagePrice, categoriesCount, brandsCount
            );
        }
    }
}