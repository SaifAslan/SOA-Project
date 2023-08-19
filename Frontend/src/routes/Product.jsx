import React, { useEffect, useState } from "react";
import { Row, Col, Card, Button, message } from "antd";
import { Routes, Route, useParams } from "react-router-dom";
import { useDispatch } from "react-redux";
import { addProduct } from "../redux/features/cart/cartSlice";
import axios from "axios";

const ProductPage = ({}) => {
  const { productId } = useParams();
  const dispatch = useDispatch();
  const [product, setProduct] = useState({});

  useEffect(() => {
    axios
      .get("http://localhost:5150/api/Product/" + productId)
      .then((res) => {
        setProduct(res.data);
      })
      .catch((err) => {
        console.log({ err });
      });
  }, []);

  useEffect(() => {
    let fetchedProduct = products.find((item) => item.id === +productId);
    setProduct(fetchedProduct);
  }, [productId]);

  const addToCart = () => {
    try {
      dispatch(addProduct({ product, quantity: 1 }));
      message.success("Product added to cart! 🥳");
    } catch (error) {
      console.log("error", error);
      message.error("Error occured please contact support!");
    }
  };

  return (
    <div className="product-page">
      {product ? (
        <Row gutter={16}>
          <Col xs={24} md={12}>
            <img
              alt={product.name}
              src={products.find((product) => product.id == productId).photo}
              height={600}
              style={{ objectFit: "cover" }}
              // className="product-image"
            />
          </Col>
          <Col xs={24} md={12}>
            <Card className="product-details">
              <h1 className="product-name">{product.productName}</h1>
              <p className="product-description">{product.productDescription}</p>
              <p className="product-price">Price: ${product.price}</p>
              <Button
                type="primary"
                onClick={addToCart}
                className="add-to-cart-button"
              >
                Add to Cart
              </Button>
            </Card>
          </Col>
        </Row>
      ) : (
        "loading ..."
      )}
    </div>
  );
};

export default ProductPage;
const products = [
  {
    id: 1,
    title: "Wireless Bluetooth Earbuds",
    description:
      "Immerse yourself in high-quality sound with these wireless Bluetooth earbuds. Enjoy seamless connectivity and convenience on the go.",
    price: 49.99,
    photo: "https://i.ebayimg.com/images/g/bLcAAOSwFTxkJjrV/s-l1600.jpg",
  },
  {
    id: 2,
    title: "Smart Fitness Tracker Watch",
    description:
      "Track your fitness goals and stay motivated with this smart fitness tracker watch. Monitor your heart rate, track your workouts, and receive notifications on your wrist.",
    price: 79.99,
    photo:
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
  },
  // Add more products...
  {
    id: 19,
    title: "Premium Coffee Beans",
    description:
      "Indulge in the rich and aromatic flavors of our premium coffee beans. Sourced from the finest coffee plantations, these beans offer a truly satisfying coffee experience.",
    price: 12.99,
    photo:
      "https://media.davidnieper.co.uk/catalog/product/1/3/13bd6de3138e105acaf577806deaa7bae544bcc7_maria_cotton_summer_dress_4043_SS23_1_13.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=&width=&canvas=:",
  },
  {
    id: 20,
    title: "Portable External Hard Drive",
    description:
      "Expand your storage capacity and securely store your files with this portable external hard drive. With ample space and fast data transfer speeds, it's the perfect companion for your digital storage needs.",
    price: 89.99,
    photo: "https://cdn.chums.co.uk/prodimg/MX007_Grey_1_zoom.jpg",
  },
];
