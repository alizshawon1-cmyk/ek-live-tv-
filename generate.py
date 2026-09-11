import os

channels = [
    # --- Sports Channels ---
    {"name": "T Sports HD", "url": "http://jatrapala.com:8083/TSportsHD/tracks-v1a1/mono.m3u8"},

    # --- Bangladeshi Channels ---
    {"name": "Somoy TV", "url": "http://jatrapala.com:8083/SomoyTv/tracks-v1a1/mono.m3u8"},
    {"name": "Jamuna TV", "url": "http://jatrapala.com:8083/JamunaTV/tracks-v1a1/mono.m3u8"},
    {"name": "Channel 24", "url": "http://jatrapala.com:8083/channel24/tracks-v1a1/mono.m3u8"},
    {"name": "DBC News", "url": "http://jatrapala.com:8083/DBCNews/tracks-v1a1/mono.m3u8"},
    {"name": "Ekattor TV", "url": "http://jatrapala.com:8083/EkattorTV/tracks-v1a1/mono.m3u8"},
    {"name": "Independent TV", "url": "http://jatrapala.com:8083/IndependentTV/tracks-v1a1/mono.m3u8"},
    {"name": "ATN News", "url": "http://jatrapala.com:8083/ATNNews/tracks-v1a1/mono.m3u8"},
    {"name": "News 24", "url": "http://jatrapala.com:8083/News24/tracks-v1a1/mono.m3u8"},
    
    {"name": "Channel I", "url": "http://jatrapala.com:8083/ChannelI/tracks-v1a1/mono.m3u8"},
    {"name": "ATN Bangla", "url": "http://jatrapala.com:8083/ATNBangla/tracks-v1/mono.m3u8"},
    {"name": "NTV", "url": "http://jatrapala.com:8083/NTV/tracks-v1a1/mono.m3u8"},
    {"name": "RTV", "url": "http://jatrapala.com:8083/Feedget/rtv_nk_34/tracks-v1a1/mono.m3u8"},
    {"name": "Bangla Vision", "url": "http://jatrapala.com:8083/BanglaVision/tracks-v1a1/mono.m3u8"},
    {"name": "Boishakhi TV", "url": "http://jatrapala.com:8083/BoishakhiTV/tracks-v1a1/mono.m3u8"},
    {"name": "Channel 9", "url": "http://jatrapala.com:8083/Channel9/tracks-v1a1/mono.m3u8"},
    {"name": "Deepto TV", "url": "http://jatrapala.com:8083/DeeptoTV/tracks-v1a1/mono.m3u8"},
    {"name": "Bangla TV", "url": "http://jatrapala.com:8083/BanglaTV/tracks-v1a1/mono.m3u8"},
    {"name": "Maasranga TV", "url": "http://jatrapala.com:8083/Maasranga/tracks-v1a1/mono.m3u8"},
  
    {"name": "Gazi TV", "url": "http://jatrapala.com:8083/GaziTV/tracks-v1a1/mono.m3u8"},
    {"name": "Nagorik TV", "url": "http://jatrapala.com:8083/NagorikTV/tracks-v1a1/mono.m3u8"},
    
    {"name": "Ekushey TV", "url": "http://jatrapala.com:8083/ETV/tracks-v1a1/mono.m3u8"},
    {"name": "S A TV", "url": "http://jatrapala.com:8083/SATV/tracks-v1a1/mono.m3u8"},

    # --- Indian & Entertainment Channels ---
    {"name": "Enterr10 Bangla", "url": "http://jatrapala.com:8083/enterr10-bangla/tracks-v1a1/mono.m3u8"},
    {"name": "Colors Bangla", "url": "http://jatrapala.com:8083/colors-bangla/tracks-v1a1/mono.m3u8"},
    {"name": "Zee Bangla", "url": "http://jatrapala.com:8083/Feedget/ZeeBangla_8/tracks-v1a1/mono.m3u8"},
    {"name": "Star Jalsha HD", "url": "http://jatrapala.com:8083/StarJalshaHD/tracks-v1a1/mono.m3u8"},
   
    {"name": "Sony Entertainment TV HD", "url": "http://jatrapala.com:8083/Feedget/SonyEntertainmentTelevisionHD_9/tracks-v1a1/mono.m3u8"},
    {"name": "Sony Aath", "url": "http://jatrapala.com:8083/Feedget/SonyAath_7/tracks-v1a1/mono.m3u8"},
    {"name": "Star Gold", "url": "http://jatrapala.com:8083/Star-Gold/tracks-v1a1/mono.m3u8"},
    {"name": "Sony MAX", "url": "http://jatrapala.com:8083/Feedget/SonyMAX_37/tracks-v1a1/mono.m3u8"},
    {"name": "Sony PIX HD", "url": "http://jatrapala.com:8083/Feedget/SonyPIXHD/tracks-v1a1/mono.m3u8"},
    {"name": "&picture HD", "url": "http://jatrapala.com:8083/andpictureHD/tracks-v1a1/mono.m3u8"},
    {"name": "Zee Cinema HD", "url": "http://jatrapala.com:8083/Feedget/ZeeCinemaHD_38/tracks-v1a1/mono.m3u8"},
    {"name": "Star Movies", "url": "http://jatrapala.com:8083/Feedget/Star-Movies/tracks-v1a1/mono.m3u8"},
   
    # --- Kids, Info & Religious Channels ---
    {"name": "Makkah Live", "url": "http://jatrapala.com:8083/Feedget/MakkahLive_21/tracks-v1a1/mono.m3u8"},
    {"name": "Cartoon Network", "url": "http://jatrapala.com:8083/Feedget/CartoonNetwork_6/tracks-v1a1/mono.m3u8"},
    {"name": "POGO", "url": "http://jatrapala.com:8083/Feedget/POGO_5/tracks-v1a1/mono.m3u8"},
    {"name": "Animal Planet HD", "url": "http://jatrapala.com:8083/Feedget/AnimalPlanetHD_12/tracks-v1a1/mono.m3u8"},
    {"name": "Discovery", "url": "http://jatrapala.com:8083/Feedget/Discovery/tracks-v1a1/mono.m3u8"},
    {"name": "National Geographic", "url": "http://jatrapala.com:8083/Feedget/National-Geography/tracks-v1a1/mono.m3u8"},
    {"name": "TLC HD", "url": "http://jatrapala.com:8083/Feedget/TLCHD_13/tracks-v1a1/mono.m3u8"},

    {"name": "PTV Sports", "url": "http://jatrapala.com:8083/Feedget/ptv_pk/tracks-v1a1/mono.m3u8"},
    {"name": "Sony Ten 1", "url": "http://jatrapala.com:8083/SonyTen1/tracks-v1a1/mono.m3u8"},
    {"name": "Sony Ten 2", "url": "http://jatrapala.com:8083/SonyTen2/tracks-v1a1/mono.m3u8"},
    {"name": "Sony Ten 3", "url": "http://jatrapala.com:8083/SonyTen3/tracks-v1a1/mono.m3u8"},
    {"name": "Star Select HD 1", "url": "http://jatrapala.com:8083/Feedget/Star-Select-Hd-1/tracks-v1a1/mono.m3u8"},
    {"name": "Star Select HD 2", "url": "http://jatrapala.com:8083/Feedget/Star-Select-Hd-2/tracks-v1a1/mono.m3u8"},
    {"name": "Star Sports 1 HD", "url": "http://jatrapala.com:8083/StarSports1HD/tracks-v1a1/mono.m3u8"},
    {"name": "Star Sports 2 HD", "url": "http://jatrapala.com:8083/StarSports2HD/tracks-v1a1/mono.m3u8"},
    {"name": "Eurosport HD", "url": "http://jatrapala.com:8083/Feedget/EurosportHD_17/tracks-v1a1/mono.m3u8"}
]

playlist_content = "#EXTM3U\n"
for ch in channels:
    playlist_content += f"#EXTINF:-1,{ch['name']}\n{ch['url']}\n"

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)

print("Playlist generated successfully!")
