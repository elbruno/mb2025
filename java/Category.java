package com.tutorial.copilot.model;

// Crear enumeración Category para categorizar productos
public enum Category {
    ELECTRONICS("Electrónicos"),
    CLOTHING("Ropa"),
    BOOKS("Libros"),
    FOOD("Alimentos"),
    HOME("Hogar"),
    SPORTS("Deportes"),
    TOYS("Juguetes");
    
    private final String displayName;
    
    Category(String displayName) {
        this.displayName = displayName;
    }
    
    public String getDisplayName() {
        return displayName;
    }
    
    @Override
    public String toString() {
        return displayName;
    }
}