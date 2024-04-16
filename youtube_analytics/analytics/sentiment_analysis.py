from transformers import pipeline
from nltk.tokenize import word_tokenize
from collections import Counter


def truncate_comment(comment, max_seq_length=128):
    '''Function to truncate a comment to have a maximum of max_seq_length tokens'''
    tokens = word_tokenize(comment)
    truncated_tokens = tokens[:max_seq_length]
    truncated_comment = ' '.join(truncated_tokens)
    return truncated_comment


def get_sentiments_of_comments(df, debug=False) -> dict:
    """
    Performs sentiment analysis on the comments in the DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame containing the comments.
        debug (bool): Whether to print out the intermediate results or not.

    Returns:
        dict: A dictionary containing the percentage of positive, neutral, and negative comments.
              The keys are 'Positive', 'Neutral', and 'Negative'.
              The values are strings representing the percentage of each sentiment category.
              For example: {'Positive': '70.00%', 'Neutral': '20.00%', 'Negative': '10.00%'}

    Note:
        This function requires the 'transformers' library to be installed.
    """
    # Load sentiment analysis model
    specific_model = pipeline(
        model="finiteautomata/bertweet-base-sentiment-analysis")

    comments = df['comments'].tolist()
    comments = [str(comment) for comment in comments]

    # Truncate comments to a maximum sequence length of 128 tokens
    truncated_comments = [truncate_comment(
        comment, max_seq_length=20) for comment in comments]

    # Perform sentiment analysis on truncated comments
    result = specific_model(truncated_comments)

    # Mapping sentiment labels to numerical values
    sentiment_mapping = {'NEG': -1, 'NEU': 0, 'POS': 1}
    df['predicted_sentiment'] = [sentiment_mapping[item['label']]
                                 for item in result]

    # Count sentiment labels
    sentiment_counts = Counter(item['label'] for item in result)

    # Calculate sentiment percentages
    total_comments = len(result)
    sentiment_percentages = {
        sentiment_mapping[label]: f"{(count / total_comments) * 100:.2f}%" for label, count in sentiment_counts.items()}

    if debug:
        print(sentiment_percentages)

    return sentiment_percentages
