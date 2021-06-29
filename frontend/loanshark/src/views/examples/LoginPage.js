import React, { Component } from 'react';

import classnames from "classnames";
import Axios from "axios";
import {  toast,ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardImg,
  CardTitle,
  Label,
  FormGroup,
  Form,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Container,
  Row,
  Col,
} from "reactstrap";

// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";
import Footer from "components/Footer/Footer.js";

// import { withRouter } from 'react-router-dom'; 

class LoginPage extends Component {


  onSubmit = () => {
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
  Axios.post("http://localhost:8000/auth/login/", {
    email:email,
    password: password,
  })
    .then((response) => {
      let return_data = response.data;
      console.log('return_data',return_data)
      localStorage.setItem("email", return_data.email)
      localStorage.setItem("token", return_data.tokens.token)
      localStorage.setItem("id", return_data.tokens.id)
      localStorage.setItem("full_name", return_data.tokens.full_name)
      localStorage.setItem("phone_number", return_data.tokens.phone_number)
      localStorage.setItem("address", return_data.tokens.address)
      toast.success("welcome back");



      // console.log('email',email)
      // console.log('id',localStorage.getItem('id'))
      // console.log('token',localStorage.getItem('token'))
      // console.log(localStorage.getItem('full_name'))
      // console.log(localStorage.getItem('phone_number'))
      // console.log(localStorage.getItem('address'))
      // console.log('return_data',return_data)

     
      this.props.history.push('/profile-page')


    })
    .catch((error) => {
          toast.error("Username and/or password are incorrect");
    });

};
componentDidMount() {
  

}
  render() {
    return (
      <div>
      <ToastContainer />

<ExamplesNavbar />
<div className="wrapper">
<div className="page-header">
  <div className="page-header-image" />
  <div className="content">
    <Container>
      <Row>
        <Col className="offset-lg-0 offset-md-3" lg="5" md="6">
          <div
            className="square square-7"
            id="square7"
            
          
          />
          <div
            className="square square-8"
            id="square8"
            
          
          />
          <Card className="card-register">
            <CardHeader>
              <CardImg
                alt="..."
                src={require("assets/img/square-purple-1.png").default}
              />
              <CardTitle tag="h4">Login</CardTitle>
            </CardHeader>
            <CardBody>
              <Form className="form">

                <InputGroup

                >
                  <InputGroupAddon addonType="prepend">
                    <InputGroupText>
                      <i className="tim-icons icon-email-85" />
                    </InputGroupText>
                  </InputGroupAddon>
                  <Input
                    placeholder="Email"
                    type="text"
                    id="email"
                    required

                  />
                </InputGroup>
                <InputGroup

                >
                  <InputGroupAddon addonType="prepend">
                    <InputGroupText>
                      <i className="tim-icons icon-lock-circle" />
                    </InputGroupText>
                  </InputGroupAddon>
                  <Input
                    placeholder="Password"
                    id="password"
                    type="password"
                    name="password"

                  />
                </InputGroup>
                <FormGroup check className="text-left">
                  <Label check>
                    <Input type="checkbox" />
                    <span className="form-check-sign" />I agree to the{" "}
                    <a>
                      terms and conditions
                    </a>
                    .
                  </Label>
                </FormGroup>
              </Form>
            </CardBody>
            <CardFooter>
              <Button className="btn-round" color="primary" size="lg" onClick={() => this.onSubmit()}>
                Login
              </Button>
            </CardFooter>
          </Card>
        </Col>
      </Row>
      <div className="register-bg" />
      <div
        className="square square-1"
        id="square1"
        
      />
      <div
        className="square square-2"
        id="square2"
        
      />
      <div
        className="square square-3"
        id="square3"
        
      />
      <div
        className="square square-4"
        id="square4"
        
      />
      <div
        className="square square-5"
        id="square5"
        
      />
      <div
        className="square square-6"
        id="square6"
        
      />
    </Container>
  </div>
</div>
<Footer />
</div>
</div>
    );
  }
}

export default LoginPage; 