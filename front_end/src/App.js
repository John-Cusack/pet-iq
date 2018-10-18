import React, { Component } from 'react';
import axios from 'axios';
import './App.css';
import Owners from './components/Owner/Owners'

const API = 'http://127.0.0.1:5000/api/v1/';
const DEFAULT_QUERY = 'owner'

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      owners: [],
      isLoading: false,
      error: null,
    };
  }


  getOwners = () => {
    console.log('started process')
    this.setState({ isLoading: true });
    console.log('got state')
    axios.get(API + DEFAULT_QUERY)
      .then(result => this.setState({
        owners: result,
        isLoading: false
      }))
      .catch(error => this.setState({
        error,
        isLoading: false
      }));
  }


  render() {
    const { owners, isLoading, error } = this.state;
    const string = JSON.stringify(owners, null, 4);
    console.log(string)
    if (error) {
      return <p>{error.message}</p>;
    }

    if (isLoading) {
      return <p>Loading ...</p>;
    }

    return (
      <div>
        <button onClick={this.getOwners}>Get Owner Emails</button>
        <div>
          the emails are{owners.statusCode}
        </div>
      </div>
    );
  }
}

export default App;
