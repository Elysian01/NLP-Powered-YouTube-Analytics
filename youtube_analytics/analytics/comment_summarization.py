import numpy as np
import torch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity

def cluster_comments_lda(comments, num_topics):
    # Preprocess comments
    vectorizer = CountVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(comments)

    # Apply LDA
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(X)

    # Get topic distributions for comments
    topic_distributions = lda.transform(X)

    # Assign each comment to the topic with the highest probability
    comment_clusters = np.argmax(topic_distributions, axis=1)

    return comment_clusters

def calculate_silhouette_score(comments, comment_clusters,num_topics):
    # Convert comments to topic distributions
    vectorizer = CountVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(comments)

    # Calculate pairwise cosine similarity between topic distributions of comments
    topic_distributions = LatentDirichletAllocation(n_components=num_topics, random_state=42).fit_transform(X)
    pairwise_similarity = cosine_similarity(topic_distributions)

    # Calculate Silhouette score
    silhouette_avg = silhouette_score(pairwise_similarity, comment_clusters)
    print(f"Silhouette Score for Topic Modelling based Clustering: {silhouette_avg}")

    return silhouette_avg

from transformers import BartForConditionalGeneration, BartTokenizer

# Function to generate a summary for a given text using BART
def generate_bart_summary(text):
    # Load tokenizer
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    # Load model
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    # Move model to GPU if available
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    device = "cpu"
    model.to(device)

    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding="longest")
    inputs.to(device)

    try:
       # Estimate token length of the transcript
        token_length = inputs.input_ids.size(1)
        max_summary_length = token_length // 2  # Set summary length to half of the estimated token length
        # print("MAX_S_L: ",max_summary_length)

        summary_ids = model.generate(inputs.input_ids, max_length=max_summary_length, num_beams=4, early_stopping=True, min_length=10)

        # Decode and return the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        print(f"Error processing text: {e}")
        summary = ""

    return summary

# Function to break down text into smaller chunks
def chunk_text(text, chunk_size=2048):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

# Function to generate summaries for each cluster and concatenate them
def summarize_clusters(df, clusters):
    # Initialize an empty list to store summaries of each cluster
    cluster_summaries = []

    # Iterate over unique cluster labels
    for cluster_label in np.unique(clusters):
        # Get comments belonging to the current cluster
        if cluster_label == -1:
            cluster_comments = df.loc[clusters == cluster_label, 'comments'].tolist()
        else:
            cluster_comments = df.loc[clusters == cluster_label, 'comments'].tolist()

        # Concatenate comments into a single string
        cluster_text = ' '.join(cluster_comments)

        # Chunk the cluster text into smaller parts
        text_chunks = chunk_text(cluster_text)

        # Generate summary for each chunk and concatenate them
        chunk_summaries = [generate_bart_summary(chunk) for chunk in text_chunks]
        cluster_summary = ' '.join(chunk_summaries)

        # Append the summary to the list of summaries
        cluster_summaries.append(cluster_summary)

    # Concatenate summaries of all clusters
    all_clusters_summary = ' '.join(cluster_summaries)

    return all_clusters_summary




def generate_comment_summaries(df2):
    # try:
    #     if not df2:
    #         raise ValueError("No comments provided.")
        

        # Example usage
        comments = df2['comments'].tolist()
        num_topics = 4  # Number of topics
        comment_clusters = cluster_comments_lda(comments, num_topics)
        unique_labels = np.unique(comment_clusters)
        print("Distinct Labels Using Topic Modelling: ", unique_labels)

        calculate_silhouette_score(comments, comment_clusters, num_topics)

        # Generate summaries for each cluster of comments and concatenate them
        summary = summarize_clusters(df2, comment_clusters)
        print("Clustered Summary:", summary)

        return summary

    # except Exception as e:
    #     print("Error occurred during comment summarization:", e)
    #     return None


