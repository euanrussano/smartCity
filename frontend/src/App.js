//import logo from './logo.svg';
//import './App.css';
import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    accounts: []
  }
  componentDidMount(){
    this.getAccounts();
  }

  getAccounts(){
    axios
      .get('http://127.0.0.1:8000/api/accounts/')
      .then(res => {
        this.setState({ accounts:res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }
  
  render(){
    return (
      <div>
        {this.state.accounts.map(item => (
         <div key={item.id}>
           <h1>Account {item.id}</h1>
           <p>{item.balance} USD</p>
         </div> 
        ))}
      </div>
    )
  }
}

export default App;
