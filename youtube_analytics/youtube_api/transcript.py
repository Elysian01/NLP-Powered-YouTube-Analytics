from youtube_transcript_api import YouTubeTranscriptApi
from .utils import extract_video_id, get_credentials


def get_video_transcript(url, debug=False):

    # video_id = "mJ3bGvy0WAY"
    video_id = extract_video_id(url)
    if debug:
        print("Transcript Video ID: ", video_id)

    transcript, _ = generate_transcript_from_link(video_id)
    return transcript


def generate_transcript_from_link(video_id):
    # video_id = extract_video_id(link)
    try: 
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        script = ""
        for text in transcript:
            t = text["text"]
            if t != '[Music]':
                script += t + " "
        return script, len(script.split())  
    except: 
        return "", 0



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


