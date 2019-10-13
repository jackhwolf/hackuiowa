import React from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import './floodstyle.scss';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'
import LoginImage from './Sign.png'
import './graphstyle.scss';
import {
	XYPlot,
	XAxis,
	YAxis,
	VerticalGridLines,
	HorizontalGridLines,
	VerticalBarSeries,
	VerticalBarSeriesCanvas,
	LabelSeries
} from 'react-vis';


class Flood extends React.Component {
	constructor(props) {
		super(props)
		this.state = {address:'', floodwatchResults: {}, showInfo: 'None'};
		this.handleChange10 = this.handleChange10.bind(this);
		this.handleClick1 = this.handleClick1.bind(this);
		this.changeShowInfo = this.changeShowInfo.bind(this);
	}

	changeShowInfo() {
		console.log("showing info")
		this.setState({
			showInfo: ''
		})
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
		this.setState({
			showInfo: ''
		})
	}

	render() {
		return (
			<div className="style1">
				<div className="image1">
					<img src={LoginImage} />
				</div>
				<Container className="contain1">
				<Row>
					<Col>
						<Form className = 'form2'>
							<Form.Group controlId="formBasicEmail" className = 'form-group'>
								<Form.Label style={{marginTop: '90px', fontWeight:'bold', fontSize:'30px', color:'white'}}>ENTER ADDRESS</Form.Label>
								<Form.Control type="email" placeholder="Address" onChange={this.handleChange10}/>
								<Form.Text className="text-muted" htmlFor="username"></Form.Text>
								<Button variant="outline-light" size="lg" onClick={this.handleClick1} className="btn" block>
								Submit
								</Button>
							</Form.Group>
						</Form>
				</Col>
				<Col>
					<div className="Graphstyle">
						<div>
							<XYPlot title="Cumulative sum of rainfall" xType="ordinal" width={500} height={500} xDistance={100}>
							<VerticalGridLines />
							<HorizontalGridLines />
							<XAxis title="Days" style={{line:{stroke: '#FFFF33'}, ticks: {stroke: '#FFFF33'}}}/>
							<YAxis title="Cumulative sum of rainfall"
							style={{line:{stroke: '#FFFF33'}, ticks: {stroke: '#FFFF33'}, text: {align: {vertical: 'top', horizontal: 'lefts'}}}}/>
							<VerticalBarSeries title="Cumulative sum of rainfall" className="vertical-bar-series-example" data={this.state.floodwatchResults['rainfall']} />
							</XYPlot>
						</div>
					</div>
				</Col>
				<Col className="col3">
					<Card style={{ width: '18rem', display: this.state.showInfo}}>
						<Card.Body style={{paddingTop: '10px'}}>
							<Card.Text>
								{this.state.floodwatchResults['summary']}
							</Card.Text>
							Danger: {this.state.floodwatchResults['danger']}%
							<Card.Text>
						   </Card.Text>
						</Card.Body>
					</Card>
				</Col>
			</Row>
		</Container>
	</div>
			)}
	}

	export default Flood;