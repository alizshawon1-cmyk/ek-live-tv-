import os

channels = [
    # --- Sports Channels ---
    {"name": "T Sports HD", "url": "http://jatrapala.com:8083/TSportsHD/tracks-v1a1/mono.m3u8?token=43285aaec58cca2e92ae1fee2ecd03589d8e131d-1cb83c4234ea04f3e3c42ab831c6871c-1789077371-1789066571"},

    # --- Bangladeshi Channels ---
    {"name": "Somoy TV", "url": "http://jatrapala.com:8083/SomoyTv/tracks-v1a1/mono.m3u8?token=4c3b4eff3f5e8256ed4c2f9452e47ed54b361b89-ba8565a9916356929fd3b2eaaabfa4bd-1789078320-1789067520"},
    {"name": "Jamuna TV", "url": "http://jatrapala.com:8083/JamunaTV/tracks-v1a1/mono.m3u8?token=eecac34a2bca9da8bb9418f0aaca1d6ff3b4e802-e2dc10d99ea3451cae2e795596590f9c-1789077989-1789067189"},
    {"name": "Channel 24", "url": "http://jatrapala.com:8083/channel24/tracks-v1a1/mono.m3u8?token=7166799a7c05250ca475996d45149252fdd0b72b-da539b216ca38a1357d1272bd4e308a2-1789077831-1789067031"},
    {"name": "DBC News", "url": "http://jatrapala.com:8083/DBCNews/tracks-v1a1/mono.m3u8?token=347ab76e85c1e837c32a2f8077e8097bae78af86-3d53f390a7219c4dea46238e093f9afe-1789077843-1789067043"},
    {"name": "Ekattor TV", "url": "http://jatrapala.com:8083/EkattorTV/tracks-v1a1/mono.m3u8?token=c47fddb9633d574fc0a4d66666b4ee936025db12-7a5d7df885e559d6524fc89de94fee28-1789077855-1789067055"},
    {"name": "Independent TV", "url": "http://jatrapala.com:8083/IndependentTV/tracks-v1a1/mono.m3u8?token=efa777acae35db52cbb0edddbdc0e8818bd2d374-bed89b76ddfd901ca98a20b892df19ef-1789077868-1789067068"},
    {"name": "ATN News", "url": "http://jatrapala.com:8083/ATNNews/tracks-v1a1/mono.m3u8?token=f1a56ee50611a72aecf7ff2aa9b306928e0a0a28-43b8560bd39aeb04d88a9d4d076ef328-1789077920-1789067120"},
    {"name": "News 24", "url": "http://jatrapala.com:8083/News24/tracks-v1a1/mono.m3u8?token=45407dac4b808b33f657210c6e5822c5e816f227-90374a7400cfaa6383491afffde7810a-1789077880-1789067080"},
    
    {"name": "Channel I", "url": "http://jatrapala.com:8083/ChannelI/tracks-v1a1/mono.m3u8?token=7a58068b65fcc9a1c9e9ac03cacb262da6a9aef1-4a185be75478157f4d87e18226442ee6-1789077896-1789067096"},
    {"name": "ATN Bangla", "url": "http://jatrapala.com:8083/ATNBangla/tracks-v1/mono.m3u8?token=004490d9fd60f79b7e7314c2cee3316a97fe8fed-253fc1dd793a1b45a2c9b3aba3b145cf-1789077909-1789067109"},
    {"name": "NTV", "url": "http://jatrapala.com:8083/NTV/tracks-v1a1/mono.m3u8?token=3d1de55321e4d7f4f8632066452ffb8fdca27b61-ba599e10f7081f23ea4146fff963b871-1789078016-1789067216"},
    {"name": "RTV", "url": "http://jatrapala.com:8083/Feedget/rtv_nk_34/tracks-v1a1/mono.m3u8?token=50201454d99fd4ee947e6731e0eb9c769c470a58-dbf2e788f90b603ec51dd5242ad23ff6-1789078027-1789067227"},
    {"name": "Bangla Vision", "url": "http://jatrapala.com:8083/BanglaVision/tracks-v1a1/mono.m3u8?token=6760331414858b2208a76a7141924785975cb44f-468f9b0a8ce47ba346b3507f519283c3-1789077943-1789067143"},
    {"name": "Boishakhi TV", "url": "http://jatrapala.com:8083/BoishakhiTV/tracks-v1a1/mono.m3u8?token=07d5446b911e699855039ef36637d7f36dff7b6d-7ef2c4ed084402f8265dc65ec56c431d-1789077954-1789067154"},
    {"name": "Channel 9", "url": "http://jatrapala.com:8083/Channel9/tracks-v1a1/mono.m3u8?token=f71e74f54a857e9c708c07d24bce541288de42a2-477b29a58616c5993cb8a7c0927c962c-1789077964-1789067164"},
    {"name": "Deepto TV", "url": "http://jatrapala.com:8083/DeeptoTV/tracks-v1a1/mono.m3u8?token=3e68e795555668b57cc94bef95d2ee1d0cef2d94-7a54e89c5328fa60674de2f7386fce8b-1789077978-1789067178"},
    {"name": "Bangla TV", "url": "http://jatrapala.com:8083/BanglaTV/tracks-v1a1/mono.m3u8?token=789b61008877973e30f769bbfd9ce4db3a18b9d8-7b930e17211147e1f1a4223c2b763a82-1789077931-1789067131"},
    {"name": "Maasranga TV", "url": "http://jatrapala.com:8083/Maasranga/tracks-v1a1/mono.m3u8?token=e5e79192b1dabf0c85232f1692a913a83096840b-56da3a4344153b80614c8531c0dffb4b-1789078002-1789067202"},
  
    {"name": "Gazi TV", "url": "http://jatrapala.com:8083/GaziTV/tracks-v1a1/mono.m3u8?token=5c7debcbbbd1717c470d797270ed9fcf8e2a2884-3f2c0ab3142cfa53784d83d58877ab87-1789077804-1789067004"},
    {"name": "Nagorik TV", "url": "http://jatrapala.com:8083/NagorikTV/tracks-v1a1/mono.m3u8?token=1e47454431c923942f19228bbdf9e635b998077a-b62d96cd9d3c35745d9f813737046d37-1789077819-1789067019"},
    
    {"name": "Ekushey TV", "url": "http://jatrapala.com:8083/ETV/tracks-v1a1/mono.m3u8?token=ab2f7d0181b63ef61ed1b9233dcfec587eb3714d-512e24c94f539abe812a2489f8e9917c-1789078040-1789067240"},
    {"name": "S A TV", "url": "http://jatrapala.com:8083/SATV/tracks-v1a1/mono.m3u8?token=e51da435a851a8fa08706216dc2f4d26afb70c31-8ac969b712d5f412ff713e6f13a00261-1789078051-1789067251"},

    # --- Indian & Entertainment Channels ---
    {"name": "Enterr10 Bangla", "url": "http://jatrapala.com:8083/enterr10-bangla/tracks-v1a1/mono.m3u8?token=cb5e5fde2873a4f4e2194b7fe6468de7d615e7e3-59928282e13082499350143c418366bf-1789078063-1789067263"},
    {"name": "Colors Bangla", "url": "http://jatrapala.com:8083/colors-bangla/tracks-v1a1/mono.m3u8?token=f1beb452f6d8b46fae622fb94abc72c7f6ce7405-12355b7aeaefa5fa8e61584379f9af12-1789078076-1789067276"},
    {"name": "Zee Bangla", "url": "http://jatrapala.com:8083/Feedget/ZeeBangla_8/tracks-v1a1/mono.m3u8?token=3ff3177f127df3a10f00c45519967cfc4b54b6b2-08ffe92665ae04c0d34bec71e5d00670-1789078088-1789067288"},
    {"name": "Star Jalsha HD", "url": "http://jatrapala.com:8083/StarJalshaHD/tracks-v1a1/mono.m3u8?token=845f07444b2495f5b67d5190bfca99dea02cc6bf-b95a1532e87f39b860d659c4fa798fd9-1789078101-1789067301"},
   
    {"name": "Sony Entertainment TV HD", "url": "http://jatrapala.com:8083/Feedget/SonyEntertainmentTelevisionHD_9/tracks-v1a1/mono.m3u8?token=818bfbea8a68da098dab90890042ac40f1403372-ec04664f0ca58b95f717418173a2225b-1789078142-1789067342"},
    {"name": "Sony Aath", "url": "http://jatrapala.com:8083/Feedget/SonyAath_7/tracks-v1a1/mono.m3u8?token=722b66a3eee4d6b96062eec7470e9448517380fa-93156e7c584ca0eb21426efaeeb0267a-1789078159-1789067359"},
    {"name": "Star Gold", "url": "http://jatrapala.com:8083/Star-Gold/tracks-v1a1/mono.m3u8?token=85cde29b4ffbad04fbc2c3c0d524d2cc74f81b2d-4990dcc99d0d5f38f35f171234fa43d6-1789078129-1789067329"},
    {"name": "Sony MAX", "url": "http://jatrapala.com:8083/Feedget/SonyMAX_37/tracks-v1a1/mono.m3u8?token=8c54060b7d55b2e971aea00cc1d37fb5ad581cd7-9d845621fc54a0e101e3181baa932579-1789078171-1789067371"},
    {"name": "Sony PIX HD", "url": "http://jatrapala.com:8083/Feedget/SonyPIXHD/tracks-v1a1/mono.m3u8?token=80d31452eb4e444067a18dc84dac59e66a7d1efb-784e980f2f5b70e67ee83135be800984-1789078189-1789067389"},
    {"name": "&picture HD", "url": "http://jatrapala.com:8083/andpictureHD/tracks-v1a1/mono.m3u8?token=19b0d85b041ec8688962187aa9d18133956f2cce-3c0d42b8c63dce44114055573b64e329-1789078201-1789067401"},
    {"name": "Zee Cinema HD", "url": "http://jatrapala.com:8083/Feedget/ZeeCinemaHD_38/tracks-v1a1/mono.m3u8?token=0f4fe5867d08f65f6fca432719e684c66f669367-d9ab824757dc541a2af2cb651b23f57a-1789078213-1789067413"},
    {"name": "Star Movies", "url": "http://jatrapala.com:8083/Feedget/Star-Movies/tracks-v1a1/mono.m3u8?token=d3162dc3d81206dc23fd6fb715c05e23d25b5e20-2f40294eaa6c88a451975397819e7b7f-1789078114-1789067314"},
   
    # --- Kids, Info & Religious Channels ---
    {"name": "Makkah Live", "url": "http://jatrapala.com:8083/Feedget/MakkahLive_21/tracks-v1a1/mono.m3u8?token=02c77b0fee9b2d63f287b256ad37b0b5d0634b2f-743c3db990b807b077c68b94e8687eb9-1789078227-1789067427"},
    {"name": "Cartoon Network", "url": "http://jatrapala.com:8083/Feedget/CartoonNetwork_6/tracks-v1a1/mono.m3u8?token=0fdddbcd817c6353d5851e0d5ede262c14d02498-d0e852c151e874038e83652860ef0a9d-1789078238-1789067438"},
    {"name": "POGO", "url": "http://jatrapala.com:8083/Feedget/POGO_5/tracks-v1a1/mono.m3u8?token=8ae06502da5ebb0ef49eb90808adcd2f5477393d-df9cb1a1a3affecdc7355126175ee1c1-1789078253-1789067453"},
    {"name": "Animal Planet HD", "url": "http://jatrapala.com:8083/Feedget/AnimalPlanetHD_12/tracks-v1a1/mono.m3u8?token=126939ffe75b284d20a5e11627f96074026abb37-77b2100b4740dbc484c26117cb81fe53-1789078264-1789067464"},
    {"name": "Discovery", "url": "http://jatrapala.com:8083/Feedget/Discovery/tracks-v1a1/mono.m3u8?token=cd5c19f53772179d646ac16f5b4b31dec8a25b29-381a8a781c1107cbf5b1a27fce5fab7b-1789078277-1789067477"},
    {"name": "National Geographic", "url": "http://jatrapala.com:8083/Feedget/National-Geography/tracks-v1a1/mono.m3u8?token=e9ca6c32358cf9d4bddd5d77c941f101d8cb0f6b-987b06efddc700dd3bfbb54047000974-1789078289-1789067489"},
    {"name": "TLC HD", "url": "http://jatrapala.com:8083/Feedget/TLCHD_13/tracks-v1a1/mono.m3u8?token=4804ddf6e58cd57918781fe067dea8fc1051cd4c-7b18a7756d08dd9b71c3313bab0dd560-1789078305-1789067505"},

    {"name": "PTV Sports", "url": "http://jatrapala.com:8083/Feedget/ptv_pk/tracks-v1a1/mono.m3u8?token=9dadbd80004c7dacbbf7474245d989036273651c-8826e77d75e6e58e0e2ff3731406dbf6-1789077408-1789066608"},
    {"name": "Sony Ten 1", "url": "http://jatrapala.com:8083/SonyTen1/tracks-v1a1/mono.m3u8?token=d45d2f5fbf384d284928ee72dc3f9595c4fd34cf-1a71e8963abe8b1a66adf240c92f39a7-1789077363-1789066563"},
    {"name": "Sony Ten 2", "url": "http://jatrapala.com:8083/SonyTen2/tracks-v1a1/mono.m3u8?token=f8e397a701ea5e73f2576997bd73165a9800d917-b67f454c68f58271aa9fb06ff96bfaff-1789077706-1789066906"},
    {"name": "Sony Ten 3", "url": "http://jatrapala.com:8083/SonyTen3/tracks-v1a1/mono.m3u8?token=0d545c69359b444c5c1faa1efe1ae224cd7e2905-8a97b258b1a1f6db41f0cef80829857a-1789077392-1789066592"},
    {"name": "Star Select HD 1", "url": "http://jatrapala.com:8083/Feedget/Star-Select-Hd-1/tracks-v1a1/mono.m3u8?token=ee3a7822d24b3e0509f29389ce2de3d01350a8cd-e6cf15aa65c4c35219dea1c7aaac69a4-1789077395-1789066595"},
    {"name": "Star Select HD 2", "url": "http://jatrapala.com:8083/Feedget/Star-Select-Hd-2/tracks-v1a1/mono.m3u8?token=13de8057dfe63ca427c6ae50f2af713b6636e05a-2026b667fd2bde714869475545a292aa-1789077397-1789066597"},
    {"name": "Star Sports 1 HD", "url": "http://jatrapala.com:8083/StarSports1HD/tracks-v1a1/mono.m3u8?token=b0645456330af9a8a9db451b6ee05c4e73f2c9bd-0e03416e40689c7fd91288cbacb14b3c-1789077400-1789066600"},
    {"name": "Star Sports 2 HD", "url": "http://jatrapala.com:8083/StarSports2HD/tracks-v1a1/mono.m3u8?token=c8e5389f6d2cebbebc6d852c6b0a99bf664d0bd8-28e7841067f9156482d5e54c582361e0-1789077402-1789066602"},
    {"name": "Eurosport HD", "url": "http://jatrapala.com:8083/Feedget/EurosportHD_17/tracks-v1a1/mono.m3u8?token=fdc291cec6b33845495f0c8bde049c4c12c8f618-9d0a72dec4d6418445b39b01d2f90082-1789078338-1789067538"}
]

playlist_content = "#EXTM3U\n"
for ch in channels:
    playlist_content += f"#EXTINF:-1,{ch['name']}\n{ch['url']}\n"

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist_content)

print("Playlist generated successfully!")
