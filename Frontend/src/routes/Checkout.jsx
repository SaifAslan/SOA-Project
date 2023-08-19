// import React, { useState } from "react";
// import { Card, Button, InputNumber, Row, Col } from "antd";
// import  "../styles/cart.scss";
// import { Route, Router } from "react-router-dom";

// const Checkout = () => {
//   // Replace with your cart data
//   const [cartItems, setCartItems] = useState([
//     { id: 1, name: "Product 1", price: 10.99, quantity: 2 },
//     { id: 2, name: "Product 2", price: 19.99, quantity: 1 },
//     { id: 3, name: "Product 3", price: 7.99, quantity: 3 },
//   ]);

//   const handleDelete = (itemId) => {
//     const updatedCartItems = cartItems.filter((item) => item.id !== itemId);
//     setCartItems(updatedCartItems);
//   };

//   const handleQuantityChange = (itemId, quantity) => {
//     const updatedCartItems = cartItems.map((item) => {
//       if (item.id === itemId) {
//         return { ...item, quantity };
//       }
//       return item;
//     });
//     setCartItems(updatedCartItems);
//   };

//   const calculateSubtotal = () => {
//     return cartItems.reduce(
//       (total, item) => total + item.price * item.quantity,
//       0
//     );
//   };

//   const calculateShippingCost = () => {
//     // Replace with your shipping cost calculation logic
//     return 5.0;
//   };

//   const calculateTotal = () => {
//     const subtotal = calculateSubtotal();
//     const shippingCost = calculateShippingCost();
//     return subtotal + shippingCost;
//   };

//   return (
//     <div className="cart-page">
//       <Row gutter={32}>
//         <Col md={24} lg={16}>
//           <div className="cart-items">
//             {cartItems.map((item) => (
//               <Card key={item.id} className="cart-item">
//                 <h3>{item.name}</h3>
//                 <p>Price: ${item.price}</p>
//                 <p>Quantity:</p>
//                 <InputNumber
//                   min={1}
//                   defaultValue={item.quantity}
//                   onChange={(quantity) =>
//                     handleQuantityChange(item.id, quantity)
//                   }
//                 />
//                 <Button onClick={() => handleDelete(item.id)}>Delete</Button>
//               </Card>
//             ))}
//           </div>
//         </Col>
//         <Col md={24} lg={8}>
//           <div className="cart-summary">
//             <Card className="summary-card">
//               <h3>Summary</h3>
//               <p>Subtotal: ${calculateSubtotal()}</p>
//               <p>Shipping Cost: ${calculateShippingCost()}</p>
//               <p>Total: ${calculateTotal()}</p>
//               <Button type="primary">Checkout</Button>
//             </Card>
//           </div>
//         </Col>

//       </Row>
//     </div>
//   );
// };

// export default Checkout;
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";
import CheckoutForm from "../components/CheckoutForm";
import { useEffect, useState } from "react";
import axios from "axios";
import { useSelector } from "react-redux";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe(
  "pk_test_51NMyLEEuOjFLJVPuq4bSZaqs1fbFro4PKBhANuxTByGDUhog4xbfxXt2U7IDTnzf3Qwnt664KRvs5bliKb9w5lhr00dAD8QEmK"
);

const PAYMENT_SERVICE_URL = "http://localhost:8070/api";

export default function App() {
  const [options, setOptions] = useState(null);
  const user = useSelector((state) => state.user);
  const cart = useSelector((state) => state.cart);
  useEffect(() => {
    getPaymentIntent();
  }, []);

  const getPaymentIntent = (orderId) => {
    console.log(Math.round(calculateTotal()));
    axios
      .post(PAYMENT_SERVICE_URL + "/create-payment-intent", {
        amount: Math.round(calculateTotal()),
        orderId: +cart.cartId,
        userId: user.userID ? +user.userID : 6474,
      })
      .then((response) => {
        setOptions({
          // passing the client secret obtained from the server
          clientSecret: response.data.clientSecret,
        });
      });
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

  // const options = {
  //   // passing the client secret obtained from the server
  //   clientSecret: 'pi_3NeK56EuOjFLJVPu1qgbSlEn_secret_FsT9tI8lIeToGgm2Y0JW4MsSE',
  // };

  return options ? (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm clientSecret={options.clientSecret} />
    </Elements>
  ) : (
    <p>loading</p>
  );
}
