import { Button, Card, Checkbox, Form, Input, message } from "antd";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

const USER_SERVICE_URL = "http://localhost:6001";

const onFinishFailed = (e) => {
  console.log("login form failed!", e);
};
function RegisterUser() {
  const [form] = Form.useForm();
  const dispatch = useDispatch();
  const userInfo = useSelector((state) => state.user);
  const navigate = useNavigate();
  //   useEffect(() => {
  //     if (userInfo.userID) {
  //       navigate("/");
  //     }
  //   }, [userInfo]);

  const onFinish = (values) => {
    handleLogin(values);
    // handleLogin(values);
  };

  const handleLogin = (userData) => {
    console.log(userData);
    axios
      .post(USER_SERVICE_URL + "/adduser", {
        ...userData,
        userType: "buyer",
      })
      .then((response) => {
        console.log(response);
        message.success("Register successful! 😎");
        setTimeout(navigate("/login"), 2000)
      })
      .catch((err) => {
        console.log({ err });
        message.error("Register error! 😔");
      });
  };

  return (
    <div>
      <Card >
        <Form
          form={form}
          name="basic"
       
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="Username"
            name="userName"
            rules={[
              {
                required: true,
                message: "Please input your username!",
              },
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            rules={[
              {
                required: true,
                message: "Please input your password!",
              },
            ]}
          >
            <Input.Password />
          </Form.Item>
          <Form.Item
            label="email"
            name="email"
            rules={[
              {
                required: true,
                message: "Please input your email!",
              },
            ]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Mobile Number"
            name="mobileNumber"
            rules={[
              {
                required: true,
                message: "Please input your Mobile Number!",
              },
            ]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Address"
            name="address"
            rules={[
              {
                required: true,
                message: "Please input your Address!",
              },
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
          >
            <Button type="primary" htmlType="submit">
              Register
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
}

export default RegisterUser;
