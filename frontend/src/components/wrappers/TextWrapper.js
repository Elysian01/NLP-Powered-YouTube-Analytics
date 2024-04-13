import React from "react";
import WrapperHeader from "../headers/WrapperHeader";

import "../css/wrapper.css";

function TextWrapper(props) {
	return (
		<div className="text-wrapper" id="customScroll">
			<WrapperHeader title={props.title} />
			<div className="summarized-text-wrapper">
				<div class="summarized-content">
					{props.summarizedContent}
				</div>
			</div>
		</div>
	);
}

export default TextWrapper;
