package com.example.producingwebservice.repo;

import com.example.producingwebservice.model.Carts;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CartRepo extends JpaRepository<Carts, Long> {
}
