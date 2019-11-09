import React, { Component } from "react";
import { connect } from "react-redux";

import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

import { login } from "../actions/auth";
import { authErrors, isAuthenticated } from "../reducers";

class Nav extends Component {
  state = {
    username: "",
    password: ""
  };

  handleInputChange = event => {
    const target = event.target,
      value = target.type === "checkbox" ? target.checked : target.value,
      name = target.name;

    this.setState({
      [name]: value
    });
  };

  onSubmit = event => {
    event.preventDefault();
    console.log(this.state);
    this.props.onSubmit(this.state.username, this.state.password);
  };

  logged_out_nav = (
    <Form inline onSubmit={this.onSubmit}>
      <Form.Control
        type="text"
        name="username"
        placeholder="Username"
        className="mr-sm-2"
        onChange={this.handleInputChange}
      />
      <Form.Control
        type="password"
        name="password"
        placeholder="Password"
        className=" mr-sm-2"
        onChange={this.handleInputChange}
      />
      <Button type="submit">Submit</Button>
    </Form>
  );

  logged_in_nav = (<p>Hello User!</p>);

  render() {
    const errors = this.props.errors || {};
    return (
      <Navbar expand="sm" variant="dark" bg="dark">
        <Container>
          <Navbar.Brand href="poo">Syndicate Sound</Navbar.Brand>
          {this.props.isAuthenticated
            ? this.logged_in_nav
            : this.logged_out_nav}
        </Container>
      </Navbar>
    );
  }
}

const mapStateToProps = state => ({
  errors: authErrors(state),
  isAuthenticated: isAuthenticated(state)
});

const mapDispatchToProps = dispatch => ({
  onSubmit: (username, password) => {
    dispatch(login(username, password));
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(Nav);
