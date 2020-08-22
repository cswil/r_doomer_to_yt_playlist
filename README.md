# Explanation of each file

### all_current_posts.py

This fetches every youtube video id posted to the subreddit, can easily be edited to get just the links

### init_playlist.py

I attempted to use this to create a playlist with every song but its capped at 50 videos, could be useful to someone i guess

### monitor_posts.py

Check when a new vid is uploaded and then using that add it to playlist

### yt_api_add_to_pl.py

The functions that upload the videos to the playlist, you need to get a client_secret.json file from the yt v3 api to run this.
