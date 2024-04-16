import tensorflow as tf
from analytics import get_topics
from analytics import get_sentiments_of_comments
from analytics import get_keywords
from youtube_api import get_comments, get_video_transcript


import warnings
warnings.filterwarnings("ignore")


class YouTubeAnalytics():
    def __init__(self, url, no_of_comments=100, debug=False):
        self.url = url
        self.no_of_comments = no_of_comments
        self.transcript_available = False
        self.df = None
        self.extracted_keywords = None

        # Fetch Comments
        print("Fetching Comments ...")
        self.df = get_comments(self.url, self.no_of_comments, debug)
        if self.df.empty:
            return "Comments Not Available"
        else:
            print("\n-----------------Comments Fetched-----------------\n\n")
        if debug:
            print("Shape of Comments Dataframe: ", self.df.shape)
            print(self.df.head())

        # Fetch Transcript
        print("Fetching Transcript ...")
        transcript = get_video_transcript(self.url, debug)
        if transcript:
            self.transcript_available = True
            if debug:
                print("Video Transcript: \n" + transcript)
        else:
            print("Transcript not available for this video.\n\n")

        # Keyword Extraction
        print("Commputing Keywords ...")
        self.extracted_keywords = get_keywords(self.df, debug)
        print("\n-----------------Keywords Extracted-----------------\n")

        # Sentiments Analysis
        print("Sentiment Analysis Started ...")
        get_sentiments_of_comments(self.df, debug)
        print("\n-----------------Sentiment Analysis Finished-----------------\n")

        # Topic Modeling
        print("Topic Modeling Started ...\n")
        get_topics(self.df, debug)
        print("\n-----------------Topic Modeling Finished-----------------\n")


if __name__ == "__main__":
    # url = input("Enter YouTube Video Link: ")
    url = "https://youtu.be/bMknfKXIFA8"
    no_of_comments = 100
    YouTubeAnalytics(url, no_of_comments, debug=True)
