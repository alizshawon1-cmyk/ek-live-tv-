import re
import requests

# সকল চ্যানেলের সম্মিলিত তালিকা (সবগুলোর সাথেই page_url দেওয়া হয়েছে যাতে অটো-ফেচ হতে পারে)
channels_info = [
    # Jatrapala চ্যানেলসমূহ
    {"name": "T Sports HD", "page_url": "http://jatrapala.com/live-tv/tsports.html"},
    {"name": "Somoy TV", "page_url": "http://jatrapala.com/live-tv/somoy-tv.html"},
    {"name": "Jamuna TV", "page_url": "http://jatrapala.com/live-tv/jamunatv.html"},
    {"name": "Channel 24", "page_url": "http://jatrapala.com/live-tv/channel-24.html"},
    {"name": "DBC News", "page_url": "http://jatrapala.com/live-tv/dbcnews.html"},
    {"name": "Ekattor TV", "page_url": "http://jatrapala.com/live-tv/ekattor-tv.html"},
    {"name": "Independent TV", "page_url": "http://jatrapala.com/live-tv/independenttv.html"},
    {"name": "ATN News", "page_url": "http://jatrapala.com/live-tv/atnnews.html"},
    {"name": "News 24", "page_url": "http://jatrapala.com/live-tv/news-24.html"},
    {"name": "Channel I", "page_url": "http://jatrapala.com/live-tv/channel-i.html"},
    {"name": "Bangla Vision", "page_url": "http://jatrapala.com/live-tv/banglavision.html"},
    {"name": "ATN Bangla", "page_url": "http://jatrapala.com/live-tv/atn-bangla.html"},
    {"name": "NTV", "page_url": "http://jatrapala.com/live-tv/ntv.html"},
    {"name": "RTV", "page_url": "http://jatrapala.com/live-tv/rtv.html"},
    {"name": "Boishakhi TV", "page_url": "http://jatrapala.com/live-tv/boishakhitv.html"},
    {"name": "Ekushey TV", "page_url": "http://jatrapala.com/live-tv/etv.html"},
    {"name": "Bangla TV", "page_url": "http://jatrapala.com/live-tv/bangla-tv.html"},
    {"name": "Deepto TV", "page_url": "http://jatrapala.com/live-tv/deepto-tv.html"},
    {"name": "Nagorik TV", "page_url": "http://jatrapala.com/live-tv/nagorik-tv.html"},
    {"name": "Maasranga TV", "page_url": "http://jatrapala.com/live-tv/maasranga.html"},
    {"name": "SA TV", "page_url": "http://jatrapala.com/live-tv/satv.html"},
    {"name": "Gazi TV", "page_url": "http://jatrapala.com/live-tv/gazi-tv.html"},
    
    # লোকাল সার্ভার চ্যানেলসমূহ (play.php পেজের লিংক)
    {"name": "Duronto TV", "page_url": "http://172.19.178.180/play.php?id=3668684838"},
    {"name": "Ruposhi Bangla", "page_url": "http://172.19.178.180/play.php?id=6416654447"},
    {"name": "Movie Bangla TV", "page_url": "http://172.19.178.180/play.php?id=9799573742"},
    
    # Jatrapala চ্যানেলসমূহ
    {"name": "Channel 9", "page_url": "http://jatrapala.com/live-tv/channel-9.html"},
    {"name": "Colors Bangla", "page_url": "http://jatrapala.com/live-tv/colors-bangla.html"},
    {"name": "Zee Bangla", "page_url": "http://jatrapala.com/live-tv/zee-bangla.html"},
    
    # লোকাল সার্ভার চ্যানেলসমূহ
    {"name": "Jalsha Movies HD", "page_url": "http://172.19.178.180/play.php?id=3372594744"},
    {"name": "Zee Bangla Cinema", "page_url": "http://172.19.178.180/play.php?id=8012094529"},
    {"name": "Colors Bangla Cinema", "page_url": "http://172.19.178.180/play.php?id=9872082878"},
    
    # Jatrapala চ্যানেলসমূহ
    {"name": "Enterr10 Bangla", "page_url": "http://jatrapala.com/live-tv/enterr10.html"},
    {"name": "Star Jalsha HD", "page_url": "http://jatrapala.com/live-tv/star-jalsha.html"},
    {"name": "Star Gold", "page_url": "http://jatrapala.com/live-tv/star-gold.html"},
    {"name": "Sony MAX", "page_url": "http://jatrapala.com/live-tv/sony-max.html"},
    {"name": "Zee Cinema HD", "page_url": "http://jatrapala.com/live-tv/zee-cinema.html"},
    {"name": "Star Movies", "page_url": "http://jatrapala.com/live-tv/star-movies.html"},
    {"name": "Sony PIX HD", "page_url": "http://jatrapala.com/live-tv/sony-pix.html"},
    {"name": "Sony Entertainment TV HD", "page_url": "http://jatrapala.com/live-tv/sony-tv.html"},
    {"name": "Makkah Live", "page_url": "http://jatrapala.com/live-tv/makkah-live.html"},
    {"name": "POGO", "page_url": "http://jatrapala.com/live-tv/pogo.html"},
    {"name": "Cartoon Network", "page_url": "http://jatrapala.com/live-tv/cartoon-network.html"},
    {"name": "Animal Planet HD", "page_url": "http://jatrapala.com/live-tv/animal-planet.html"},
    {"name": "Discovery", "page_url": "http://jatrapala.com/live-tv/discovery.html"},
    {"name": "National Geographic", "page_url": "http://jatrapala.com/live-tv/national-geographic.html"},
    {"name": "TLC HD", "page_url": "http://jatrapala.com/live-tv/tlc.html"},
    {"name": "PTV Sports", "page_url": "http://jatrapala.com/live-tv/ptv.html"},
    {"name": "Eurosport HD", "page_url": "http://jatrapala.com/live-tv/eurosport.html"},
    {"name": "Sony Ten 1", "page_url": "http://jatrapala.com/live-tv/sony-ten-1.html"},
    {"name": "Sony Ten 2", "page_url": "http://jatrapala.com/live-tv/sony-ten-2.html"},
    {"name": "Sony Ten 3", "page_url": "http://jatrapala.com/live-tv/sony-ten-3.html"},
    {"name": "Star Sports Select HD 1", "page_url": "http://jatrapala.com/live-tv/star-sports-selected-1.html"},
    {"name": "Star Sports Select HD 2", "page_url": "http://jatrapala.com/live-tv/star-sports-selected-2.html"},
    {"name": "Star Sports 1 HD", "page_url": "http://jatrapala.com/live-tv/star-sports-1.html"},
    {"name": "Star Sports 2 HD", "page_url": "http://jatrapala.com/live-tv/star-sports-2.html"},
    
    # লোকাল সার্ভার চ্যানেলসমূহ
    {"name": "Star Sports 3", "page_url": "http://172.19.178.180/play.php?id=1717823063"},
    
    # Jatrapala চ্যানেলসমূহ
    {"name": "Ten Cricket", "page_url": "http://jatrapala.com/live-tv/ten-cricket.html"},
    
    # লোকাল সার্ভার চ্যানেলসমূহ
    {"name": "A Sports", "page_url": "http://172.19.178.180/play.php?id=4960725297"},
    {"name": "Ten Cricket (Local)", "page_url": "http://172.19.178.180/play.php?id=5079856223"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

playlist_content = "#EXTM3U\n"
success_count = 0

for ch in channels_info:
    try:
        response = requests.get(ch["page_url"], headers=headers, timeout=10)
        if response.status_code == 200:
            # রেগুলার এক্সপ্রেশন দিয়ে .m3u8 বা fmp4 লিংক খোঁজা
            match = re.search(r'(http[^\s\'\"<>]+?\.m3u8[^\s\'\"<>]*)', response.text)
            if match:
                stream_url = match.group(1).replace(" ?token=", "?token=")
                playlist_content += f"#EXTINF:-1,{ch['name']}\n{stream_url}\n"
                print(f"[Success] Fetched token for {ch['name']}")
                success_count += 1
            else:
                print(f"[Warning] Stream link not found for {ch['name']}")
        else:
            print(f"[Error] Page not found for {ch['name']}")
    except Exception as e:
        print(f"[Error] Failed for {ch['name']}: {e}")

# প্লেলিস্ট ফাইল সেভ করা
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)

print(f"\nDone! Successfully auto-fetched {success_count} channels.")