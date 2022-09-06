from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

opt = webdriver.ChromeOptions()

opt.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opt)

driver.get('https://yandex.ru')
driver.implicitly_wait(5)

search = driver.find_element_by_xpath("//*[@data-id = 'images'][@href = '//yandex.ru/images/']")
search.click()

url = driver.current_url
assert url == 'https://yandex.ru/images/', ('URL не соответствует https://yandex.ru/images/')

first_image = driver.find_element_by_xpath("(//*[@class = 'cl-teaser__wrap'])[1]")
first_image.click()

opened_image = driver.find_element_by_xpath("//*[contains(@class, 'cl-layout__wrap__i')]")
time.sleep(2)
first_img_url = driver.current_url

next_button = driver.find_element_by_xpath("//*[@class = 'cl-layout__nav__right']")
next_button.click()
time.sleep(2)
second_img_url = driver.current_url

if first_img_url == second_img_url:
    raise Exception('Картинка не изменилась!')

previous_button = driver.find_element_by_xpath("//*[@class = 'cl-layout__nav__left']")
previous_button.click()
time.sleep(1)

first_img_url_back = driver.current_url
if first_img_url != first_img_url_back:
    raise Exception('Не первая картинка!')

img_src = driver.find_element_by_xpath("//*[@class = 'image__image']")
attrib = img_src.get_attribute('src')

resp = requests.get(attrib)

if resp.status_code != 200:
    raise Exception('Что не так с источником картинки!')

driver.close()