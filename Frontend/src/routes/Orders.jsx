import { Card, Col, Row } from "antd";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";

function Orders() {
  const user = useSelector((state) => state.user);
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    axios
      .get(`http://localhost:5001/GetAllShipments?user_id=${user.userID}`)
      .then((res) => {
        setOrders(res.data);
      })
      .catch((error) => {
        console.log({ error });
      });
  }, []);

  return (
    <div>
      <Row gutter={32}>
        {orders.map((order, index) => {
          return (
            <Col md={24} lg={16}>
              <Card key={index} title={`Order ID: ` + order.cartId} style={{width:"900px"}}>
                <Row gutter={32}>
                  <Col md={24} lg={16}>
                    <div className="cart-items">
                      {order.cartItem.map((item) => (
                        <Card key={item.id} className="cart-item">
                          <h3>{item.name}</h3>
                          <p>Price: ${item.amount}</p>
                          <p>Quantity:{item.quntity} </p>
                        </Card>
                      ))}
                    </div>
                  </Col>
                  <Col md={24} lg={8}>
                    <p>Order: {order.status}</p>
                    <p>Courier: {order.shipments?.shipments[0].courier}</p>
                    <p>Source: {order.shipments?.shipments[0].source.city}</p>
                    <p>
                      Destination:{" "}
                      {order.shipments?.shipments[0].destination.city}
                    </p>
                  </Col>
                </Row>
              </Card>
            </Col>
          );
        })}
      </Row>
    </div>
  );
}

export default Orders;
