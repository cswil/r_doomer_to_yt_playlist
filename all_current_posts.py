import requests
from datetime import datetime
import traceback
import time
from pprint import pprint
base_url = "https://api.pushshift.io/reddit/search/submission/?subreddit=DoomersMusic&limit=1000&sort=desc&before="
start = datetime.utcnow()
def get_posts():
    cnt = 0
    handle = open('out','w')
    prev_epoch = int(start.timestamp())
    while 1:
        new_url = base_url + str(prev_epoch)
        json = requests.get(new_url, headers={'User-Agent': "Post collector by /u/GoldArrow997"})
        time.sleep(1)
        json_data= json.json()
        if 'data' not in json_data:
            break
        objects = json_data['data']
        if len(objects) == 0:
            break
        for object in objects:
            prev_epoch = object['created_utc'] - 1
            cnt += 1
            try:
                mystr = object["media"]["oembed"]["html"]
                tmp1 = mystr.split('src')[1]
                tmp1 = tmp1[2:]
                tmp1 = tmp1.split('?')[0]
                print(tmp1)
                if "www.youtube.com" in tmp1:
                    endcode = tmp1.split('/')[4]
                    handle.write(f"https://www.youtube.com/watch?v={endcode}" + "\n")
            except:
                print('No media tag')
            

    print(f'We got {cnt} posts')
get_posts()