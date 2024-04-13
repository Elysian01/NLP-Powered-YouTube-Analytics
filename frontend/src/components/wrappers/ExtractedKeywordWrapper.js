import React from "react";
import WrapperHeader from "../headers/WrapperHeader";

function ExtractedKeywordWrapper(props) {
	return (
		<div className="keywords-wrapper">
			<WrapperHeader title="Extracted Keywords from Comments" />
			{props.extractedKeywords.map((keyword) => (
				<h2 className="keyword" key={keyword}>
					{keyword}{" "}
				</h2>
			))}
		</div>
	);
}

export default ExtractedKeywordWrapper;
