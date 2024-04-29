from flask import Flask, request, jsonify
from youtube_analytics import YouTubeAnalytics

app = Flask(__name__)

# Endpoint to get all the analytics


@app.route('/get_analytics', methods=["POST"])
def get_analytics():
    """Endpoint to fetch analytics for a YouTube video.

    Returns:
        JSON: A JSON object containing extracted keywords, sentiment analysis, and other analytics.

    Example:
        {
            "extracted_keywords": [
                "React",
                "day day day",
                "Bob",
                "react tutorial",
                ...
                "Bobs"
            ],
            "sentiment_analysis": {
                "-1": "5.00%",
                "0": "7.00%",
                "1": "88.00%"
            },
            "transcri...": "..."
        }
    """
    req = request.get_json()

    if "link" in req:
        print("Requested YouTube Link: ", req['link'])

        # url = req['link']
        url = "https://www.youtube.com/watch?v=pg19Z8LL06w&t=2907s"
        no_of_comments = 100
        ya = YouTubeAnalytics(url, no_of_comments, debug=True)
        analytics = ya.get_analysis()
        return jsonify(analytics)
    else:
        return jsonify({"error": "Please provide youtube video link for analytics commputation"})


if __name__ == '__main__':
    app.run(debug=True)
