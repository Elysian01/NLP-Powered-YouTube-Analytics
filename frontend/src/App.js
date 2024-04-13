import "./App.css";
import PageHeader from "./components/headers/PageHeader";
import AnalyticsWrapper from "./components/wrappers/AnalyticsWrapper";

function App() {
	return (
		<div className="bg">
			<PageHeader />
			<AnalyticsWrapper />
		</div>
	);
}

export default App;
