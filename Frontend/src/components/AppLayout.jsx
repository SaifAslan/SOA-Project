import React from 'react';
import { Link } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import {
  HomeOutlined,
  ShoppingCartOutlined,
  UserOutlined,
} from '@ant-design/icons';

const { Header, Content } = Layout;

const AppLayout = ({ children }) => {
  return (
    <Layout>
      <Header>
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="1" icon={<HomeOutlined />}>
            <Link to="/">Home</Link>
          </Menu.Item>
          <Menu.Item key="2" icon={<ShoppingCartOutlined />}>
            <Link to="/cart">Cart</Link>
          </Menu.Item>
          <Menu.Item key="3" icon={<UserOutlined />}>
            <Link to="/login">Login</Link>
          </Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
          {children}
        </div>
      </Content>
    </Layout>
  );
};

export default AppLayout;
