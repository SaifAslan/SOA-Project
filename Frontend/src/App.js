import "./App.css";
import Product from "./routes/Product";
import Cart from "./routes/Cart";
import AppLayout from "./components/AppLayout";
import { Route, Routes } from "react-router-dom";
import Products from "./routes/Products";
import Login from "./routes/Login";
import Checkout from "./routes/Checkout";
import Strip from "./routes/strip";

function App() {
  return (
    <div className="App">
      <AppLayout>
        <div className="container">
          <Routes>
            <Route path="/" Component={Products} />
            <Route path="/product/:productId" Component={Product} />
            <Route path="/cart" Component={Cart} />
            <Route path="/login" Component={Login} />
            <Route path="/checkout" Component={Checkout} />
            <Route path="/stripe" Component={Strip} />
          </Routes>
        </div>
      </AppLayout>
    </div>
  );
}

export default App;
