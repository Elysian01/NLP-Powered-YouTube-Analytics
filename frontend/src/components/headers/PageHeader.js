import React from "react";
import "../css/misc.css";
import logo from "../../static/logo.png";

function PageHeader() {
	return (
		<div className="header">
			<img src={logo} alt="logo" />
			<div>
				<h1 className="header-title">
					<span>
						NLP Powered <span>YouTube Analytics</span>
					</span>
				</h1>
			</div>
		</div>
	);
}

export default PageHeader;
