from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


opt = webdriver.ChromeOptions()

opt.add_argument("start-maximized")

opt.add_argument("--ignore-certificate-errors")

opt.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=opt)

driver.get('https://yandex.ru')
driver.implicitly_wait(5)

search = driver.find_element_by_xpath("//*[@class='input__control input__input']")
search.send_keys('Тензор')

suggest = driver.find_element_by_xpath("//*[@class='suggest2__content suggest2__content_theme_normal']")

search.send_keys(Keys.ENTER)

results = driver.find_element_by_xpath("//*[contains(@class, 'serp-list serp-list_left_yes')]")

first_result = driver.find_element_by_xpath("//*[@class = 'serp-item'][1]//*[@href='https://tensor.ru/']")

driver.close()
