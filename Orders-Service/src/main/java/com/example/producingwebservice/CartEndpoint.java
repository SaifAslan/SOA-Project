package com.example.producingwebservice;

import com.example.producingwebservice.model.Cart_items;
import com.example.producingwebservice.model.Carts;

import com.example.producingwebservice.repo.CartRepo;
import com.example.producingwebservice.repo.Cart_itemRepo;
import io.spring.guides.gs_producing_web_service_cart.*;

import jakarta.transaction.Transactional;

import org.hibernate.JDBCException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;


import java.sql.SQLException;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.List;


@Endpoint
public class CartEndpoint {

    private List<Carts> cartsList;
    private static final String NAMESPACE_URI = "http://spring.io/guides/gs-producing-web-service-cart";

    private boolean flag;

    @Autowired
    Cart_itemRepo repo_cart;
    @Autowired
    CartRepo cartRepo;



    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "postCartRequest")
    @ResponsePayload
    @Transactional
    public PostCartResponse postCart(@RequestPayload PostCartRequest request) throws SQLException {
        PostCartResponse response = new PostCartResponse();
        Carts carts = new Carts();
        carts.setUserId(request.getCartSubmissionRequest().getUserId());
        carts.setStatus(request.getCartSubmissionRequest().getStatus());
        carts.setCart_id(request.getCartSubmissionRequest().getCartId());

//        Adding the update clause

        Carts updateCart = cartRepo.findById(request.getCartSubmissionRequest().getCartId()).orElse(null);
        if (updateCart != null){
            updateCart.setStatus(request.getCartSubmissionRequest().getStatus());
            cartRepo.save(updateCart);
            response.setMessage("Updated");
            flag = true;
        }


        System.out.println("The value of cartId " + carts.getUserId());
//        Cart_items cart_items = new Cart_items();
        List<CartItem> cartItem = request.getCartSubmissionRequest().getCartItem();
        List<Cart_items> cart_items = new ArrayList<>();

        for (CartItem cartItem1 : cartItem) {
            Cart_items cartItemsEntity = convertCartItemToCartItems(cartItem1);
            cartItemsEntity.setCart(carts);
            cart_items.add(cartItemsEntity);

        }
        cart_items.get(0).getCart().getCart_id();
        System.out.println("This is the cart_item " + cart_items.get(0).getCart().getUserId());

        if (flag != true) {
           repo_cart.saveAll(cart_items);
            response.setMessage("Success");
        }


        response.setCartSubmissionRequest(request.getCartSubmissionRequest());


        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getCartByStatusRequest")
    @ResponsePayload
    @Transactional
    public GetCartByStatusResponse getCartByStatus(@RequestPayload GetCartByStatusRequest request){

        GetCartByStatusResponse response = new GetCartByStatusResponse();

        List<CartData> listCartData = new ArrayList<>();
        System.out.println("This is the cart method");
        cartsList = cartRepo.findByStatus(request.getStatus());
        System.out.println("This is the total number of carts: " + cartsList.size());

        for (Carts cartsLists : cartsList) {
            CartData cartData = new CartData();
            cartData.setCartId(cartsLists.getCart_id());
            cartData.setStatus(cartsLists.getStatus());
            cartData.setUserId(cartsLists.getUserId());
            List<Cart_items> cart_items = repo_cart.findByCart(cartsLists);

            for (Cart_items cart_item: cart_items) {
                CartItem cartItem = new CartItem();
                cartItem.setAmount(cart_item.getAmount());
                cartItem.setQuantity(cart_item.getQuantity());
                cartItem.setProductId(cart_item.getProduct_id());
                cartItem.setName(cart_item.getName());
                cartData.getCartItem().add(cartItem);
            }

            listCartData.add(cartData);
        }

        response.getCartData().addAll(listCartData);

        System.out.println(cartsList);

        return response;
    }



    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getCartByUserRequest")
    @ResponsePayload
    @Transactional
    public GetCartByUserResponse getCartByUser(@RequestPayload GetCartByUserRequest request){

        GetCartByUserResponse response = new GetCartByUserResponse();
        List<CartData> listCartData = new ArrayList<>();
        System.out.println("This is the cart method");
        if (request.getStatus().isBlank()) {
            cartsList = cartRepo.findByUserId(request.getUserId());
        } else {
            cartsList = cartRepo.findByUserIdAndStatus(request.getUserId(), request.getStatus());
        }

        for (Carts cartsLists : cartsList) {
            CartData cartData = new CartData();
            cartData.setCartId(cartsLists.getCart_id());
            cartData.setStatus(cartsLists.getStatus());
            cartData.setUserId(cartsLists.getUserId());
            List<Cart_items> cart_items = repo_cart.findByCart(cartsLists);

            for (Cart_items cart_item: cart_items) {
                CartItem cartItem = new CartItem();
                cartItem.setAmount(cart_item.getAmount());
                cartItem.setQuantity(cart_item.getQuantity());
                cartItem.setProductId(cart_item.getProduct_id());
                cartItem.setName(cart_item.getName());
                cartData.getCartItem().add(cartItem);
            }

            listCartData.add(cartData);
        }

        response.getCartData().addAll(listCartData);

        System.out.println(cartsList);

        return response;

    }

    public Cart_items convertCartItemToCartItems(CartItem cartItem) {
        Cart_items cartItemsEntity = new Cart_items();
        cartItemsEntity.setProduct_id(cartItem.getProductId());
        cartItemsEntity.setQuantity(cartItem.getQuantity());
        cartItemsEntity.setAmount(cartItem.getAmount());
        cartItemsEntity.setName(cartItem.getName());
        System.out.println("this is inside the method" + cartItemsEntity.getProduct_id());
        // Set other properties as needed
        return cartItemsEntity;
    }


}