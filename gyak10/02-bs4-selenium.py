import bs4
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

URL = r"https://www.netpincer.hu/city/szeged"


def main():
    # driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(URL)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    all_restaurants = soup.find("section", attrs={'class': 'vendor-list-section'})
    for etterem in all_restaurants.find_all('li'):
        piros_sav = etterem.find('div', attrs={'class': 'tag-container'})
        if piros_sav:
            for kedvezmeny_jelzo in ["kedvezmény", "ingyen", "ajándék"]:
                if kedvezmeny_jelzo in piros_sav.text.lower():
                    print("Kedvezmény van!")
                    # CSS Selector
                    # Másolás a böngészőből
                    fig_caption = etterem.select('a:nth-child(1) > figure:nth-child(1) > figcaption:nth-child(2) > span:nth-child(1) > span:nth-child(1)')
                    # print(fig_caption)
                    print(f"-- {fig_caption[0].text} - {piros_sav.text}")
    driver.close()


if __name__ == '__main__':
    main()
