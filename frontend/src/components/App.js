import React from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";

import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    Container, Row, Col,
    ListGroup, ListGroupItem, Badge } from 'reactstrap';

export default class App extends React.Component {
    constructor(props) {
      super(props);
  
      this.toggle = this.toggle.bind(this);
      this.state = {
        isOpen: false
      };
    }
    toggle() {
      this.setState({
        isOpen: !this.state.isOpen
      });
    }
    render() {
        return (
            <Container>
                <Navbar color="light" light expand="md" sticky={'top'}>
                    <NavbarBrand href="/">Mifugo</NavbarBrand>
                    <NavbarToggler onClick={this.toggle} />
                    <Collapse isOpen={this.state.isOpen} navbar>
                        <Nav className="ml-auto" navbar>
                            <NavItem>
                            <NavLink href="/kondo/">Kondo</NavLink>
                            </NavItem>
                            <NavItem>
                            <NavLink href="/mbuzi/">Mbuzi</NavLink>
                            </NavItem>
                            <NavItem>
                            <NavLink href="/ngombe">Ngombe</NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Navbar>
            <Row>
                <Col xs="3">
                    <ListGroup flush>
                        <DataProvider endpoint="api/ngombe/" render={data => (data.map(animal => ( 
                            <ListGroupItem key={animal.id} className="justify-content-between" tag="a" href="#" action>{animal.tag}</ListGroupItem>
                        )))} />
                    </ListGroup>
                </Col>
                <Col xs="9">.col-8</Col>
            </Row>
    </Container>
    );
    }
}

