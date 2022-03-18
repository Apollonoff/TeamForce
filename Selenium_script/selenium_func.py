#pip install selenium
#pip install fake_useragent


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup



url = 'https://www.google.com/'
#
# useragent = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={useragent.random}")
# options.add_argument('headless')

#set proxy
#options.add_argument("--proxy-server=138.128.91.65:8888")

driver = webdriver.Chrome(options=options)

try:
    driver.get(url=url)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



# if __name__ == '__main__':
#     name = ''
#     selenium_bot_father(name)