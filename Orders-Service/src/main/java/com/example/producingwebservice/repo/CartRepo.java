package com.example.producingwebservice.repo;

import com.example.producingwebservice.model.Carts;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CartRepo extends JpaRepository<Carts, Long> {

    List<Carts> findByStatus(String status);


    List<Carts> findByUserIdAndStatus(String userId, String status);

    List<Carts> findByUserId(String userId);
}
