import React from "react";
import WrapperHeader from "../headers/WrapperHeader";

import "../css/wrapper.css";

function TextWrapper(props) {
  let text;
  if (props.summarizedContent == "") {
    text = "Not Available";
  } else {
    text = props.summarizedContent;
  }
  return (
    <div className="text-wrapper" id="customScroll">
      <WrapperHeader title={props.title} />
      <div className="summarized-text-wrapper">
        <div className="summarized-content">{text}</div>
      </div>
    </div>
  );
}

export default TextWrapper;
