from youtube_analytics.analytics import get_topics
from youtube_analytics.analytics import get_sentiments_of_comments
from youtube_analytics.analytics import get_keywords
from youtube_analytics.analytics import generate_youtube_transcript_summaries
from youtube_analytics.analytics import generate_comment_summaries
from youtube_analytics.youtube_api import get_comments, get_video_transcript

import warnings
warnings.filterwarnings("ignore")


class YouTubeAnalytics():
    def __init__(self, url, no_of_comments=100, debug=False):
        self.url = url
        self.no_of_comments = no_of_comments
        self.debug = debug
        self.analytics = {}

        self.transcript_available = False
        self.df = None
        self.extracted_keywords = None
        self.sentiment_analysis_data = None
        self.comment_summary = ""
        self.transcript_summary = ""
        self.topics = None

    def get_analysis(self):
        # Fetch Comments
        print("Fetching Comments ...")
        self.df = get_comments(self.url, self.no_of_comments, self.debug)

        if self.df.empty:
            return "Comments Not Available"
        else:
            print("\n-----------------Comments Fetched-----------------\n\n")

        if self.debug:
            print("Shape of Comments Dataframe: ", self.df.shape)
            print(self.df.head())

        # Fetch Transcript
        print("Fetching Transcript ...")
        transcript = get_video_transcript(self.url, self.debug)
        if transcript:
            self.transcript_available = True
            self.analytics["transcript_available"] = True
            if self.debug:
                print("Video Transcript: \n" + transcript)
        else:
            print("Transcript not available for this video.\n\n")
            self.analytics["transcript_available"] = False

        # Keyword Extraction
        print("Commputing Keywords ...")
        self.extracted_keywords = get_keywords(self.df, self.debug)
        self.analytics["extracted_keywords"] = self.extracted_keywords
        print("\n-----------------Keywords Extracted-----------------\n")

        # Sentiments Analysis
        print("Sentiment Analysis Started ...")
        self.sentiment_analysis_data = get_sentiments_of_comments(
            self.df, self.debug)
        self.analytics["sentiment_analysis"] = self.sentiment_analysis_data
        print("\n-----------------Sentiment Analysis Finished-----------------\n")

        # Topic Modeling
        print("Topic Modeling Started ...\n")
        self.topics = get_topics(self.df, self.debug)
        self.analytics["topics"] = self.topics
        print("\n-----------------Topic Modeling Finished-----------------\n")

        # Transcribe Summarization
        print("Transcribe Summarization Started ...")
        if (self.analytics["transcript_available"]):
            self.transcript_summary = generate_youtube_transcript_summaries(transcript)
            # print(self.transcript_summary)
            self.analytics["generated_summary"]= self.transcript_summary
        print("\n-----------------Transcribe Summarization Finished-----------------\n")

        # Comment Summarization
        if not self.df.empty:  # Check if comments are available
            print("Comment Summarization Started ...")
            self.comment_summary = generate_comment_summaries(self.df)
            self.analytics["generated_comment_summary"] = self.comment_summary
            print("\n-----------------Comment Summarization Finished-----------------\n")
        else:
            print("No comments available. Skipping comment summarization.\n")

        return self.analytics


if __name__ == "__main__":
    # url = input("Enter YouTube Video Link: ")
    url = "https://youtu.be/bMknfKXIFA8"
    no_of_comments = 100
    ya = YouTubeAnalytics(url, no_of_comments, debug=True)
    print(ya.get_analysis())
