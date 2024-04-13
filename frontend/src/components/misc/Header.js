import React from "react";
import "../css/misc.css";

function Header() {
	return (
		<div className="header">
			<img src="../../logo.png" alt="logo" />
			<div>
				<h1 className="header-title">
					<span>
						NLP Powered{" "}
						<span className="white">YouTube Analytics</span>
					</span>
				</h1>
			</div>
		</div>
	);
}

export default Header;
