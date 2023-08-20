import { Button, Card, Col, Form, Input, Row, message } from "antd";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

function Orders() {
  const user = useSelector((state) => state.user);
  const [orders, setOrders] = useState([]);
  const [trackedOrder, setTrackedOrder] = useState({});
  const [form] = Form.useForm();
  const navigate = useNavigate();
  useEffect(() => {
    if (user.userID == 0) {
      message.error("please login first!");
      navigate("/login");
    } else {
      axios
        .get(`http://localhost:5001/GetAllShipments?user_id=${user.userID}`)
        .then((res) => {
          setOrders(res.data);
        })
        .catch((error) => {
          console.log({ error });
        });
    }
  }, []);

  const trackOrder = (data) => {
    console.log(data);
    axios
      .get(`http://localhost:5001/TrackOrder/${+data.orderId}`)
      .then((res) => {
        if (typeof res.data == "string") {
          message.error("failed to track order!");
        } else {
          console.log(res.data);
          setTrackedOrder(res.data);
        }
      })
      .catch((error) => {
        console.log({ error });
      });
  };

  return (
    <div>
      <Row gutter={(32, 32)}>
        <Col md={24} lg={12}>
          {orders.length > 0 ? (
            <Row gutter={(32, 32)}>
              {orders.map((order, index) => {
                return (
                  <Col md={24} lg={24}>
                    <Card
                      key={index}
                      title={`Order ID: ` + order.cartId}
                      style={{ width: "100%", marginBottom: "1rem" }}
                    >
                      <Row gutter={32}>
                        <Col md={24} lg={12}>
                          <div className="cart-items">
                            {order.cartItem.map((item) => (
                              <Card
                                style={{ width: "100%", marginBottom: "1rem" }}
                                key={item.id}
                                className="cart-item"
                              >
                                <h3>{item.name}</h3>
                                <p>Price: ${item.amount}</p>
                                <p>Quantity:{item.quntity} </p>
                              </Card>
                            ))}
                          </div>
                        </Col>
                        <Col md={24} lg={12}>
                          <p>Order: {order.status}</p>
                          <p>
                            Courier: {order.shipments?.shipments[0]?.courier}
                          </p>
                          <p>
                            Source: {order.shipments?.shipments[0]?.source.city}
                          </p>
                          <p>
                            Destination:{" "}
                            {order.shipments?.shipments[0]?.destination.city}
                          </p>
                        </Col>
                      </Row>
                    </Card>
                  </Col>
                );
              })}
            </Row>
          ) : (
            "You don't have any orders"
          )}
        </Col>
        <Col md={24} lg={12}>
          <Card style={{ width: "100%" }} title="Tarck your order">
            <Form
              form={form}
              name="basic"
              initialValues={{
                remember: true,
              }}
              onFinish={trackOrder}
              autoComplete="off"
            >
              <Form.Item
                name="orderId"
                label="Order ID"
                rules={[
                  {
                    required: true,
                    message: "Please input your orderId!",
                  },
                ]}
              >
                <Input />
              </Form.Item>
              <Row gutter={16}>
                <Col>
                  <Form.Item>
                    <Button type="primary" htmlType="submit">
                      Track
                    </Button>
                  </Form.Item>
                  {trackedOrder.cartId && (
                    <Card
                      style={{ width: "100%", marginBottom: "1rem" }}
                      title={`Order: ${trackedOrder.cartId} updates`}
                    >
                      <div>
                        {trackedOrder?.shipment?.updates.map(
                          (update, index) => {
                            return (
                              <Card
                                key={index}
                                style={{ width: "100%", marginBottom: "1rem" }}
                              >
                                <p> Status: {update.status}</p>
                                <p> Location: {update.location}</p>
                                <p> Date and time: {update.datetime}</p>
                              </Card>
                            );
                          }
                        )}
                      </div>
                    </Card>
                  )}
                </Col>
              </Row>
            </Form>
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default Orders;
