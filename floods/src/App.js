import React from 'react';
import './App.css';
import UserLogin from './UserLogin';
import Register from './Register'


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      login: true
    };
  }

  componentDidMount() {
    this.rightSide.classList.add("right");
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
        <div className="App">
          <div className="login">
            <div className="container" ref={ref => (this.container = ref)}>
            {login && (
                <UserLogin containerRef={ref => (this.curr = ref)} />
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
