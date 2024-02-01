import google.auth

def get_credentials():
    credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])  
    return {'credentials': credentials, 'project': project}

# # Example usage
# credentials_dict = get_credentials()
# print(credentials_dict)
