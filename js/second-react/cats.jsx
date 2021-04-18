"use strict";

const App = () => {
	const [cats, setCats] = React.useState([
		{name: "cat1"}, // TODO: add IDs for cats to use React Keys
		{name: "cat2"}
	]);

	const insertCat = (e) => {
		setCats([...cats, {name: "newcat"}]);
	};

	const removeCat = (name) => {
		setCats(cats.filter((cat) => cat.name !== name));
	};

	const renameCat = (old, newName) => {
		setCats(cats.map((cat) => cat.name === old
									? {...cat, name: newName}
									: cat));
	};

	return <div id="app">
		<button onClick={insertCat}>meow</button>
		<CatList catlist={cats} />
	</div>
}

const CatList = (props) => {
	return <ul id="cats">
		{props.catlist.map((cat, index) => <Cat name={cat.name} />)}
	</ul>
};

const Cat = (props) => {
	return <li className="cat">{props.name}</li>
}

ReactDOM.render(<App />, document.querySelector('#root'));
