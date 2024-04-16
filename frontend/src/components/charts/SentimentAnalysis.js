import React from "react";
import { PieChart, pieArcLabelClasses } from "@mui/x-charts";

import WrapperHeader from "../headers/WrapperHeader";

function SentimentAnalysis() {
	const data = [
		{
			id: 0,
			value: 75,
			label: "Positive",
			color: "#009879",
		},
		{
			id: 1,
			value: 15,
			label: "Neutral",
			color: "#FFBA32",
		},
		{
			id: 2,
			value: 10,
			label: "Negative",
			color: "#ff6c74",
		},
	];
	return (
		<div className="sentiment-analysis-wrapper">
			<WrapperHeader title="Sentiment Analysis" />
			<PieChart
				colors={["#01A98F", "#FFBA32", "#ff6c74"]}
				series={[
					{
						arcLabel: (item) => `${item.value} %`,
						arcLabelMinAngle: 45,
						data,
						highlightScope: {
							faded: "global",
							highlighted: "item",
						},
						faded: {
							innerRadius: 30,
							additionalRadius: -30,
							color: "gray",
						},
					},
				]}
				width={400}
				height={200}
				// slotProps={{
				// 	legend: {
				// 		labelStyle: {
				// 			fontSize: 18,
				// 			fill: "white",
				// 		},
				// 	},
				// }}
				sx={{
					[`& .${pieArcLabelClasses.root}`]: {
						fill: "white",
						fontWeight: "bold",
						fontSize: 18,
					},
				}}
			/>
		</div>
	);
}

export default SentimentAnalysis;
