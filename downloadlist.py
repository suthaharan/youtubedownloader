from pytube import YouTube
from pytube import Playlist

def Downloadlist(listURL):
    playlistlink = listURL
    playlist = Playlist(playlistlink)
    for video in playlist.videos:
        print(video.watch_url)
        #print(vars(video))
        Download(video.watch_url, './nuxtrestaurant')



def Download(link, linkDir):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(linkDir)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


linklist = input("Enter the YouTube video list URL: ")
Downloadlist(linklist)