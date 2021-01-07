import './App.css';
import React from 'react';



class FoodSearch extends React.Component {
  constructor(props){
    super(props);
    this.state = {value: '', searched: false};

    this.handleChange = this.handleChange.bind(this);
  }
  handleChange = event => {
    this.setState({value: event.target.value});
  }
  afterSubmission = event => {
    this.setState({searched: true});
    event.preventDefault();
    this.componentDidMount();
  }
  componentDidMount() {
    fetch("https://api.edamam.com/search?q=chicken&app_id=5b888f44&app_key=3dc654182b583fe360491aceb99db768")
    .then(response => {
      console.log(response);
    })
    .catch(err => {
      console.error(err);
    });
  }
  render() {
    console.log(this.state.totalReactPackages);
    return (
      <div>
      <form id="mainsearchform" onSubmit={this.afterSubmission}>
        <input type="text" id="mainsearchfield" onChange={this.handleChange}/>
        <input type="submit" value="Search" id="mainsearchbutton"/>
      </form>
      <p>{this.state.totalReactPackages}</p>
      </div>
    );
  }

}



function App() {
  return (
    <FoodSearch name="Food item" />
  );
}

export default App;
