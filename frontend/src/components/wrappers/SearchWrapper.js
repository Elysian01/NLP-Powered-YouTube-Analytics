import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartLine } from "@fortawesome/fontawesome-free-solid";

function SearchWrapper({ link, setLink, fetchData }) {
  const handleFetchData = () => {
    fetchData(link);
  };

  return (
    <div className="search-wrapper">
      <div className="input-wrapper">
        <input
          type="link"
          placeholder="Enter YouTube Video Link"
          name="video_link"
          id="video_link"
          value={link}
          onChange={(e) => setLink(e.target.value)}
          required
        />
      </div>
      <div>
        <button className="red-btn" onClick={handleFetchData}>
          <FontAwesomeIcon icon={faChartLine} />
          &nbsp; Fetch Analytics
        </button>
      </div>
      <div>
        <button className="dark-btn">
          <a
            href="https://github.com/Elysian01/NLP-Powered-YouTube-Analytics"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fa fa-lg fa-brands fa-github"></i> &nbsp; View Code
          </a>
        </button>
      </div>
    </div>
  );
}

export default SearchWrapper;
