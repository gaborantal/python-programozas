import markovify


def main():
    with open("data/ts1.txt", "r") as fp:
        lyrics = fp.read()
    # lyrics = lyrics.lower()
    # lyrics = lyrics.replace("\r\n\r\n", "\r\n")
    text_model = markovify.Text(lyrics)
    text_model = text_model.compile(True)
    for i in range(5):
        # print(text_model.make_sentence())
        print(text_model.make_short_sentence(100, 20))


if __name__ == '__main__':
    main()
