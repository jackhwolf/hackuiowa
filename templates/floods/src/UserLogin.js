import React from 'react';
import './style.scss';
import LoginImage from './LoginImage.svg'

class UserLogin extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', password:''};
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

   async handleClick(e) {
   	const url = 'http://52.8.227.164/user'
   	const data = {username:this.state.userName, password:this.state.password};
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
  this.setState({password: e.target.value})
 }
 

render() {
	return (
		<div className = 'outer-container' ref={this.props.containerRef}> 
			<div className = 'header'> Login </div>
			<div className="content">
			<div className="image">
            	<img src={LoginImage} />
          	</div>
			<div className = 'form'>
				<div className = 'form-group'>
					<label htmlFor="username">Username</label>
             		<input type="text" value = {this.state.userName}  name="username" placeholder="username" onChange={this.handleChange1}/>
             	</div>
             	<div className="form-group">
              		<label htmlFor="password">Password</label>
              		<input type="password" value = {this.state.password}  name="password" placeholder="password" onChange={this.handleChange2}/>
				</div>
			</div>
			</div>
        	<div className="footer">
          		<button onClick={this.handleClick} type="button" className="btn">
            		Login
          		</button>
          	</div>
     	 </div>
	);
}	
}

export default UserLogin;