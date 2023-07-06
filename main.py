import requests
import json
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from instabot import Bot
import os

username = "IG USERNAME"
password = "IG PASSWORD"
tellTOKEN = "TOKEN" #open https://tellonym.me and login to your tellonym and past code from GetTellToken.js to your web browser console (ctrl + shift + c) and copy and paste token to "TOKEN" in this script.
description = "post description"
delay = 10 #time every time the script has to request a new tell (given in seconds) recommends at least 10 seconds

asciart = """
   _____             _   _           _ _____      ____        _   
  / ____|           | | | |         | |_   _|    |  _ \      | |  
 | (___  _ __   ___ | |_| |_ ___  __| | | |  __ _| |_) | ___ | |_ 
  \___ \| '_ \ / _ \| __| __/ _ \/ _` | | | / _` |  _ < / _ \| __|
  ____) | |_) | (_) | |_| ||  __/ (_| |_| || (_| | |_) | (_) | |_ 
 |_____/| .__/ \___/ \__|\__\___|\__,_|_____\__, |____/ \___/ \__|
        | |                                  __/ |                
        |_|                                 |___/  

https://github.com/xanonDev/SpottedIgBot
 """
print(asciart)
os.system("del /f config")
os.system("rm -rf config")
bot = Bot()
bot.login(username=username, password=password)
url = "https://api.tellonym.me/tells?limit=1"

def divide_into_lines(text, max_length):
    lines = []
    while len(text) > max_length:
        line = text[:max_length]
        last_space = line.rfind(' ')
        if last_space == -1:
            last_space = max_length
        lines.append(line[:last_space])
        text = text[last_space:].lstrip()
    lines.append(text)
    return '\n'.join(lines)

def dirtywords(string):
    with open("wl.json", "r", encoding='utf-8') as wl:
        dirtywords = wl.read()
        dirtywords = json.loads(dirtywords)

    for word in dirtywords:
        if word.lower() in string.lower():
            censored_word = word[0] + "*" * (len(word) - 2) + word[-1]
            string = string.lower().replace(word.lower(), censored_word)
    return string

headers = {
  "Host": "api.tellonym.me",
  "Cookie":
  "_ga=GA1.2.946892631.1688123642; _gid=GA1.2.1688166150.1688123642; __cf_bm=h6ei.Yu_c2ghmZBM8gy.Ssk_AshpR8dezGDXotx8fn4-1688123643-0-ATEYj5rtbnEuSDrt13tq3NbKJV2v5C6potHIrevBfjg2GzCC0ePm5w0mqah9z4k+cw==",
  "Cache-Control": "max-age=0",
  "Sec-Ch-Ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Authorization": f"Bearer {tellTOKEN}",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
  "Accept":
  "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-User": "?1",
  "Sec-Fetch-Dest": "document",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}
log = open("lastell.txt", "r")
lasttell = log.read()
log.close()
while True:
  print("waiting for tells....")
  sleep(delay)
  print("collecting telll....")
  response = requests.get(url, headers=headers)
  j = json.loads(response.text)
  tell = j["tells"][0]["tell"]
  if tell == lasttell:
    print("the tells are the same")
  else:
    print(f"new tells: {tell}")
    with open("lastell.txt", "w") as log:
      log.write(tell)
    lasttell = tell
    tell = divide_into_lines(tell, 30)
    tell = dirtywords(tell) #remove this line if you want spotted uncensored
    image = Image.new('RGB', (1080, 1080), color='black')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=70)
    position = (0, 0)
    draw.text(position, tell, fill='white', font=font)
    image.save('tell.jpg')
    bot.upload_photo("tell.jpg", caption=description)
    os.remove("tell.jpg.REMOVE_ME")