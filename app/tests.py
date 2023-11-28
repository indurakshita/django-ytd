from pytube import YouTube

def download(video_url):

    video = YouTube(video_url)
    for stream in video.streams.all():
        if stream.is_progressive or stream.audio_codec:
            print(stream.type)

    
data = download("https://youtu.be/AX6OrbgS8lI?si=tOh5pbkiZ6rwSDAt")

