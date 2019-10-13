"use strict";

const App = () => {
  const [cats, setCats] = React.useState([{
    name: "cat1"
  }, // TODO: add IDs for cats to use React Keys
  {
    name: "cat2"
  }]);

  const insertCat = e => {
    setCats([...cats, {
      name: "newcat"
    }]);
  };

  const removeCat = name => {
    setCats(cats.filter(cat => cat.name !== name));
  };

  const renameCat = (old, newName) => {
    setCats(cats.map(cat => cat.name === old ? { ...cat,
      name: newName
    } : cat));
  };

  return React.createElement("div", {
    id: "app"
  }, React.createElement("button", {
    onClick: insertCat
  }, "meow"), React.createElement(CatList, {
    catlist: cats
  }));
};

const CatList = props => {
  return React.createElement("ul", {
    id: "cats"
  }, props.catlist.map((cat, index) => React.createElement(Cat, {
    name: cat.name
  })));
};

const Cat = props => {
  return React.createElement("li", {
    className: "cat"
  }, props.name);
};

ReactDOM.render(React.createElement(App, null), document.querySelector('#root'));
