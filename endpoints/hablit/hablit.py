import json
from bs4 import BeautifulSoup
import requests

def hablit_search(username):
    url = "https://hablit.net/profile/{}".format(username)
    
    # Change hablit_sessions cookie value to your own, From testing it seems it stopped working aftering a couple hours.
    r = requests.get(url, cookies={'hablit_session': 'eyJpdiI6Ik1TTFRhVUVyelN2elVISzE4Y0ZkV3c9PSIsInZhbHVlIjoiTklLVFhDaTZQNmxPZUJrT24wc28xd0tWN3BzeHJCVEpRTlg5Z0RDNEtBSFdrZXZIWjhkQkhxeENSSGdpb3VMNE54ZWxnbjJLNUhGRjlCbUpmMjRsK2VZczh5Umx3VkpYYXl4R2t5ckpxb0VHbDhOdlBQQUo1dlcyTmpSblF1SnQiLCJtYWMiOiJkYTY2ZmFkN2UwYWY1ZjRhMjBmZTQyNjY2MWVjYTcxM2MxNWRhMjIxYzY3ZDNkYzBmNWExODJjZDUwYzk2ZjRjIiwidGFnIjoiIn0%3D'})
    soup = BeautifulSoup(r.text, "html.parser")

    motto = soup.find("h4", {"class": "text-lg font-semibold italic"})
    if motto:
        motto = motto.text
    # else:
    #     motto = "Motto is not set on webpage."
    

    avatar = soup.find("div", {"class": "col-span-3 md:col-span-1 h-[150px] lg:h-[220px] profile-bg rounded-lg relative flex gap-x-2 items-center text-white overflow-hidden"})
    if avatar:
        avatar = avatar.find("img")["src"]
    # else:
    #     avatar = "Avatar is not set on webpage."


    coins = soup.find("h4", {"class": "text-[#b16d18] font-semibold text-2xl"})
    if coins:
        coins = coins.text
    # else:
    #     coins = "Coins are not set on webpage."


    duckets = soup.find("h4", {"class": "text-[#812378] font-semibold text-2xl"})
    print("ducketttttttttttssssssssss ======= ", duckets)
    if duckets:
        duckets = duckets.text
    # else:
    #     duckets = "Duckets are not set on webpage."


    diamonds = soup.find("h4", {"class": "text-[#146867] font-semibold text-2xl"})
    if diamonds:
        diamonds = diamonds.text
    # else:
    #     diamonds = "Diamonds are not set on webpage."


    # used for testing during development
    # raw_data = "Avatar: {}\nMotto: {}\nCoins: {}\nDuckets: {}\nDiamonds: {}".format(avatar, motto, coins, duckets, diamonds)
    # print(raw_data)
    
    return json.dumps({
        "avatar": avatar.strip('\r\n').strip("\r\n "),
        "motto": motto.strip('\r\n').strip("\r\n "),
        "credits": coins.strip('\r\n').strip("\r\n "),
        "duckets": duckets.strip('\r\n').strip("\r\n "),
        "diamonds": diamonds.strip('\r\n').strip("\r\n ")
    })
