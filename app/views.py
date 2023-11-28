from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

def home(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')

        if not video_url:
            return HttpResponse('Please enter a YouTube video URL.')

        try:
            # Download the YouTube video
            video = download_youtube_video(video_url)

            # Filter out non-progressive streams
            progressive_streams = [stream for stream in video.streams if stream.is_progressive or stream.audio_codec]

            context = {
                'title': video.title,
                'thumbnail': video.thumbnail_url,
                'url': video_url,
                'streams': progressive_streams,
            }

            return render(request, 'app/home.html', context)
        except Exception as e:
            return HttpResponse(f'Error: {e}')

    return render(request, 'app/home.html', {})

def download_youtube_video(video_url):
    yt = YouTube(video_url)
    return yt

