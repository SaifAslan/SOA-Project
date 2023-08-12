import React, { useState } from "react";
import { Card, Button, InputNumber, Row, Col } from "antd";
import "../styles/cart.scss";
import { useNavigate } from "react-router-dom";
const CartPage = () => {
  // Replace with your cart data
  const navigate = useNavigate();

  const [cartItems, setCartItems] = useState([
    { id: 1, name: "Product 1", price: 10.99, quantity: 2 },
    { id: 2, name: "Product 2", price: 19.99, quantity: 1 },
    { id: 3, name: "Product 3", price: 7.99, quantity: 3 },
  ]);

  const handleDelete = (itemId) => {
    const updatedCartItems = cartItems.filter((item) => item.id !== itemId);
    setCartItems(updatedCartItems);
  };

  const handleQuantityChange = (itemId, quantity) => {
    const updatedCartItems = cartItems.map((item) => {
      if (item.id === itemId) {
        return { ...item, quantity };
      }
      return item;
    });
    setCartItems(updatedCartItems);
  };

  const calculateSubtotal = () => {
    return cartItems.reduce(
      (total, item) => total + item.price * item.quantity,
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
                <p>Price: ${item.price}</p>
                <p>Quantity:</p>
                <InputNumber
                  min={1}
                  defaultValue={item.quantity}
                  onChange={(quantity) =>
                    handleQuantityChange(item.id, quantity)
                  }
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
              <p>Total: ${calculateTotal()}</p>
              <Button type="primary" onClick={()=>{navigate("/checkout")}}>Checkout</Button>
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
