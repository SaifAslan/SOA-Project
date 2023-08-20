import React, { useEffect, useState } from "react";
import { Card, Button, InputNumber, Row, Col, message } from "antd";
import "../styles/cart.scss";
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
  addCartId,
  addDeliveryCost,
  addProduct,
  removeProduct,
} from "../redux/features/cart/cartSlice";
import axios from "axios";

const ORCHESTRATOR_SERVICE_URL = "http://localhost:5001";

const CartPage = () => {
  // Replace with your cart data
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [courierData, setCourierData] = useState({});
  const cart = useSelector((state) => state.cart);
  const user = useSelector((state) => state.user);
  const handleDelete = (productId) => {
    dispatch(removeProduct(productId));
  };
  console.log(cart);
  useEffect(() => {
    cart.cartItems.length > 0 && getCourierCost();
  }, []);

  const postCart = () => {
    user.userID == 0 && message.error("please login first!");
    user.userID == 0 && navigate("/login");
    user.userID !== 0 &&
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
    let priceForOne = item.amount / item.quantity;
    dispatch(
      addProduct({
        quantity: quantity,
        product: {
          productId: item.productId,
          price: priceForOne,
          productName: item.name,
        },
      })
    );
    getCourierCost();
  };

  const calculateSubtotal = () => {
    return cart.cartItems.reduce((total, item) => total + item.amount, 0);
  };

  const calculateTotal = () => {
    const subtotal = calculateSubtotal();
    const shippingCost = +courierData?.amount;
    return subtotal + shippingCost;
  };

  const getCourierCost = () => {
    axios
      .post("http://localhost:5001/CalculateShippingCostNoCourier", {
        source: {
          state: "USA",
          city: "NYC",
          zip: "10001",
          street: "any street in new york city",
          delivery_point: "warehouse",
        },
        destination: {
          state: "UK",
          city: "Birmingham",
          zip: "b4 78j",
          street: "aston street",
          delivery_point: "my home",
        },
        items: cart.cartItems.map((item) => {
          return {
            item_id: item.productId.toString(),
            name: item.name,
            count: item.quantity,
          };
        }),
      })
      .then((res) => {
        setCourierData(res.data);
        dispatch(addDeliveryCost(+res?.data?.amount ?? 100));
      })
      .catch((err) => {
        console.log({ err });
      });
  };
  return (
    <div className="cart-page">
      {cart.cartItems.length > 0 ? (
        <Row gutter={32}>
          <Col md={24} lg={16}>
            <div className="cart-items">
              {cart.cartItems.map((item) => (
                <Card key={item.productId} className="cart-item">
                  <h3>{item.name}</h3>
                  <p>Price: ${item.amount.toFixed(2)}</p>
                  <p>Quantity: </p>
                  <InputNumber
                  style={{marginRight:"1rem"}}
                    min={1}
                    defaultValue={item.quantity}
                    onChange={(quantity) =>
                      handleQuantityChange(item, quantity)
                    }
                  />
                  <Button  onClick={() => handleDelete(item.productId)}>
                    Delete
                  </Button>
                </Card>
              ))}
            </div>
          </Col>
          <Col md={24} lg={8}>
            <div className="cart-summary">
              <Card className="summary-card">
                <h3>Summary</h3>
                <p>Will be delivered in {courierData.days} days</p>
                <p>Subtotal: ${calculateSubtotal().toFixed(2)}</p>
                <p>Shipping Cost: ${courierData?.amount?.toFixed(2)}</p>
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
      ) : (
        "cart is empty"
      )}

      {/* <Routes>
        <Route path="/checkout" Component={<h1>bhfjehfj</h1>} />
      </Routes> */}
    </div>
  );
};

export default CartPage;
