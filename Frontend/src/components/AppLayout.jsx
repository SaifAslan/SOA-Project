import React from "react";
import { Link } from "react-router-dom";
import { Layout, Menu, message } from "antd";
import {
  HomeOutlined,
  ShoppingCartOutlined,
  UserOutlined,
} from "@ant-design/icons";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../redux/features/user/userSlice";

const { Header, Content } = Layout;

const AppLayout = ({ children }) => {
  const dispatch = useDispatch();
  const userInfo = useSelector((state) => state.user);
  console.log(userInfo);

  const handleLogout = () => {
    dispatch(logout());
    message.success("User logged out! 👋");
  };

  return (
    <Layout>
      <Header style={{ paddingInline: 0 }}>
        <Menu mode="horizontal" defaultSelectedKeys={["1"]}>
          <Menu.Item key="1" icon={<HomeOutlined />}>
            <Link to={"/"}>Home</Link>
          </Menu.Item>
          <Menu.Item key="2" icon={<ShoppingCartOutlined />}>
            <Link to="/cart">Cart</Link>
          </Menu.Item>
          {userInfo.userID ? (
            <Menu.Item key="3" icon={<ShoppingCartOutlined />}>
              <Link to="/cart">Orders</Link>
            </Menu.Item>
          ):null}
          <Menu.Item
            key="4"
            icon={<UserOutlined />}
            onClick={() => (userInfo.userID ? handleLogout() : null)}
          >
            {userInfo.userID ? (
              <span>Logout</span>
            ) : (
              <Link to="/login">Login</Link>
            )}
          </Menu.Item>
        </Menu>
      </Header>
      <Content>
        <div style={{ background: "#fff" }}>{children}</div>
      </Content>
    </Layout>
  );
};

export default AppLayout;
