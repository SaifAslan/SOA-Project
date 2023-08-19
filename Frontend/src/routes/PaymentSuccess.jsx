import axios from "axios";
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { emptyCart } from "../redux/features/cart/cartSlice";
import { useParams } from "react-router-dom";

const ORCHESTRATOR_SERVICE_URL = "http://localhost:5001";

function PaymentSuccess() {
  const cart = useSelector((state) => state.cart);
  const { orderid } = useParams();
  const dispatch = useDispatch();
  useEffect(() => {
    axios
      .post(ORCHESTRATOR_SERVICE_URL + "/StartShipping/" + orderid, {
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
      })
      .then((res) => {
        dispatch(emptyCart());
      })
      .catch((err) => {
        console.log({ err });
      });
  }, []);

  return <div>PaymentSuccess {orderid}</div>;
}

export default PaymentSuccess;
