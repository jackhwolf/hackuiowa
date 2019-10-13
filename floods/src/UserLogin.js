import React from 'react';
import './style.scss';
import LoginImage from './Sign.png'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import {BrowserRouter as Router, Redirect, Route, withRouter} from 'react-router-dom'
//import Logfailed from './Logfailed'
import Flood from './Flood'

class UserLogin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', password:'', act:'l', flag:0, txt:'', redir:'false'};
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
        console.log(json['Cookie']);
        let path = `Flood`;
        this.props.history.push(path)
        this.setState({flag: 1, txt:'', redir:'true'});
        this.props.loginSuccessHandler()
      }
      else {
         this.setState({flag:2, txt:'Wrong Username or Password'}); 
      }
   		console.log('Success', JSON.stringify(json));
      //console.log(json['Cookie']);
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
  console.log("ll "+this.state.redir)
    // if(this.state.redir === 'true') {
    //   return <Redirect to='/Flood'/>;
    // }
	return ( 
		  <div className = 'outer-container' ref={this.props.containerRef}> 
			<div className = 'header' style={{fontSize:'50px', fontWeight:'bold'}}> LOGIN </div>
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
        <Form.Group controlId="formBasicPassword" className = 'form-group'>
        <Form.Label style={{fontWeight:'bold'}}>Password</Form.Label>
        <Form.Text className="text-muted" htmlFor="password"></Form.Text>
        <Form.Control type="password" value = {this.state.password} placeholder="Password" onChange={this.handleChange2}/>
          <br></br>
          <span style={{color:'red'}}>{this.state.txt}</span>
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

export default withRouter(UserLogin);