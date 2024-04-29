import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from youtube_analytics.analytics import generate_youtube_transcript_summaries

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

def generate_comment_cluster_summaries(comment_clusters, comments, chunk_size=8192):
    """
    Generates summaries for each cluster of comments and concatenates the returned summaries.

    Parameters:
        comment_clusters (array-like): Cluster labels for each comment.
        comments (list): List of comments.
        chunk_size (int): Size of each transcript chunk.

    Returns:
        str: Concatenated summary of all comment clusters.
    """
    # Get unique cluster labels
    unique_labels = np.unique(comment_clusters)
    
    # Initialize concatenated summary
    concatenated_summary = ""
    
    # Iterate over each cluster
    for label in unique_labels:
        # Get comments in the current cluster
        cluster_comments = [comments[i] for i, cluster_label in enumerate(comment_clusters) if cluster_label == label]
        
        # Generate summary for the cluster
        cluster_summary = generate_youtube_transcript_summaries(cluster_comments, chunk_size=chunk_size)
        
        # Concatenate the summary to the overall summary
        concatenated_summary += cluster_summary + " "
    
    return concatenated_summary



def generate_comment_summaries(comments):
    try:
        if not comments:
            raise ValueError("No comments provided.")
        

        print("Comments: ",comments)
        num_topics = 4  # Number of topics
        comment_clusters = cluster_comments_lda(comments, num_topics)
        unique_labels = np.unique(comment_clusters)
        print("Distinct Labels Using Topic Modelling: ", unique_labels)
        calculate_silhouette_score(comments, comment_clusters, num_topics)

        # Generate summaries for each cluster of comments and concatenate them
        clustered_summary = generate_comment_cluster_summaries(comment_clusters, comments)
        print("Clustered Summary:", clustered_summary)

        return clustered_summary

    except Exception as e:
        print("Error occurred during comment summarization:", e)
        return None

