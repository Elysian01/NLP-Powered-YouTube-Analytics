import React from "react";
import "../css/wrapper.css";
import SearchWrapper from "./SearchWrapper";
import SentimentAnalysis from "../charts/SentimentAnalysis";
import TopicWrapper from "./TopicWrapper";
import TextWrapper from "./TextWrapper";
import ExtractedKeywordWrapper from "./ExtractedKeywordWrapper";

function AnalyticsWrapper() {
	const summarizedContent =
		"Whenever we need to make use of side effects in our application, useEffect is the way to go. This hook doesn't present many complications, except for non-primitive data types, due to how JavaScript handles them. According to the official documentation, effects run after every completed render, but you can choose to fire them only when certain values have changed. This hook uses an array of dependencies: variables or states that useEffect listen to for changes. When their values change, the main body of the useEffect hook is executed. The return statement of this hook is used to clean methods that are already running, such as timers. The first time this hook is called, its main body is the one that is going to be evaluated first. All other subsequent times the hook is called, the return statement will be evaluated first, and, after that, the hook's main body. This behaviour is especially useful for cleaning code that is already running before run it again, which enable us to prevent memory leaks. There is an interesting behaviour with this hook when we use non-primitive JavaScript data types as dependencies (e.g., arrays, objects, functions). With primitive values, such as numbers and strings, we can define a variable from another variable, and they will be the same";

	let extractedKeywords = [
		"finding this masterpiece",
		"React tutorial Ive",
		"Bob Zirolls teaching",
		"Sir Bob Ziroll",
		"React tutorial hands",
		"perfect react tutorial",
		"GOOD TEACHER BOB",
		"great job Bob",
		"Bob Ziroll taught",
		"react great work",
		"Bobs teaching Helped",
		"teaching methods Bob",
		"make learning React",
		"job Bob youre",
		"enjoyed Bobs teaching",
		"good tutorial Amazing",
		"learn React Trust",
		"beginner friendly react",
		"started learning react",
		"react video couple",
		"Bob Ziroll",
		"great tutorial Happy",
		"level react skills",
		"code GOAT Amazing",
		"react router domreduxtoolkit",
		"tutorial Amazing pace",
		"Great teacher Tks",
		"Ive finally completed",
		"react tutorial",
		"amazing teaching skill",
	];

	extractedKeywords = extractedKeywords.slice(0, 20);

	return (
		<div className="main">
			<div className="row">
				<SearchWrapper />
			</div>
			<div className="row">
				<ExtractedKeywordWrapper
					extractedKeywords={extractedKeywords}
				/>
			</div>
			<div className="row">
				<SentimentAnalysis />
				<TopicWrapper />
			</div>
			<div className="row">
				<TextWrapper
					title="Comment Summarization"
					summarizedContent={summarizedContent}
				/>
				<TextWrapper
					title="Transcribe Summarization"
					summarizedContent={summarizedContent}
				/>
			</div>
		</div>
	);
}

export default AnalyticsWrapper;
