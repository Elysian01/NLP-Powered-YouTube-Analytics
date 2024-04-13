import "./App.css";
import Header from "./components/misc/Header";
import backgroundImage from "./static/imgs/bg.jpg";

const styles = {
	header: {
		backgroundImage: `url(${backgroundImage})`,
		height: "100vh",
		backgroundPosition: "center",
		backgroundRepeat: "no-repeat",
		backgroundSize: "cover",
	},

	content: {
		height: "100%",
		width: "100%",
		backgroundColor: "rgba(11, 9, 38, 0.9)",
	},
};

function App() {
	return (
		<div style={styles.header}>
			<div style={styles.content}>
				<Header />
			</div>
		</div>
	);
}

export default App;
