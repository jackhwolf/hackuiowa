import React from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Graph from './Graph'
import './floodstyle.scss';

class Flood extends React.Component {
  constructor(props) {
  	super(props)
  	this.state = {address:'', floodwatchResults: {}};
    this.handleChange10 = this.handleChange10.bind(this);
    this.handleClick1 = this.handleClick1.bind(this);

  }

  handleChange10(e) {
  	this.setState({address: e.target.value})
 }

 async handleClick1(e) {
   	const url = 'http://52.8.227.164/floodwatch'
   	const data = {address:this.state.address};
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
   		this.setState({
   			floodwatchResults: json
   		});
   	} catch (error) {
   		console.error('Error', error);
   	}
   }
  	render() {
  		return (
  			<>
  		<div className = "style1">
  		<Form className = 'form2'>
        <Form.Group controlId="formBasicEmail" className = 'form-group'>
          <Form.Label style={{marginTop: '90px', fontWeight:'bold'}}>Enter Address</Form.Label>
          <Form.Control type="email" placeholder="Address" onChange={this.handleChange10}/>
          <Form.Text className="text-muted" htmlFor="username"></Form.Text>
          <Button variant="outline-primary" size="lg" onClick={this.handleClick1} className="btn" block>
            		Submit
          	</Button>
        </Form.Group>
        </Form>
        </div>
        <div styleName={{marginVertical: '0'}} className="Graphstyle">
          	<Graph styleName={{marginVertical: '0'}} data={this.state.floodwatchResults['rainfall']}/>
          </div>
          </>
  			)}
}

export default Flood;