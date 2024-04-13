import React from "react";
import "../css/wrapper.css";
import WrapperHeader from "../headers/WrapperHeader";

function TopicWrapper(props) {
	let topics = [
		"TUTORIAL",
		"HELP",
		"REALLY",
		"EXPLANATION",
		"VIDEO",
		"ONE",
		"GOOD",
		"REACT",
		"MANY",
		"TEACHER",
		"GREAT",
		"LOVE",
		"REDHEART",
		"WAY",
		"PERFECT",
		"TEACH",
		"AMAZING",
		"WORK",
		"THANK",
		"WANT",
		"COURSE",
		"WELL",
		"WRITE",
		"WISH",
		"LEARN",
		"EXPLAIN",
		"CODE",
		"FINISH",
		"GET",
		"MUCH",
		"ALOT",
		"BOB",
		"SKILL",
		"SCRIMBA",
		"COMPLETE",
		"PROJECT",
		"WHOLE",
		"LIKE",
	];

	topics = topics.slice(0, 40);

	return (
		<div className="topic-wrapper">
			<WrapperHeader title="Top Topics" />
			{topics.map((topic) => (
				<h2 className="topic" key={topic}>
					{topic}{" "}
				</h2>
			))}
		</div>
	);
}

export default TopicWrapper;
