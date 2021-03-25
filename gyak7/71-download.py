import json
import os
import urllib.request
import shutil

HP_API = "http://hp-api.herokuapp.com/api/characters"

if os.path.exists("tmp"):
    shutil.rmtree("tmp")
os.mkdir("tmp")

with urllib.request.urlopen(HP_API) as f:
    html = f.read().decode('utf-8')
    data = json.loads(html)

    for character in data:
        print(f"{character['name']} - {character['image']}")
        print(character)
        # Első megoldás
        # with urllib.request.urlopen(character['image']) as img, \
        #         open(os.path.join("tmp", os.path.basename(character['image'])), "wb") as out:
        #     out.write(img.read())

        # Második megoldás
        # urllib.request.urlretrieve(character['image'], os.path.join("tmp", os.path.basename(character['image'])))
