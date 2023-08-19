import React, { useState } from "react";
import { Card, Button, InputNumber, Row, Col } from "antd";
import "../styles/cart.scss";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { addCartId, addProduct } from "../redux/features/cart/cartSlice";
import axios from "axios";

const ORCHESTRATOR_SERVICE_URL = "http://localhost:5001";

const CartPage = () => {
  // Replace with your cart data
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart);
  const user = useSelector((state) => state.user);

  const handleDelete = (productId) => {
    const updatedCartItems = cart.cartItems.filter(
      (item) => item.id !== productId
    );
    // setCartItems(updatedCartItems);
  };
  console.log(cart);

  const postCart = () => {
    axios
      .post(ORCHESTRATOR_SERVICE_URL + "/CreateOrder", {
        userId: user.userID ?? "userId",
        cartItem: cart.cartItems,
      })
      .then((response) => {
        dispatch(addCartId(response.data.cartId));
        navigate("/checkout");
      })
      .catch((error) => {
        console.log({ error });
      });
  };
  const handleQuantityChange = (item, quantity) => {
    dispatch(
      addProduct({
        quantity: quantity,
        product: {
          id: item.productId,
          price: item.amount,
          title: item.name,
        },
      })
    );
  };

  const calculateSubtotal = () => {
    return cart.cartItems.reduce((total, item) => total + item.amount, 0);
  };

  const calculateShippingCost = () => {
    // Replace with your shipping cost calculation logic
    return 5.0;
  };

  const calculateTotal = () => {
    const subtotal = calculateSubtotal();
    const shippingCost = calculateShippingCost();
    return subtotal + shippingCost;
  };

  return (
    <div className="cart-page">
      <Row gutter={32}>
        <Col md={24} lg={16}>
          <div className="cart-items">
            {cart.cartItems.map((item) => (
              <Card key={item.id} className="cart-item">
                <h3>{item.name}</h3>
                <p>Price: ${item.amount}</p>
                <p>Quantity: </p>
                <InputNumber
                  min={1}
                  defaultValue={item.quantity}
                  onChange={(quantity) => handleQuantityChange(item, quantity)}
                />
                <Button onClick={() => handleDelete(item.id)}>Delete</Button>
              </Card>
            ))}
          </div>
        </Col>
        <Col md={24} lg={8}>
          <div className="cart-summary">
            <Card className="summary-card">
              <h3>Summary</h3>
              <p>Subtotal: ${calculateSubtotal()}</p>
              <p>Shipping Cost: ${calculateShippingCost()}</p>
              <p>Total: ${calculateTotal().toFixed(2)}</p>
              <Button
                type="primary"
                onClick={() => {
                  postCart();
                  // navigate("/checkout");
                }}
              >
                Checkout
              </Button>
            </Card>
          </div>
        </Col>
      </Row>
      {/* <Routes>
        <Route path="/checkout" Component={<h1>bhfjehfj</h1>} />
      </Routes> */}
    </div>
  );
};

export default CartPage;
