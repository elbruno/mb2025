package com.tutorial.copilot;

import com.tutorial.copilot.model.Category;
import com.tutorial.copilot.model.Product;
import com.tutorial.copilot.service.InventoryManager;

import java.math.BigDecimal;
import java.util.List;
import java.util.Map;
import java.util.Optional;

// Programa principal para demostrar los ejemplos de GitHub Copilot en Java
public class CopilotTutorialMain {
    
    public static void main(String[] args) {
        System.out.println("=== GitHub Copilot Tutorial - Ejemplos en Java ===\n");
        
        // Crear instancia del gestor de inventario
        InventoryManager inventoryManager = new InventoryManager();
        
        // Demostrar funcionalidades básicas
        demonstrateBasicOperations(inventoryManager);
        
        System.out.println("\n" + "=".repeat(60) + "\n");
        
        // Demostrar búsquedas avanzadas
        demonstrateAdvancedSearch(inventoryManager);
        
        System.out.println("\n" + "=".repeat(60) + "\n");
        
        // Demostrar reportes y estadísticas
        demonstrateReportsAndStatistics(inventoryManager);
        
        System.out.println("\n" + "=".repeat(60) + "\n");
        
        // Demostrar operaciones de stock
        demonstrateStockOperations(inventoryManager);
    }
    
    // Método para demostrar operaciones básicas del inventario
    private static void demonstrateBasicOperations(InventoryManager manager) {
        System.out.println("📦 OPERACIONES BÁSICAS DE INVENTARIO");
        System.out.println("====================================\n");
        
        // Mostrar productos iniciales
        System.out.println("📋 Productos en inventario:");
        List<Product> allProducts = manager.getAllActiveProducts();
        allProducts.forEach(product -> 
            System.out.printf("  • [%d] %s - $%.2f (Stock: %d)%n", 
                product.getId(), product.getName(), product.getPrice(), product.getQuantity())
        );
        
        // Añadir un nuevo producto
        System.out.println("\n➕ Añadiendo nuevo producto...");
        Product newProduct = Product.builder()
                .name("AirPods Pro")
                .description("Auriculares inalámbricos con cancelación de ruido")
                .price(249.99)
                .quantity(15)
                .category(Category.ELECTRONICS)
                .brand("Apple")
                .build();
        
        manager.addProduct(newProduct);
        System.out.printf("   Producto añadido: %s%n", newProduct.getName());
        
        // Buscar producto por ID
        System.out.println("\n🔍 Buscando producto por ID...");
        Optional<Product> foundProduct = manager.findProductById(1L);
        if (foundProduct.isPresent()) {
            Product product = foundProduct.get();
            System.out.printf("   Encontrado: %s - $%.2f%n", product.getName(), product.getPrice());
        }
        
        // Actualizar producto
        System.out.println("\n✏️ Actualizando precio de producto...");
        if (foundProduct.isPresent()) {
            Product productToUpdate = foundProduct.get();
            productToUpdate.setPrice(BigDecimal.valueOf(899.99));
            manager.updateProduct(productToUpdate.getId(), productToUpdate);
            System.out.printf("   Precio actualizado a: $%.2f%n", productToUpdate.getPrice());
        }
    }
    
    // Método para demostrar búsquedas avanzadas
    private static void demonstrateAdvancedSearch(InventoryManager manager) {
        System.out.println("🔍 BÚSQUEDAS AVANZADAS");
        System.out.println("======================\n");
        
        // Buscar por rango de precio
        System.out.println("💰 Productos entre $30 y $100:");
        List<Product> priceRangeProducts = manager.findProductsByPriceRange(
                BigDecimal.valueOf(30), BigDecimal.valueOf(100)
        );
        priceRangeProducts.forEach(product -> 
            System.out.printf("  • %s - $%.2f%n", product.getName(), product.getPrice())
        );
        
        // Buscar por categoría
        System.out.println("\n📱 Productos de categoría ELECTRONICS:");
        List<Product> electronicsProducts = manager.findProductsByCategory(Category.ELECTRONICS);
        electronicsProducts.forEach(product -> 
            System.out.printf("  • %s (%s) - $%.2f%n", 
                product.getName(), product.getBrand(), product.getPrice())
        );
        
        // Buscar por nombre
        System.out.println("\n📝 Productos que contienen 'book':");
        List<Product> nameSearchProducts = manager.searchProductsByName("book");
        nameSearchProducts.forEach(product -> 
            System.out.printf("  • %s - $%.2f%n", product.getName(), product.getPrice())
        );
        
        // Buscar por marca
        System.out.println("\n🏷️ Productos de marca Apple:");
        List<Product> appleProducts = manager.findProductsByBrand("Apple");
        appleProducts.forEach(product -> 
            System.out.printf("  • %s - $%.2f (Stock: %d)%n", 
                product.getName(), product.getPrice(), product.getQuantity())
        );
        
        // Búsqueda con múltiples criterios
        System.out.println("\n🎯 Búsqueda avanzada (Electrónicos, precio < $1000):");
        List<Product> advancedSearchResults = manager.searchProducts(
                null, Category.ELECTRONICS, null, null, BigDecimal.valueOf(1000)
        );
        advancedSearchResults.forEach(product -> 
            System.out.printf("  • %s (%s) - $%.2f%n", 
                product.getName(), product.getBrand(), product.getPrice())
        );
    }
    
