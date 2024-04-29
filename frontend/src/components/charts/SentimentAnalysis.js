import React from "react";
import { PieChart, pieArcLabelClasses } from "@mui/x-charts";

import WrapperHeader from "../headers/WrapperHeader";

function SentimentAnalysis({ sentimentData }) {
  // Convert sentimentData object to array of objects
  const data = Object.keys(sentimentData).map((key) => ({
    id: key,
    value: parseFloat(sentimentData[key].replace("%", "")),
    label: key === "-1" ? "Negative" : key === "0" ? "Neutral" : "Positive",
    color: key === "-1" ? "#ff6c74" : key === "0" ? "#FFBA32" : "#009879",
  }));

  return (
    <div className="sentiment-analysis-wrapper">
      <WrapperHeader title="Sentiment Analysis" />
      <PieChart
        colors={["#ff6c74", "#FFBA32", "#009879"]}
        series={[
          {
            arcLabel: (item) => `${item.value}%`,
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
