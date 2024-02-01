import os 
import creds 
from googleapiclient.discovery import build  

def get_comments(no_of_comments):  
    # Create YouTube API client  
    # credentials, project = creds.get_credentials()

    # Create YouTube API client  
    # youtube = build('youtube', 'v3', credentials=credentials)  
    youtube = build('youtube', 'v3', developerKey='AIzaSyA9v06e0DT_uKWuN39swpQKKKgXtO-QLVA')
    
    # Set video ID  
    video_id = '6amIq_mP4xM'  
    
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
                order='relevance' , 
                pageToken=results['nextPageToken']  
            ).execute()  
        else:  
            break  
    
    # Print the comments  
    print("Number of comments: ", len(comments))  
    for i, comment in enumerate(comments):  
        print("Comment ", i+1, " : ", comment)

    return 

# Example usage
get_comments(10)  # Change the argument to the number of comments you want to retrieve
