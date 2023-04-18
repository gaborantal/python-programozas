import bs4
import yaml
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

URL = "https://www.coosp.etr.u-szeged.hu/"

with open("credentials.yaml", encoding="utf8") as fp:
    conf = yaml.load(fp, Loader=yaml.FullLoader)


def main():
    felvett_targyak = dict()

    opts = Options()
    opts.headless = True

    # driver = webdriver.Firefox()
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(URL)
    username = driver.find_element("id", "username")
    username.send_keys(conf['user']['neptun'])
    password = driver.find_element("id", "password")
    password.send_keys(conf['user']['password'])
    search_button = driver.find_element("xpath", "//input[@type='submit' and @value='Belépés']")
    search_button.click()
    #
    # slider = driver.find_element_by_css_selector("div.slider")
    # move = ActionChains(driver)
    # move.click_and_hold(slider).move_by_offset(200, 0).release().perform()
    #
    # WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div.sliderOk"))
    # )
    # table = driver.find_element_by_css_selector("#resultingTable").get_attribute('outerHTML')
    # soup = bs4.BeautifulSoup(table, "html.parser")

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    scenes = soup.find("div", attrs={'id': 'scenetreecontainer'})
    for scene in scenes.find_all('div', attrs={'class': 'scene'}):
        title = scene.find('span', attrs={'class': 'title'})
        # print(title)
        # print(title['title'])
        if title.text not in felvett_targyak:
            felvett_targyak[title.text] = 0
        felvett_targyak[title.text] += 1

    print("Felvett tárgyaim")
    for targy, felvetelek_szama in felvett_targyak.items():
        if felvetelek_szama > 1:
            print(f"-- {targy}, {felvetelek_szama} alkalommal.")


if __name__ == '__main__':
    main()
