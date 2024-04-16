import re
import google.auth


def get_credentials():
    credentials, project = google.auth.default(
        scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    return {'credentials': credentials, 'project': project}

# # Example usage
# credentials_dict = get_credentials()
# print(credentials_dict)


def extract_video_id(url):
    # Regular expression pattern to match YouTube video ID
    pattern = r"(?:(?<=youtu.be/)|(?<=\?v=)|(?<=\&v=))([\w-]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
