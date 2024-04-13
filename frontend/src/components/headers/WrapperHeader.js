import React from "react";

function WrapperHeader(props) {
	return (
		<div className="wrapper-header">
			<div>
				<h1 className="header-title">
					<span>{props.title}</span>
				</h1>
			</div>
		</div>
	);
}

export default WrapperHeader;
