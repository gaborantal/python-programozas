import os

import markovify


def get_lyrics(eloado):
    with open(os.path.join("data", f"{eloado}.txt"), "r") as fp:
        lyrics = fp.read()
    text_model = markovify.Text(lyrics)
    text_model = text_model.compile(True)
    rv = ""
    for i in range(5):
        # print(text_model.make_sentence())
        rv += text_model.make_short_sentence(100, 20) or ""
        rv += "<br />"
    return rv


if __name__ == '__main__':
    get_lyrics("three_days_grace")