    // Método para demostrar reportes y estadísticas
    private static void demonstrateReportsAndStatistics(InventoryManager manager) {
        System.out.println("📊 REPORTES Y ESTADÍSTICAS");
        System.out.println("==========================\n");
        
        // Estadísticas generales
        System.out.println("📈 Estadísticas generales del inventario:");
        InventoryManager.InventoryStatistics stats = manager.calculateStatistics();
        System.out.printf("  • Total de productos: %d%n", stats.getTotalProducts());
        System.out.printf("  • Cantidad total en stock: %d%n", stats.getTotalQuantity());
        System.out.printf("  • Valor total del inventario: $%.2f%n", stats.getTotalValue());
        System.out.printf("  • Precio promedio: $%.2f%n", stats.getAveragePrice());
        System.out.printf("  • Número de categorías: %d%n", stats.getCategoriesCount());
        System.out.printf("  • Número de marcas: %d%n", stats.getBrandsCount());
        
        // Reporte por categoría
        System.out.println("\n📋 Reporte de inventario por categoría:");
        Map<Category, List<Product>> categoryReport = manager.generateInventoryReportByCategory();
        for (Map.Entry<Category, List<Product>> entry : categoryReport.entrySet()) {
            System.out.printf("  🏷️ %s (%d productos):%n", 
                entry.getKey().getDisplayName(), entry.getValue().size());
            entry.getValue().forEach(product -> 
                System.out.printf("     • %s (Stock: %d)%n", product.getName(), product.getQuantity())
            );
        }
        
        // Reporte de valor por categoría
        System.out.println("\n💰 Valor de inventario por categoría:");
        Map<Category, BigDecimal> valueReport = manager.generateValueReportByCategory();
        for (Map.Entry<Category, BigDecimal> entry : valueReport.entrySet()) {
            System.out.printf("  • %s: $%.2f%n", 
                entry.getKey().getDisplayName(), entry.getValue());
        }
        
        // Productos más caros
        System.out.println("\n💎 Top 3 productos más caros:");
        List<Product> expensiveProducts = manager.getTopExpensiveProducts(3);
        for (int i = 0; i < expensiveProducts.size(); i++) {
            Product product = expensiveProducts.get(i);
            System.out.printf("  %d. %s - $%.2f%n", 
                i + 1, product.getName(), product.getPrice());
        }
    }
    
    // Método para demostrar operaciones de stock
    private static void demonstrateStockOperations(InventoryManager manager) {
        System.out.println("📦 OPERACIONES DE STOCK");
        System.out.println("=======================\n");
        
        // Mostrar productos con stock bajo
        System.out.println("⚠️ Productos con stock bajo (menos de 30 unidades):");
        List<Product> lowStockProducts = manager.findLowStockProducts(30);
        if (lowStockProducts.isEmpty()) {
            System.out.println("  ✅ No hay productos con stock bajo");
        } else {
            lowStockProducts.forEach(product -> 
                System.out.printf("  • %s - Stock: %d unidades%n", 
                    product.getName(), product.getQuantity())
            );
        }
        
        // Mostrar productos sin stock
        System.out.println("\n❌ Productos sin stock:");
        List<Product> outOfStockProducts = manager.findOutOfStockProducts();
        if (outOfStockProducts.isEmpty()) {
            System.out.println("  ✅ Todos los productos tienen stock disponible");
        } else {
            outOfStockProducts.forEach(product -> 
                System.out.printf("  • %s - SIN STOCK%n", product.getName())
            );
        }
        
        // Demostrar operaciones de stock en un producto específico
        System.out.println("\n🔄 Operaciones de stock - Ejemplo con iPhone 14:");
        Optional<Product> iphoneOpt = manager.getAllActiveProducts().stream()
                .filter(p -> p.getName().contains("iPhone"))
                .findFirst();
        
        if (iphoneOpt.isPresent()) {
            Product iphone = iphoneOpt.get();
            System.out.printf("  Stock inicial: %d unidades%n", iphone.getQuantity());
            
            // Reducir stock
            boolean stockReduced = iphone.reduceStock(5);
            if (stockReduced) {
                System.out.printf("  ✅ Vendidas 5 unidades. Stock actual: %d%n", iphone.getQuantity());
            }
            
            // Añadir stock
            iphone.addStock(10);
            System.out.printf("  ✅ Recibidas 10 unidades. Stock actual: %d%n", iphone.getQuantity());
            
            // Verificar estado del stock
            System.out.printf("  📊 Estado del producto:%n");
            System.out.printf("     • En stock: %s%n", iphone.isInStock() ? "Sí" : "No");
            System.out.printf("     • Stock bajo (< 20): %s%n", iphone.isLowStock(20) ? "Sí" : "No");
            System.out.printf("     • Valor total: $%.2f%n", iphone.getTotalValue());
        }
        
        // Resumen final
        System.out.println("\n📋 Resumen final del inventario:");
        System.out.printf("  • Total de productos activos: %d%n", manager.getActiveProductCount());
        System.out.printf("  • Total de productos en sistema: %d%n", manager.getTotalProductCount());
        
        InventoryManager.InventoryStatistics finalStats = manager.calculateStatistics();
        System.out.printf("  • Valor total del inventario: $%.2f%n", finalStats.getTotalValue());
    }
}