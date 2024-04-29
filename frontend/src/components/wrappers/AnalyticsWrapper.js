import React, { useState } from "react";
import "../css/wrapper.css";
import SearchWrapper from "./SearchWrapper";
import SentimentAnalysis from "../charts/SentimentAnalysis";
import TopicWrapper from "./TopicWrapper";
import TextWrapper from "./TextWrapper";
import ExtractedKeywordWrapper from "./ExtractedKeywordWrapper";

function AnalyticsWrapper() {
  const [analyticsData, setAnalyticsData] = useState(null);
  const [link, setLink] = useState("");

  const fetchData = async (link) => {
    try {
      const response = await fetch("http://127.0.0.1:5000/get_analytics", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ link: link }),
      });
      const data = await response.json();
      setAnalyticsData(data);
    } catch (error) {
      console.error("Error fetching analytics:", error);
    }
  };

  return (
    <div className="main">
      <div className="row">
        <SearchWrapper link={link} setLink={setLink} fetchData={fetchData} />
      </div>
      {analyticsData && (
        <>
          <div className="row">
            <ExtractedKeywordWrapper
              extractedKeywords={analyticsData.extracted_keywords}
            />
          </div>
          <div className="row">
            <SentimentAnalysis
              sentimentData={analyticsData.sentiment_analysis}
            />
            <TopicWrapper topics={analyticsData.topics} />
          </div>
          <div className="row">
            <TextWrapper
              title="Comment Summarization"
              summarizedContent={analyticsData.generated_comment_summary}
            />
            <TextWrapper
              title="Transcribe Summarization"
              summarizedContent={analyticsData.generated_summary}
            />
          </div>
        </>
      )}
    </div>
  );
}

export default AnalyticsWrapper;
