from __future__ import unicode_literals

import os

import youtube_dl

url = 'https://www.youtube.com/watch?v=tD0K9cUd2ys'
output = 'mp4'
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    mp3 = ydl.download([url])

for filename in os.listdir("."):

    if filename[-3:] == 'mp3':
        os.rename(filename,'sample.mp3')

