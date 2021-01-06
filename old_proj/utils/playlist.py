from youtube_dl import YoutubeDL

y = YoutubeDL({'quiet':True, 'ignoreerrors':True})
f = open('playlist.txt', 'a')
for v in y.extract_info("https://www.youtube.com/playlist?list=PLI89Mvc1S1ws6TloLOnK_ecArjdr1o8ac", download=False)['entries']:
    try:
        print(v['title'], file=f)
    except:
        continue
