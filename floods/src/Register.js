import React from 'react';
import './style.scss';
import LoginImage from './LoginImage.png'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'

class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', email:'', password:'', act:'s'};
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleChange3 = this.handleChange3.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

 
 async handleClick(e) {
    const url = 'http://52.8.227.164/user'
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
			<div className = 'header'> Register </div>
      <div className="content">
      <div className="image">
              <img src={LoginImage} />
      </div>
			<Form className = 'form'>
				<Form.Group controlId="formBasicEmail" className = 'form-group'>
          <Form.Label style={{marginTop: '90px'}}>Username</Form.Label>
					<Form.Text className="text-muted" htmlFor="username"></Form.Text>
          <input type="text" value = {this.state.userName} name="username" placeholder="username" onChange={this.handleChange1}/>
        </Form.Group>
        <Form.Group controlId="formBasicEmail" className = 'form-group'>
        <Form.Label>Email Address</Form.Label>
        <Form.Text className="text-muted" htmlFor="email">We'll never share your email with anyone else.</Form.Text>
          <input value = {this.state.email} type="text" value = {this.state.email} name="Email Address" placeholder="Email Address" onChange={this.handleChange2}/>
        </Form.Group>
        <Form.Group controlId="formBasicPassword" className = 'form-group'>
        <Form.Label>Password</Form.Label>
        <Form.Text className="text-muted" htmlFor="password"></Form.Text>
        	<input value = {this.state.password} type="password" value = {this.state.password} name="password" placeholder="password" onChange={this.handleChange3} />
        </Form.Group>
				</Form>
			</div>
      <div className="footer">
        <Button variant="outline-primary" size="lg" onClick={this.handleClick} type="button" className="btn" block>
        	Register
        </Button>
      </div>
    </div>
	);
}	
}

export default Register;