from  pytube import YouTube

link = "https://youtu.be/XOocduQwygU"
youtube_1 = YouTube(link)

# print(youtube_1.title)
#print(youtube_1.thumbnail_url)

#videos = youtube_1.streams.all() #all format

videos = youtube_1.streams.filter(only_audio=True) #only audio

vid = list(enumerate(videos))
for i in vid:
    print(i)

print()
strm = int(input("enter : "))
videos[strm].download()
print('Successfully')


#********** Playlist **************

# from pytube import Playlist

# py = Playlist("https://www.youtube.com/playlist?list=PLjVLYmrlmjGfhrXt_Kb6liQh2yzkcaPMi")

# print(f'Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()