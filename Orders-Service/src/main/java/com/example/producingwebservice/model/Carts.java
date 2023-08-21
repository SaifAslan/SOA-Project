package com.example.producingwebservice.model;


import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "carts")
public class Carts {
    @Id
//    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "cart_id")
    private long cart_id;
    @Column(name = "user_id", nullable = false)
    private String userId;
    @Column(name = "status", nullable = false)
    private String status;
}
