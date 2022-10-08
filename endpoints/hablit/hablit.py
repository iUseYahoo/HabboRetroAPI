import json
from bs4 import BeautifulSoup
import requests

def hablit_search(username):
    url = "https://hablit.net/profile/{}".format(username)
    # This expires after a certain amount of time or uses I belive, Or maybe even if the wrong IP is using it, so try your own cookie.
    r = requests.get(url, cookies={'hablit_session': 'eyJpdiI6IkYzcmlqY1BSRzlHWC82WTNMSVVQU2c9PSIsInZhbHVlIjoiYVoyVjVDTTZPNkhSSEZ6VVdqYmUzTTVlUG9PYkdwSDFTSS80Z2J1RFR0MzFtTW5SOVZBY0JqMCtpSGk5V1hzL2hieVIrN20wZ2JnamFKN3VONWlHRkJNV3ZMVGh2cWJITFBmYkR5K2piVy9DUTc2QUhaMStMb2c1RDVuU2xuQW8iLCJtYWMiOiI3Y2I1ZDBhMDIwZmQxNDhhZjY0ODk0N2RhMTlkYzYxNTlhYWY5NTYzY2QyNWUzZjc1ZTMwMDU1NzljZDllZDM3IiwidGFnIjoiIn0%3D'})
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


    # this is used for debugging
    # raw_data = "Avatar: {}\nMotto: {}\nCoins: {}\nDuckets: {}\nDiamonds: {}".format(avatar, motto, coins, duckets, diamonds)
    # print(raw_data)
    
    # display unicode for motto
    motto = motto.encode('ascii', 'xmlcharrefreplace').decode('utf-8')

    return json.dumps({
        "avatar": avatar.strip('\r\n').strip("\r\n "),
        "motto": motto.strip('\r\n').strip("\r\n "),
        "credits": coins.strip('\r\n').strip("\r\n "),
        "duckets": duckets.strip('\r\n').strip("\r\n "),
        "diamonds": diamonds.strip('\r\n').strip("\r\n ")
    })
