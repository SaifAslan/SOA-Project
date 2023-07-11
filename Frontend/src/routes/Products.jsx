import React, { useState } from "react";
import { Card, Col, Row, Select } from "antd";

const { Option } = Select;

// Sample product data
const products = [
  {
    id: 1,
    title: "Wireless Bluetooth Earbuds",
    description:
      "Immerse yourself in high-quality sound with these wireless Bluetooth earbuds. Enjoy seamless connectivity and convenience on the go.",
    price: 49.99,
    photo:
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
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
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
  },
  {
    id: 20,
    title: "Portable External Hard Drive",
    description:
      "Expand your storage capacity and securely store your files with this portable external hard drive. With ample space and fast data transfer speeds, it's the perfect companion for your digital storage needs.",
    price: 89.99,
    photo:
      "https://www.gant.co.uk/dw/image/v2/BFLN_PRD/on/demandware.static/-/Sites-gant-master/default/dwf2e5d003/pim/202204/234100/110/202204-234100-110-flat-fv-1.jpg?sw=650",
  },
];

const ProductCard = ({ product }) => {
  const { title, description, price, photo } = product;

  return (
    <Card
      hoverable
      cover={<img alt={title} src={photo} />}
      style={{ marginBottom: 20 }}
    >
      <h3>{title}</h3>
      <div
        style={{
          display: "-webkit-box",
          WebkitBoxOrient: "vertical",
          WebkitLineClamp: 2,
          overflow: "hidden",
          textOverflow: "ellipsis",
        }}
      >
        {description}
      </div>
      <div style={{ marginTop: 10, fontWeight: "bold" }}>Price: ${price}</div>
    </Card>
  );
};

const Products = () => {
  const [sorting, setSorting] = useState("price"); // Default sorting option

  // Handler for sorting option change
  const handleSortingChange = (value) => {
    setSorting(value);
  };

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
      <div style={{ marginBottom: 20 }}>
        <Select
          defaultValue={sorting}
          onChange={handleSortingChange}
          style={{ width: 150 }}
        >
          <Option value="price">Price</Option>
          <Option value="title">Title</Option>
        </Select>
      </div>
      <Row gutter={[16, 16]}>
        {sortedProducts.map((product) => (
          <Col key={product.id} xs={24} sm={12} md={8} lg={6}>
            <ProductCard product={product} />
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default Products;
