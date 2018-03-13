import React, { Component } from 'react';
import './animated.css';

class Animated extends Component {
  render() {
    return (
      <div>
        <h1>Hello World</h1>
        <div className="img-wrap">
          <img src="/China.png" alt=""/>
        </div>
        <div className="rainbow-wrap">
          <h1>Hello CSS</h1>
        </div>
        <div className="rotate"></div>
        <div className="step-wrap"><h1>Typing animation by Lix.<span>&nbsp;</span></h1></div>
      </div>
    );
  }
}

export default Animated;
