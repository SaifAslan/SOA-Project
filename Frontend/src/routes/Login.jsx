import { Button, Card, Checkbox, Form, Input, message } from "antd";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
const onFinishFailed = (e) => {
  console.log("login form failed!", e);
};

const Login = () => {
  const [form] = Form.useForm();
  const dispatch = useDispatch();
  const userInfo = useSelector((state) => state.user);
  const navigate = useNavigate();

  useEffect(() => {
    if (userInfo.userID) {
      navigate("/");
    }
  }, [userInfo]);

  const onFinish = (values) => {
    handleLogin(values)
    // handleLogin(values);
  };

  const handleLogin = (userData) => {
    console.log(userData);
    axios
      .post("http://localhost:9000/authenticateuser", userData)
      .then((response) => {
        console.log(response);
        message.success("Login successful! 😎"); 
      })
      .catch((err) => {
        console.log({ err });
        message.error("Login error! 😔"); 

      });
  };

  console.log(userInfo);
  return (
    <div>
      <Card>
        <Form
          form={form}
          name="basic"
          labelCol={{
            span: 8,
          }}
          wrapperCol={{
            span: 16,
          }}
          style={{
            maxWidth: 600,
          }}
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
            name="remember"
            valuePropName="checked"
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Checkbox>Remember me</Checkbox>
          </Form.Item>

          <Form.Item
            wrapperCol={{
              offset: 8,
              span: 16,
            }}
          >
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
};
export default Login;
