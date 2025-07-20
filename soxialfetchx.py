print("""
oo_____oo____oooo____oooooo____oooooo____oo_____oo_
_oo___oo___oo____oo__oo____oo__oo____oo___oo___oo__
__oo_oo___oo______oo_oo_____oo_oo_____oo___oo_oo___
___ooo____oo______oo_oo_____oo_oo_____oo____ooo____
__oo_oo____oo____oo__oo____oo__oo____oo____oo_oo___
_oo___oo_____oooo____oooooo____oooooo_____oo___oo__
___________________________________________________
""")

import urllib.request

# Ask for a username to search
username = input("Enter the username to look up: ")

# List of platforms and profile URLs
platforms = {
    "Instagram": f"https://www.instagram.com/{username}/",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Facebook": f"https://facebook.com/{username}",
    "Threads": f"https://www.threads.com/{username}",
    "YouTube":f"https://www.youtube.com/@{username}",
    "VK":f"https://vk.com/{username}",
   "Telegram":f"https://t.me/{username}",
}

print(f"\nFXLooking up username '{username}'...\n")

for platform, url in platforms.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        if response.status == 200:
            print(f"FX {platform}: FOUND at {url}")
    except:
        print(f"OX {platform}: Not found.")
