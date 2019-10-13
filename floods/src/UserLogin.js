import React from 'react';
import './style.scss';
import LoginImage from './LoginImage.png'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import {BrowserRouter as Router, Redirect} from 'react-router-dom'
//import Logfailed from './Logfailed'
import Flood from './Flood'

class UserLogin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', password:'', act:'l', flag:0, txt:''};
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }


   async handleClick(e) {
   	const url = 'http://52.8.227.164/user'
   	const data = {username:this.state.userName, password:this.state.password, action:this.state.act};
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
      if(json['Result'] === 1) {
        this.setState({flag: 1, txt:''});
      }
      else {
         this.setState({flag:2, txt:'Wrong username and Password'}); 
      }
   		console.log('Success', JSON.stringify(json));
      console.log(json['Cookie']);
   	} catch (error) {
   		console.error('Error', error);
   	}
  
 }

 handleChange1(e) {
  this.setState({userName: e.target.value})
 }
 handleChange2(e) {
  this.setState({password: e.target.value})
 }
 

render() {
  if (this.state.flag === 1) {
    console.log("KKKK")
        return <Redirect to='/Flood' />
    }
	return (
		<div className = 'outer-container' ref={this.props.containerRef}> 
			<div className = 'header'> Login </div>
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
        <Form.Group controlId="formBasicPassword" className = 'form-group'>
        <Form.Label>Password</Form.Label>
        <Form.Text className="text-muted" htmlFor="password"></Form.Text>
          <input type="password" value = {this.state.password}  name="password" placeholder="password" onChange={this.handleChange2} />
          <br></br>
          <span>{this.state.txt}</span>
        </Form.Group>
        </Form>
			</div>
        <div className="footer">
          		<Button variant="outline-primary" size="lg" onClick={this.handleClick} className="btn" block>
            		Login
          		</Button>
          </div>
      </div>
	);
}	
}

export default UserLogin;