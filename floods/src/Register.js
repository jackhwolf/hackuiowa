import React from 'react';
import './style.scss';
import LoginImage from './Sign.png'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'

class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', email:'', password:'', act:'s', reg:''};
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleChange3 = this.handleChange3.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

 
 async handleClick(e) {
    const url = 'http://52.8.227.164/user'
    this.setState({reg:'Registered Successfully!'});
    const data = {username:this.state.userName, password:this.state.password, email:this.state.email, action: this.state.act};
    try {
      const response = await fetch(url, 
      {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json'
        },
      });
      const json = await response.json();
      console.log('Success', JSON.stringify(json));
    } catch (error) {
      console.error('Error', error);
    }
  
 }

 handleChange1(e) {
  this.setState({userName: e.target.value})
 }
 handleChange2(e) {
  this.setState({email: e.target.value})
 }
 handleChange3(e) {
  this.setState({password: e.target.value})
 }

render() {
	return (
		<div className = 'outer-container' ref={this.props.containerRef}> 
			<div className = 'header' style={{fontSize:'50px', fontWeight:'bold'}}> REGISTER </div>
      <div className="content">
      <div className="image">
              <img src={LoginImage} />
      </div>
			<Form className = 'form'>
				<Form.Group controlId="formBasicEmail" className = 'form-group'>
          <Form.Label style={{marginTop: '90px', fontWeight:'bold'}}>Username</Form.Label>
					<Form.Text className="text-muted" htmlFor="username"></Form.Text>
          <Form.Control type="email" value = {this.state.userName} placeholder="Username" onChange={this.handleChange1}/>
        </Form.Group>
        <Form.Group controlId="formBasicEmail" className = 'form-group'>
        <Form.Label style={{fontWeight:'bold'}}>Email Address</Form.Label>
        <Form.Text className="text-muted" htmlFor="email">We'll never share your email with anyone else.</Form.Text>
        <Form.Control type="email" value = {this.state.email} placeholder="Email Address" onChange={this.handleChange2}/>
        </Form.Group>
        <Form.Group controlId="formBasicPassword" className = 'form-group'>
        <Form.Label style={{fontWeight:'bold'}}>Password</Form.Label>
        <Form.Text className="text-muted" htmlFor="password"></Form.Text>
        <Form.Control type="password" value = {this.state.password} placeholder="Password" onChange={this.handleChange3}/>
        </Form.Group>
				</Form>
			</div>
      <div className="footer">
        <Button variant="outline-primary" size="lg" onClick={this.handleClick} type="button" className="btn" block>
        	Register
        </Button>
        <span style={{color:'red'}}>{this.state.reg}</span>
      </div>
    </div>
	);
}	
}

export default Register;