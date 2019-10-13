import React, {Component} from 'react'
import {render} from 'react-dom'

import {Router, Route, IndexRoute, browserHistory} from 'react-router';

import App from './App'
import UserLogin from './UserLogin'
import Flood from './Flood'

render(
	<Router history={browserHistory}
	<Route component={App}> 
		<Route path="/Flood" component={Flood}/>
		<Route path="/UserLogin" component={UserLogin}>
	</Route>
	</Router>
	);
