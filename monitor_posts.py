import requests
from datetime import datetime
import traceback
import time
from pprint import pprint
from yt_api_add_vid_to_pl import auth_flow, add_video_to_playlist
base_url = "https://api.pushshift.io/reddit/search/submission/?subreddit=DoomersMusic&limit=1"
start = datetime.utcnow()

def monitor_post():
    youtube = auth_flow()
    post = []
    cnt=0
    while 1:
        json = requests.get(base_url, headers={'User-Agent': "Post collector by /u/GoldArrow997"})
        json_data = json.json()
        objects = json_data['data']
        if len(objects) == 0:
            pass
        else:
            for obj in objects:
                cnt+=1
                print(cnt)
                if 1:     
                    try:
                        mystr = obj["media"]["oembed"]["html"]
                        tmp1 = mystr.split('src')[1]
                        tmp1 = tmp1[2:]
                        tmp1 = tmp1.split('?')[0]
                        print(tmp1)
                        if "www.youtube.com" in tmp1:
                            endcode = tmp1.split('/')[4]
                            print(post, endcode)
                            if endcode not in post:
                                post.append(endcode)
                                add_video_to_playlist(youtube,endcode,"PLAJaFQmLLogHL39yBFwtgSK_x5lcFjBfg")
                    except Exception as e:
                        print(e)
                else:
                    print('Epochs are the same')
        time.sleep(300)
monitor_post()