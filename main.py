from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test():
    searchText = 'pomade'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)

    driver.get('https://www.cultbeauty.com/')
    driver.find_elements_by_css_selector('#header-search-input')[0].send_keys(searchText)
    driver.find_elements_by_css_selector('#header-search-input')[0].send_keys(Keys.ENTER)


    receivedText = driver.find_elements_by_css_selector('#responsive-product-list-title')[0].text.lower()

    print(receivedText)
    assert receivedText == "“" + searchText + "”", 'Error test'

    # python -m pytest test.py 