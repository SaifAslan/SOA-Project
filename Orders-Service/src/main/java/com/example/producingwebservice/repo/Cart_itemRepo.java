package com.example.producingwebservice.repo;

import com.example.producingwebservice.model.Cart_items;
import org.springframework.data.jpa.repository.JpaRepository;

public interface Cart_itemRepo extends JpaRepository<Cart_items, Long> {
}
