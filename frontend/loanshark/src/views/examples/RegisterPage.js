import React,{ Component } from "react";
import Axios from "axios";
import {  toast,ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import classnames from "classnames";
import FormData from 'form-data'

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

class RegisterPage extends Component {


   onSubmit  = () => {
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
    let confirm_password = document.getElementById("confirm_password").value
    let full_name = document.getElementById("full_name").value
    let phone_number = document.getElementById("phone_number").value
    let proof = document.getElementById("proof").files[0]


    let data = new FormData(); // creates a new FormData object
    data.append('proof', proof, proof.name);
    data.append('email', email);
    data.append('password', password);
    data.append('full_name', full_name);
    data.append('phone_number', phone_number);
    data.append('confirm_password', confirm_password);

    Axios.post("http://localhost:8000/auth/register/", data,{

      headers: {
        'accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
      },

  })

  .then((response) => {
    setTimeout(function () {
      toast.success("Your Account Has Been Created Successfully! it will be approved by the Admin as soon as possible");
    }, 100);
    this.props.history.push("/login-page");
  })

    .catch((error) => {
      console.log('error',error)
      toast.error("Something went wrong, please try again");
    });

};

  render (){
    return(
<div >
<ExamplesNavbar />
      <ToastContainer />

      <div className="wrapper" encType="multipart/form-data" >
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
                      <CardTitle tag="h4">Register</CardTitle>
                    </CardHeader>
                    <CardBody>
                      <Form className="form">

                        <InputGroup
                          className={classnames({
                      
                          })}
                        >
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="tim-icons icon-email-85" />
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input
                            placeholder="Email"
                            id="email"
                            name="email"
                            type="text"

                          />
                        </InputGroup>
                        <InputGroup
                          className={classnames({
              
                          })}
                          >
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="tim-icons icon-lock-circle" />
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input
                            placeholder="Password"
                            id="password"
                            name="password"
                            type="password"

                          />
                        </InputGroup>

                        <InputGroup
                          className={classnames({
                          })}
                          >
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="tim-icons icon-lock-circle" />
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input
                            placeholder="Confirm password"
                            type="password"
                            id="confirm_password"
                            name="confirm_password"

                          />
                        </InputGroup>
                        












                        <InputGroup
                          className={classnames({
                          })}
                          >
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="tim-icons icon-lock-circle" />
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input
                            placeholder="Full name"
                            type="text"
                            id="full_name"
                            name="full_name"

                          />
                        </InputGroup>
                        <InputGroup
                          className={classnames({
                          })}
                          >
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="tim-icons icon-lock-circle" />
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input
                            placeholder="Phone N°"
                            type="text"
                            id="phone_number"
                            name="phone_number"

                          />
                        </InputGroup>










                        <InputGroup
                          className={classnames({
                          })}
                          >

                          <Input
                            placeholder="Proof of employment"
                            type="file"
                            id="proof"
                            name="proof"
    
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
                      <Button className="btn-round" color="primary" size="lg"onClick={() => this.onSubmit()}>
                        Get Started
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

export default RegisterPage; 