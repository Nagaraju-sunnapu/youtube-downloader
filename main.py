from pytube import YouTube

def download_video(url, output_path="."):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path=output_path)
    print(f"Downloaded: {yt.title}")

if __name__ == "__main__":
    # Replace with your desired video URL
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_video(video_url)
