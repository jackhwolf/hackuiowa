import React from 'react';
import UserLogin from './UserLogin';
import Register from './Register'
import {BrowserRouter as Router, Route} from 'react-router-dom'
import { withRouter } from 'react-router-dom'
import Flood from './Flood'


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      login: true,
      divLoginDisplay: '',
      divLandingDisplay: 'None'
    };
    this.toggleDivViz = this.toggleDivViz.bind(this);
  }

  componentDidMount() {
    this.rightSide.classList.add("right");
  }

toggleDivViz() {
  var divLogin = this.state.divLoginDisplay
  var divLanding = this.state.divLandingDisplay
  this.setState({
    divLoginDisplay: divLanding,
    divLandingDisplay: divLogin
  })
}

changeState() {
    const { login } = this.state;

    if (login) {
      this.rightSide.classList.remove("right");
      this.rightSide.classList.add("left");
    } else {
      this.rightSide.classList.remove("left");
      this.rightSide.classList.add("right");
    }
    this.setState(prevState => ({ login: !prevState.login }));
  }

render() {
    const {login} = this.state;
    const curr = login ? "Register" : "Login";
    const currentActive = login ? "login" : "register";
  return (
    <Router>
        <div className="App">
          <div className="login" style={{display: this.state.divLoginDisplay}}>
            <div className="container" ref={ref => (this.container = ref)}>
            {login && (
                <UserLogin containerRef={ref => (this.curr = ref)} loginSuccessHandler={this.toggleDivViz}/>
              )}
            {!login && (
                <Register containerRef={ref => (this.curr = ref)} />
              )}
            </div>
            <RightSide
            curr={curr}
            currentActive={currentActive}
            containerRef={ref => (this.rightSide = ref)}
            onClick={this.changeState.bind(this)}
          />
          </div>
        </div>

        <div style={{display: this.state.divLandingDisplay}}>
          <Flood />
        </div>
        </Router>
  );
}
}

const RightSide = props => {
  return (
    <div
      className="right-side"
      ref={props.containerRef}
      onClick={props.onClick}
    >
      <div className="inner-container">
        <div className="text">{props.curr}</div>
      </div>
    </div>
  );
};

export default App;
