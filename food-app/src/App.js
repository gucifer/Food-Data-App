import './App.css';
import React from 'react';
import reply from "./reply.json";
import reply2 from "./reply2.json";

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
    this.props.parentCallback(this.state.value,null,"view1");
    event.preventDefault();
  }

  checkKey(event){
    if(event.key === 'Enter'){
      this.props.parentCallback(this.state.value,null,"view1");
    }
  }
  render() {
    return (
    <div id="searchbar">
      <form onSubmit={e => { e.preventDefault(); }}>
        <input type="text" placeholder={this.state.value} autofocus id="searchinput" onChange={this.handleChange} onKeyPress={this.checkKey}/>
        <button onClick={this.handleSubmit}>
          <div id="searchicon">&#9906;</div>
        </button>
      </form>
    </div>  
    );
  }
}
class FoodList extends React.Component {
  constructor(props){
    super(props);
    this.state = {value:""};
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick(event){
    this.props.parentCallback(null,event.target.className,"view2");
  }

  render() {
    return(
      <div id="foodlist">
        {
          reply["recipes"].map((recipe) => {
            return (
              <div id="listitem" className={recipe.id} onClick={this.handleClick}>
                <div id="itemimage" className={recipe.id}>
                  <img src={recipe.image} alt={recipe.title} className={recipe.id}/>
                </div>
                <div id="itemdata" className={recipe.id}>
                  {recipe.title}
                </div>
              </div>
            )
          })
        }
      </div>
    );
  }
}

class FoodDetail extends React.Component{
  constructor(props){
    super(props);
    this.state = {id:-1, summary: true, ingredients:false, recipe:false, nutrients:false};
    this.openTab = this.openTab.bind(this);
  }
  openTab(event) {
    if(event.target.className === "Summary") {
      this.setState({summary: true, ingredients:false, recipe:false, nutrients:false})
    }
    if(event.target.className === "Ingredients") {
      this.setState({summary: false, ingredients:true, recipe:false, nutrients:false})
    }
    if(event.target.className === "Recipe") {
      this.setState({summary: false, ingredients:false, recipe:true, nutrients:false})
    }
    if(event.target.className === "Nutrients") {
      this.setState({summary: false, ingredients:false, recipe:false, nutrients:true})
    }
    if(event.target.className === "Back") {
      this.props.parentCallback(null,null,"view1");
    }
  }
  render() {
    return(
      <div id="fooddetail">
        <h2>{reply2.name}</h2>
        <div class="tab">
          <button class="tablinks Back" onClick={this.openTab} className="Back">Back</button>
          <button class="tablinks" onClick={this.openTab} className="Summary">Summary</button>
          <button class="tablinks" onClick={this.openTab} className="Ingredients">Ingredients</button>
          <button class="tablinks" onClick={this.openTab} className="Recipe">Recipe</button>
          <button class="tablinks" onClick={this.openTab} className="Nutrients">Nutrients</button>
        </div>
        <div id="Summary" class={this.state.summary?'':'invisible'}>
          <h3>Summary</h3>
          <p dangerouslySetInnerHTML={{__html: reply2.summary}}></p>
        </div>
        
        <div id="Ingredients" class={this.state.ingredients?'':'invisible'}>
          <h3>Ingredients</h3>
            {
              reply2.ingredients.map((ing,i) => {
                return (
                  <div class="ingredient-item">
                  <div class="split left">
                  <strong>Item {i+1}</strong> : {ing.orig}
                  </div>
                  <div class="split right">
                  <img src={ing.image} id="ing-image" alt={ing.name}/>
                  </div>
                  </div>
                )
              })
            }
        </div>
        
        <div id="Recipe" class={this.state.recipe?'':'invisible'}>
          <h3>Recipe</h3>
          <p>Coming Soon</p>
        </div>

        <div id="Nutrients" class={this.state.nutrients?'':'invisible'}>
          <h3>Nutrients</h3>
          <p>Coming Soon</p>
        </div>
      </div>
    );
  }
}

class Mainpage extends React.Component {
  state = { value: "",view: "view1",id:null }
  callbackFunction = (search,id,view) => {
    if(search === null){
      search = this.state.search;
    }
    if(view === null){
      view = this.state.view;
    }
    if(id === null){
      id = this.state.id;
    }
    this.setState({value: search,view:view,id:id});
  }

  render() {
    return (
      <div>
        <Searchbar parentCallback = {this.callbackFunction}/>
        {
          this.state.view === "view1"?
        <FoodList parentCallback = {this.callbackFunction} searchterm = {this.state.value}/> :
        <FoodDetail parentCallback = {this.callbackFunction}/>
        }
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
