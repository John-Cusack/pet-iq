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

  getOwners() {
    this.setState({ isLoading: true });

    axios.get(API + DEFAULT_QUERY)
      .then(result => this.setState({
        owners: result.data.owners,
        isLoading: false
      }))
      .catch(error => this.setState({
        error,
        isLoading: false
      }));
  }


  render() {
    const { owners, isLoading, error } = this.state;

    if (error) {
      return <p>{error.message}</p>;
    }

    if (isLoading) {
      return <p>Loading ...</p>;
    }

    return (
      <div>
        <button onClick={this.getOwners}></button>
        <div>
          {owners.map(owners =>{
            return <Owners
              email={owners.email}
            />
          })}
        </div>
      </div>
    );
  }
}

export default App;
