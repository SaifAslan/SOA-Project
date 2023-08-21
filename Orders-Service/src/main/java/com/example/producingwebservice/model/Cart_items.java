package com.example.producingwebservice.model;


import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "cart_items")
public class Cart_items {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "cart_item_id")
    private long cart_item_id;

    @ManyToOne(cascade = CascadeType.PERSIST)
    @JoinColumn(name = "cart_id", referencedColumnName = "cart_id")
    private Carts cart;

    private String product_id;
    private String name;
    private int quantity;
    private double amount;
}


