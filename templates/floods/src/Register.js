import React from 'react';
import './style.scss';
import LoginImage from './LoginImage.svg'

class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {userName:'', email:'', password:''};
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleChange3 = this.handleChange3.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

 
 handleClick(e) {
  console.log(this.state.userName);
  console.log(this.state.email);
  console.log(this.state.password);
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
			<div className = 'form'>
				<div className = 'form-group'>
					<label htmlFor="username">Username</label>
          <input type="text" value = {this.state.userName} name="username" placeholder="username" onChange={this.handleChange1}/>
        </div>
        <div className = 'form-group'>
          <label htmlFor="email">Email Address</label>
          <input value = {this.state.email} type="text" value = {this.state.email} name="Email Address" placeholder="Email Address" onChange={this.handleChange2}/>
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
        	<input value = {this.state.password} type="password" value = {this.state.password} name="password" placeholder="password" onChange={this.handleChange3} />
				</div>
			</div>
      </div>
      <div className="footer">
        <button onClick={this.handleClick} type="button" className="btn">
        	Register
        </button>
      </div>
    </div>
	);
}	
}

export default Register;