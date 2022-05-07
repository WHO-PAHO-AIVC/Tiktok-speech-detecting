from TikTokApi import TikTokApi


api = TikTokApi()

for trending_video in api.trending.videos():
    video_bytes = video.bytes()
    break

with open("test.mp4", "wb") as out:
    out.write(video_bytes)
