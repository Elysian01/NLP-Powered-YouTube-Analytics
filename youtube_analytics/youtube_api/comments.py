import pandas as pd
from googleapiclient.discovery import build
from .utils import extract_video_id, get_credentials


def get_comments(url: str, no_of_comments: int, debug=False) -> pd.DataFrame:
    """
    Retrieves comments from a YouTube video and stores them in a Pandas DataFrame.

    Parameters:
        url (str): The URL of the YouTube video.
        no_of_comments (int): The number of comments to retrieve.

    Returns:
        pandas.DataFrame: A DataFrame containing the retrieved comments.

    Note:
        This function requires the `googleapiclient` library to be installed.
        It also requires a valid YouTube API key.
    """

    # video_id='bMknfKXIFA8'
    video_id = extract_video_id(url)
    if debug:
        print("Video ID: ", video_id)

    # Create YouTube API client
    # credentials, project = creds.get_credentials()

    # Create YouTube API client
    # youtube = build('youtube', 'v3', credentials=credentials)
    youtube = build('youtube', 'v3',
                    developerKey='AIzaSyA9v06e0DT_uKWuN39swpQKKKgXtO-QLVA')

    # Call the API to get comments
    comments = []
    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        order='relevance'
    ).execute()

    # Loop through each comment and append to comments list
    comment_count = 0
    while results and comment_count < no_of_comments:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            comment_count += 1

            # Break out of the loop if the desired number of comments is reached
            if comment_count == no_of_comments:
                break

        # Check if there are more comments and continue iterating
        if 'nextPageToken' in results:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                order='relevance',
                pageToken=results['nextPageToken']
            ).execute()
        else:
            break

    # Store comments in a DataFrame
    df = pd.DataFrame({'comments': comments})

    # Return the DataFrame
    return df


if __name__ == "__main__":
    # Example usage
    # Change the argument to the number of comments you want to retrieve
    url = input("Enter YouTube Video Link: ")
    df = get_comments(url, 100)
    print(df)
