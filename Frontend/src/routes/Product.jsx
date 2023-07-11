import React from "react";
import { Row, Col, Card, Button } from "antd";
import { Routes, Route, useParams } from "react-router-dom";

const ProductPage = ({}) => {
  const { productId } = useParams();
  console.log(productId);
  // Replace with your product data
  const product = {
    id: 1,
    title: "Wireless Bluetooth Earbuds",
    description:
      "Immerse yourself in high-quality sound with these wireless Bluetooth earbuds. Enjoy seamless connectivity and convenience on the go.",
    price: 49.99,
    photo:
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
  };

  const addToCart = () => {
    // Logic to add the product to the cart
    // You can implement your own cart management logic here
    console.log("Product added to cart:", product);
  };

  return (
    <div className="product-page">
      <Row gutter={16} >
        <Col xs={24} md={12} >
          <img
            alt={product.name}
            src={product.photo}
            // className="product-image"
          />
        </Col>
        <Col xs={24} md={12}> 
          <Card className="product-details">
            <h1 className="product-name">{product.title}</h1>
            <p className="product-description">{product.description}</p>
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
    </div>
  );
};

export default ProductPage;
