import yt_dlp

def download_youtube(url, pilihan):
    
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'retries': 10,              
        'fragment_retries': 10,    
        'continuedl': True,         
        'socket_timeout': 30,      
    }

    if pilihan == '1':
        print("\n--- Menyiapkan Download MP4 (Video) ---")
        ydl_opts['format'] = 'best[ext=mp4]/best'
    
    elif pilihan == '2':
        print("\n--- Menyiapkan Download Audio (M4A) ---")
        # Mengambil m4a (audio saja) karena ini format paling aman tanpa FFmpeg
        ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio/best'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Sedang memproses... Tunggu sebentar.")
            ydl.download([url])
            print("\nBerhasil! File sudah tersimpan di folder.")
    except Exception as e:
        print(f"\nWaduh, ada error: {e}")

if __name__ == "__main__":
    print("=== YOUTUBE DOWNLOADER ===")
    link = input("Masukkan URL YouTube: ")
    print("\nMau download format apa?")
    print("1. Video (MP4)")
    print("2. Audio (M4A)")
    opsi = input("Pilih (1/2): ")

    if opsi in ['1', '2']:
        download_youtube(link, opsi)
    else:
        print("Pilihan salah!")