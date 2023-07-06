import json

with open("wl.json", "r", encoding="utf-8") as wl_file:
    wl_data = json.load(wl_file)

with open("badwords.txt", "r", encoding="utf-8") as badwords_file:
    for line in badwords_file:
        word = line.strip()
        wl_data.append(word)

with open("wl.json", "w", encoding="utf-8") as wl_file:
    json.dump(wl_data, wl_file)
