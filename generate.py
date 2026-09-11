channels = [
    {"name": "Channel 24", "url": "http://jatrapala.com:8083/channel24/tracks-v1a1/mono.m3u8?token=bf0326a03b8ff325bd4a686553f07242bfd8b6d9-4742826ad28b2c5bd9d174cb3ec059a6-1789119450-1789108650"},
    {"name": "DBC News", "url": "http://jatrapala.com:8083/DBCNews/tracks-v1a1/mono.m3u8?token=2f43ed31b70401d043e7e5017c850c88616b821b-23de513b26d08b98e408ef7cd3815fdc-1789119464-1789108664"},
    {"name": "Ekattor TV", "url": "http://jatrapala.com:8083/EkattorTV/tracks-v1a1/mono.m3u8?token=7248008be480da976f5d8b4f560988b76bca21c9-55a838bbd3d22c395c517b4b5cea55a0-1789119480-1789108680"},
    {"name": "Independent TV", "url": "http://jatrapala.com:8083/IndependentTV/tracks-v1a1/mono.m3u8?token=d8030a8ccf87fc0fff248ecb97d05c52abae78f3-5f7e6a56568accf62fe6e15bc9ee572a-1789119491-1789108691"},
    {"name": "News 24", "url": "http://jatrapala.com:8083/News24/tracks-v1a1/mono.m3u8?token=f08b48fb24902aa4ac748d8de0ba93550a1ef648-4e390d9c1fcfe27bf8ef541063856cec-1789119505-1789108705"},
    {"name": "Channel I", "url": "http://jatrapala.com:8083/ChannelI/tracks-v1a1/mono.m3u8?token=f3d65919b36f0790da1038c5a78b1032222a6555-c920f976c1f0fca1371d7d07e448802e-1789119533-1789108733"},
    {"name": "Deepto TV", "url": "http://jatrapala.com:8083/DeeptoTV/tracks-v1a1/mono.m3u8?token=fa44b61ff208e79b20289ca8071fb4738cbe2cab-3bd4663bee58ff5ddb09dc547a1f1a52-1789119548-1789108748"}
]

playlist_content = "#EXTM3U\n"
for ch in channels:
    playlist_content += f"#EXTINF:-1,{ch['name']}\n{ch['url']}\n"

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)

print("Playlist updated successfully with fresh tokens!")