from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://google.com")
driver.close()

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://google.com")
driver.close()
