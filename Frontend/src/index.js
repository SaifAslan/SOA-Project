import React from "react";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
// import 'antd/dist/antd.css';
import ProductListPage from "./routes/Products";
import * as ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
import Product from "./routes/Product";
import Cart from "./routes/Cart";

const router = createBrowserRouter([
  {
    path: "/",
    element: <ProductListPage />,
  },
  { path: "/product/:productId", element: <Product /> },
  {
    path: "/cart",
    element: <Cart />,
  },
]);
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <div className="App">
      <div className="container">
        <RouterProvider router={router} />
      </div>
    </div>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
