import './App.css';
import React from 'react';

class Searchbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: 'Search'};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.checkKey = this.checkKey.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    this.props.parentCallback(this.state.value);
    event.preventDefault();
  }

  checkKey(event){
    if(event.key === 'Enter'){
      this.props.parentCallback(this.state.value);
    }
  }
  render() {
    return (
    <div id="searchbar">
      <form onSubmit={e => { e.preventDefault(); }}>
        <input type="text" placeholder={this.state.value} autofocus id="searchinput" onChange={this.handleChange} onKeyPress={this.checkKey}/>
        <input type="button" value="Search" id="searchbutton" onClick={this.handleSubmit}/>
      </form>
    </div>  
    )
  }
}

class FoodList extends React.Component {

  render() {
    console.log('here');
    return(
      <div id="foodlist">{this.props.searchterm}</div>
    );
  }
}

class Mainpage extends React.Component {
  state = { value: "" }
  callbackFunction = (search) => {
    this.setState({value: search});
  }

  render() {
    return (
      <div>
        <Searchbar parentCallback = {this.callbackFunction}/>
        <FoodList searchterm = {this.state.value}/>
      </div>
    );
  }

}

function App() {
  return (
    <Mainpage/>
  );
}

export default App;
