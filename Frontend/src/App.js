import "./App.css";
import Product from "./routes/Product";
import Cart from "./routes/Cart";
import AppLayout from "./components/AppLayout";
import { Route, Routes } from "react-router-dom";
import Products from "./routes/Products";
import Login from "./routes/Login";
import Checkout from "./routes/Checkout";
import Orders from "./routes/Orders";
import RegisterUser from "./routes/RegisterUser";
import PaymentSuccess from "./routes/PaymentSuccess";


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
            <Route path="/orders" Component={Orders} />
            <Route path="/register" Component={RegisterUser} />
            <Route path="/payment-success/:orderid" Component={PaymentSuccess} />

          </Routes>
        </div>
      </AppLayout>
    </div>
  );
}

export default App;
