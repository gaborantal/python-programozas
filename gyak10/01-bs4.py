import bs4
import requests

URL = r"https://www.tvmustra.hu/"


def main():
    resp = requests.get(URL)
    # ellenőrzések
    print(resp.text)
    # keresgélés?
    # regex?

    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    print("text", soup.get_text())
    print("title", soup.find("title"))
    print("title", soup.title)  # Nem minden tag érhető el így!
    print("title text", soup.find("title").text)
    print("title str", soup.find("title").string)
    print("Összes kép az oldalon:", len(soup.find_all("img")))
    # Tag objektumok
    title = soup.find("title")
    print("tag neve", title.name)

    all_scripts = soup.find_all("script")
    elso = all_scripts[1]
    print(elso.name)
    print(elso['src'])

    print(soup.find_all("div", clazz='home_csatorna_musor_blokk'))
    print(soup.find_all("div", class_='home_csatorna_musor_blokk'))
    print(soup.find_all("div", attrs={'class': 'home_csatorna_musor_blokk'}))

    print("---")
    for event in soup.find_all("div", attrs={'class': 'home_csatorna_musor_blokk'}):
        if 'Hal a tortán' in event['title']:
            print(event)
            print("Keresett műsor megtalálva!")
            title_time = event['title'].replace('\n', ' ')
            print(f"-- {event['data-channel']} {title_time}")


if __name__ == '__main__':
    main()
