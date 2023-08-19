import React, { useEffect, useState } from "react";
import { Card, Col, Row, Select } from "antd";
import { Link } from "react-router-dom";
import axios from "axios";
// import { useSelector, useDispatch } from 'react-redux'
const { Option } = Select;

// Sample product data
const productsImages = [
  {
    id: 1,

    photo: "https://i.ebayimg.com/images/g/bLcAAOSwFTxkJjrV/s-l1600.jpg",
  },
  {
    id: 2,

    photo:
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
  },
  // Add more products...
  {
    id: 19,

    photo:
      "https://media.davidnieper.co.uk/catalog/product/1/3/13bd6de3138e105acaf577806deaa7bae544bcc7_maria_cotton_summer_dress_4043_SS23_1_13.jpg?quality=80&bg-color=255,255,255&fit=bounds&height=&width=&canvas=:",
  },
  {
    id: 20,

    photo: "https://cdn.chums.co.uk/prodimg/MX007_Grey_1_zoom.jpg",
  },
];

const ProductCard = ({ product }) => {
  const { productName, productDescription, price, productId } = product;

  return (
    <Card
      hoverable
      cover={
        <img
          alt={productId}
          height={450}
          style={{ objectFit: "cover" }}
          src={productsImages.find((product) => product.id === productId).photo}
        />
      }
      style={{ marginBottom: 20 }}
    >
      <h3>{productName}</h3>
      <div
        style={{
          display: "-webkit-box",
          WebkitBoxOrient: "vertical",
          WebkitLineClamp: 2,
          overflow: "hidden",
          textOverflow: "ellipsis",
        }}
      >
        {productDescription}
      </div>
      <div style={{ marginTop: 10, fontWeight: "bold" }}>Price: ${price}</div>
    </Card>
  );
};

const Products = () => {
  const [sorting, setSorting] = useState("price"); // Default sorting option
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5150/api/Product/")
      .then((res) => {
        setProducts(res.data);
      })
      .catch((err) => {
        console.log({ err });
      });
  }, []);

 
  // Function to sort the products based on selected sorting option
  const sortProducts = (option) => {
    const sortedProducts = [...products];
    switch (option) {
      case "price":
        sortedProducts.sort((a, b) => a.price - b.price);
        break;
      case "title":
        sortedProducts.sort((a, b) => a.title.localeCompare(b.title));
        break;
      default:
        break;
    }
    return sortedProducts;
  };

  const sortedProducts = sortProducts(sorting);

  return (
    <div>
      {products.length == 0 ? (
        "loading ..."
      ) : (
        <Row gutter={[16, 16]}>
          {sortedProducts.map((product) => (
            <Col key={product.id} xs={24} sm={12} md={8} lg={6}>
              <Link to={"product/" + product.productId}>
                <ProductCard product={product} />
              </Link>
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
};

export default Products;
