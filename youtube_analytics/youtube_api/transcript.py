# from googleapiclient.discovery import build
# from .utils import extract_video_id, get_credentials


# def get_video_transcript(url, debug=False):

#     # video_id = "mJ3bGvy0WAY"
#     video_id = extract_video_id(url)
#     if debug:
#         print("Transcript Video ID: ", video_id)

#     # Create YouTube API client
#     youtube = build('youtube', 'v3',
#                     developerKey='AIzaSyA9v06e0DT_uKWuN39swpQKKKgXtO-QLVA')

#     # Call the API to get video details
#     video_response = youtube.videos().list(
#         part='snippet,contentDetails',
#         id=video_id
#     ).execute()

#     # Extract transcript from video details
#     if 'items' in video_response:
#         video_info = video_response['items'][0]

#         # Check if captions are available for the video
#         if 'contentDetails' in video_info and 'caption' in video_info['contentDetails']:
#             transcript_url = video_info['contentDetails']['caption']

#             # Fetch the transcript using the transcript URL
#             transcript_response = youtube.captions().list(
#                 part='snippet',
#                 videoId=video_id
#             ).execute()

#             # Check if 'items' is not empty and 'text' key is present in the response
#             if 'items' in transcript_response and transcript_response['items']:
#                 snippet = transcript_response['items'][0].get('snippet', {})
#                 transcript_text = snippet.get('text', '')

#                 if transcript_text:
#                     return transcript_text

#     return None


# # Example usage
# if __name__ == "__main__":

#     # video_id = 'mJ3bGvy0WAY'
#     url = input("Enter YouTube Video Link: ")
#     transcript = get_video_transcript(url)

#     if transcript:
#         print("Video Transcript:")
#         print(transcript)
#     else:
#         print("Transcript not available for this video.")


from youtube_transcript_api import YouTubeTranscriptApi
from .utils import extract_video_id, get_credentials


def get_video_transcript(url, debug=False):

    # video_id = "mJ3bGvy0WAY"
    video_id = extract_video_id(url)
    if debug:
        print("Transcript Video ID: ", video_id)

    transcript, _ = generate_transcript_from_link(url)
    return transcript


def generate_transcript_from_link(link):
    video_id = extract_video_id(link)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    script = ""
    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
    return script, len(script.split())



# Example usage
if __name__ == "__main__":

    # video_id = 'mJ3bGvy0WAY'
    url = input("Enter YouTube Video Link: ")
    transcript = get_video_transcript(url)

    if transcript:
        print("Video Transcript:")
        print(transcript)
    else:
        print("Transcript not available for this video.")


