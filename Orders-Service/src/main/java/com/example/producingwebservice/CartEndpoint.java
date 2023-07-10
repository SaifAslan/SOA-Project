package com.example.producingwebservice;

import com.example.producingwebservice.model.Cart_items;
import com.example.producingwebservice.model.Carts;

import com.example.producingwebservice.repo.Cart_itemRepo;
import io.spring.guides.gs_producing_web_service_cart.CartItem;
import io.spring.guides.gs_producing_web_service_cart.PostCartRequest;
import io.spring.guides.gs_producing_web_service_cart.PostCartResponse;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import java.util.ArrayList;
import java.util.List;


@Endpoint
public class CartEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/gs-producing-web-service-cart";

    @Autowired
    Cart_itemRepo repo_cart;

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "postCartRequest")
    @ResponsePayload
    @Transactional
    public PostCartResponse postCart(@RequestPayload PostCartRequest request) {
        PostCartResponse response = new PostCartResponse();
        Carts carts = new Carts();
        carts.setUser_id(request.getCartSubmissionRequest().getUserId());


        System.out.println("The value of cartId " + carts.getUser_id());
//        Cart_items cart_items = new Cart_items();
        List<CartItem> cartItem = request.getCartSubmissionRequest().getCartItem();
        List<Cart_items> cart_items = new ArrayList<>();

        for (CartItem cartItem1 : cartItem) {
            Cart_items cartItemsEntity = convertCartItemToCartItems(cartItem1);
            cartItemsEntity.setCart(carts);
            cart_items.add(cartItemsEntity);

        }



        cart_items.get(0).getCart().getCart_id();
        System.out.println("This is the cart_item " + cart_items.get(0).getCart().getUser_id());

        repo_cart.saveAll(cart_items);

        response.setCartSubmissionRequest(request.getCartSubmissionRequest());
        response.setMessage("Success");

        return response;
    }

    public Cart_items convertCartItemToCartItems(CartItem cartItem) {
        Cart_items cartItemsEntity = new Cart_items();
        cartItemsEntity.setProduct_id(cartItem.getProductId());
        cartItemsEntity.setQuantity(cartItem.getQuantity());
        cartItemsEntity.setAmount(cartItem.getAmount());

        System.out.println("this is inside the method" + cartItemsEntity.getProduct_id());
        // Set other properties as needed
        return cartItemsEntity;
    }
}