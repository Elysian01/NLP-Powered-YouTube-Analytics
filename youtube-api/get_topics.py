import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
from googleapiclient.discovery import build

# Set up the YouTube API key and service
api_key = "YOUR_YOUTUBE_API_KEY"
youtube_service = build('youtube', 'v3', developerKey=api_key)

# Load the pre-existing dataset
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df['comment_text'].tolist()

# Function to fetch comments for a given YouTube video
def get_video_comments(video_id, max_comments=600):
    comments = []
    nextPageToken = None

    while len(comments) < max_comments:
        request = youtube_service.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=min(100, max_comments - len(comments)),
            pageToken=nextPageToken
        )
        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        if "nextPageToken" in response:
            nextPageToken = response["nextPageToken"]
        else:
            break

    return comments[:max_comments]

# Preprocess comments
def preprocess_comments(comments):
    stop_words = set(stopwords.words("english"))
    preprocessed_comments = []

    for comment in comments:
        # Remove URLs and non-alphabetic characters
        comment = re.sub(r"http\S+|www\S+|https\S+", "", comment, flags=re.MULTILINE)
        comment = re.sub(r'\W', ' ', comment)
        
        # Tokenize and remove stopwords
        words = word_tokenize(comment)
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        preprocessed_comments.append(words)

    return preprocessed_comments

# Train LDA model
def train_lda_model(comments, num_topics=5):
    dictionary = corpora.Dictionary(comments)
    corpus = [dictionary.doc2bow(comment) for comment in comments]
    
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    return lda_model

# Get topics for a specific video
def get_topics_for_video(video_id, lda_model, num_comments=600, num_words=5):
    video_comments = get_video_comments(video_id, max_comments=num_comments)
    preprocessed_comments = preprocess_comments(video_comments)
    
    # Predict topics for the comments of the specific video
    video_corpus = [dictionary.doc2bow(comment) for comment in preprocessed_comments]
    video_topics = lda_model[video_corpus]
    
    # Print the topics for the video
    for i, topics in enumerate(video_topics):
        print(f"Topics for Comment {i + 1}: {topics}")

# Main function
def main():
    # Example YouTube video ID
    video_id = "YOUR_YOUTUBE_VIDEO_ID"

    # Load the pre-existing dataset for training
    dataset_path = "path/to/your/dataset.csv"
    all_comments = load_dataset(dataset_path)

    # Preprocess and train LDA model on the entire dataset
    preprocessed_all_comments = preprocess_comments(all_comments)
    lda_model = train_lda_model(preprocessed_all_comments)

    # Get and print topics for the specific video
    get_topics_for_video(video_id, lda_model)

if __name__ == "__main__":
    main()

