import os
import sys
import httplib2
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


    # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
    # the OAuth 2.0 information for this application, including its client_id and
    # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
    # the Google Cloud Console at
    # https://cloud.google.com/console.
    # Please ensure that you have enabled the YouTube Data API for your project.
    # For more information about using OAuth2 to access the YouTube Data API, see:
    #   https://developers.google.com/youtube/v3/guides/authentication
    # For more information about the client_secrets.json file format, see:
    #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

CLIENT_SECRETS_FILE = "client_secret.json"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"




def auth_flow():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return youtube


def add_video_to_playlist(youtube,videoID,playlistID):
    add_video_request=youtube.playlistItems().insert(
    part="snippet",
    body={
        'snippet': {
        'playlistId': playlistID, 
        'resourceId': {
            'kind': 'youtube#video',
            'videoId': videoID
            }
            #'position': 0
        }
    }
     ).execute()
if __name__ == '__main__':
    youtube = auth_flow()
    with open('all_vids_from_doomer.txt') as f:
        ids = f.read().split('\n')
    for i in ids:
        try:
            add_video_to_playlist(youtube,i,"PLAJaFQmLLogHL39yBFwtgSK_x5lcFjBfg")
            print(f'{i} has been added')
        except Exception as e:
            print(e)