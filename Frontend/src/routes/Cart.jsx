import React, { useState } from "react";
import { Card, Button, InputNumber, Row, Col } from "antd";
import "../styles/cart.scss";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { addProduct } from "../redux/features/cart/cartSlice";
const CartPage = () => {
  // Replace with your cart data
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const cartItems = useSelector((state) => state.cart.cartItems);

  const handleDelete = (productId) => {
    const updatedCartItems = cartItems.filter((item) => item.id !== productId);
    // setCartItems(updatedCartItems);
  };
  console.log(cartItems);
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
    return cartItems.reduce(
      (total, item) => total + item.amount,
      0
    );
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
            {cartItems.map((item) => (
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
                  navigate("/checkout");
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
