import yt_dlp

def download_video(url):
    ydl_opts = {
    'format': 'best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s',
    
    'retries': 10,              
    'fragment_retries': 10,     
    'continuedl': True,         
    'socket_timeout': 30,      
    'no_warnings': False,
}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Sedang mengunduh...")
            ydl.download([url])
            print("\nDownload selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    video_url = input("Masukkan URL YouTube: ")
    download_video(video_url)