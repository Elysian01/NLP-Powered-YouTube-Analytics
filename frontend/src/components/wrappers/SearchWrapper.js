import React from "react";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faCoffee } from "@fortawesome/fontawesome-free-solid";
import { faChartLine } from "@fortawesome/fontawesome-free-solid";

function SearchWrapper() {
	const [link, setLink] = useState("");

	const fetchAnalysis = async () => {
		setLink("");
	};

	return (
		<div className="search-wrapper">
			<div class="input-wrapper">
				<input
					type="link"
					placeholder="Enter YouTube Video Link"
					name="video_link"
					id="video_link"
					value={link}
					onChange={(e) => setLink(e.target.value)}
					required
				/>
			</div>
			<div>
				<button className="red-btn" onClick={fetchAnalysis}>
					{/* <FontAwesomeIcon icon={faCoffee} /> */}
					<FontAwesomeIcon icon={faChartLine} />
					{/* <FontAwesomeIcon icon="fa-solid fa-magnifying-glass-chart" /> */}
					&nbsp; Fetch Analytics
				</button>
			</div>
			<div>
				<button className="dark-btn">
					<i class="fa fa-lg fa-brands fa-github"></i> &nbsp;
					View Code
				</button>
			</div>
		</div>
	);
}

export default SearchWrapper;
