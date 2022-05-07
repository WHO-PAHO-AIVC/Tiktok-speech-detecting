import random
import urllib

from TikTokApi import TikTokApi

api = TikTokApi()

results = 10

trending = api.trending(count=results)

for tiktok in trending:
    print(tiktok['id'])

print(len(trending))

random.shuffle(trending)
i = random.randint(0, 9)
print(trending[i])

# download video
try:
    b = api.get_Video_By_DownloadURL(trending[i]['itemInfos']['video']['urls'][0])
except:
    b = api.get_Video_By_TikTok(trending[i])

open('downloaded/main.mp4', "wb").write(b)

# download cover
cover = str(trending[i]['video']['cover'])
urllib.request.urlretrieve(cover, 'downloaded/cover.jpg')

# create txt file + add info
username = str(trending[i]['author']['uniqueId'])
desc = str(trending[i]['desc'])
open("downloaded/desc./txt", "a").write(f'Credits : @{username} \n {desc}')
