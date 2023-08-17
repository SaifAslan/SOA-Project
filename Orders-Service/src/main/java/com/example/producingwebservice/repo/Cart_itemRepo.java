package com.example.producingwebservice.repo;

import com.example.producingwebservice.model.Cart_items;
import com.example.producingwebservice.model.Carts;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface Cart_itemRepo extends JpaRepository<Cart_items, Long> {

    List<Cart_items> findByCart(Carts cart);
}
