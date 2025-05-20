import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=2lAe1cqCOXo"
    download_video(video_url)
