package com.tutorial.copilot.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.Objects;

// Crear clase Product con propiedades id, name, price, quantity, category
public class Product {
    private Long id;
    private String name;
    private String description;
    private BigDecimal price;
    private Integer quantity;
    private Category category;
    private String brand;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private boolean active;
    
    // Constructor vacío
    public Product() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
        this.active = true;
    }
    
    // Constructor con parámetros básicos
    public Product(String name, BigDecimal price, Integer quantity, Category category) {
        this();
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.category = category;
    }
    
    // Constructor completo
    public Product(Long id, String name, String description, BigDecimal price, 
                   Integer quantity, Category category, String brand) {
        this();
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.quantity = quantity;
        this.category = category;
        this.brand = brand;
    }
    
    // Getters y Setters
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
        this.updatedAt = LocalDateTime.now();
    }
    
    public BigDecimal getPrice() {
        return price;
    }
    
    public void setPrice(BigDecimal price) {
        this.price = price;
        this.updatedAt = LocalDateTime.now();
    }
    
    public Integer getQuantity() {
        return quantity;
    }
    
    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
        this.updatedAt = LocalDateTime.now();
    }
    
    public Category getCategory() {
        return category;
    }
    
    public void setCategory(Category category) {
        this.category = category;
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getBrand() {
        return brand;
    }
    
    public void setBrand(String brand) {
        this.brand = brand;
        this.updatedAt = LocalDateTime.now();
    }
    
    public LocalDateTime getCreatedAt() {
        return createdAt;
    }
    
    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }
    
    public boolean isActive() {
        return active;
    }
    
    public void setActive(boolean active) {
        this.active = active;
        this.updatedAt = LocalDateTime.now();
    }
    
    // Métodos de negocio
    
    // Método para verificar si el producto está en stock
    public boolean isInStock() {
        return quantity != null && quantity > 0;
    }
    
    // Método para calcular el valor total del inventario de este producto
    public BigDecimal getTotalValue() {
        if (price == null || quantity == null) {
            return BigDecimal.ZERO;
        }
        return price.multiply(BigDecimal.valueOf(quantity));
    }
    
    // Método para verificar si el producto tiene stock bajo
    public boolean isLowStock(int threshold) {
        return quantity != null && quantity <= threshold;
    }
    
    // Método para añadir stock
    public void addStock(int amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("La cantidad a añadir debe ser positiva");
        }
        this.quantity = (this.quantity == null ? 0 : this.quantity) + amount;
        this.updatedAt = LocalDateTime.now();
    }
    
    // Método para reducir stock
    public boolean reduceStock(int amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("La cantidad a reducir debe ser positiva");
        }
        if (this.quantity == null || this.quantity < amount) {
            return false; // No hay suficiente stock
        }
        this.quantity -= amount;
        this.updatedAt = LocalDateTime.now();
        return true;
    }
    
    // Implementar métodos equals, hashCode y toString
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Product product = (Product) obj;
        return Objects.equals(id, product.id) &&
               Objects.equals(name, product.name) &&
               Objects.equals(price, product.price) &&
               category == product.category;
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(id, name, price, category);
    }
    
    @Override
    public String toString() {
        return String.format("Product{id=%d, name='%s', price=%s, quantity=%d, category=%s, brand='%s', active=%s}",
                id, name, price, quantity, category, brand, active);
    }
    
    // Builder pattern para crear productos
    public static class Builder {
        private Long id;
        private String name;
        private String description;
        private BigDecimal price;
        private Integer quantity;
        private Category category;
        private String brand;
        
        public Builder id(Long id) {
            this.id = id;
            return this;
        }
        
        public Builder name(String name) {
            this.name = name;
            return this;
        }
        
        public Builder description(String description) {
            this.description = description;
            return this;
        }
        
        public Builder price(BigDecimal price) {
            this.price = price;
            return this;
        }
        
        public Builder price(double price) {
            this.price = BigDecimal.valueOf(price);
            return this;
        }
        
        public Builder quantity(Integer quantity) {
            this.quantity = quantity;
            return this;
        }
        
        public Builder category(Category category) {
            this.category = category;
            return this;
        }
        
        public Builder brand(String brand) {
            this.brand = brand;
            return this;
        }
        
        public Product build() {
            Product product = new Product();
            product.id = this.id;
            product.name = this.name;
            product.description = this.description;
            product.price = this.price;
            product.quantity = this.quantity;
            product.category = this.category;
            product.brand = this.brand;
            return product;
        }
    }
    
    public static Builder builder() {
        return new Builder();
    }
}