import os
from time import strftime, localtime

from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def driver_before():
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ["enable-logging"])
    service = Service(executable_path="D:\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def screenshots_config(driver):
    path = 'D:/myspace/my_project/AquariusPY/'
    path = os.path.join(path, 'screenshots')
    if not os.path.exists(path):
        os.mkdir(path)
    file_name = strftime('%Y_%m_%d_%H_%M_%S', localtime()) + '.png'
    path = os.path.join(path, file_name)
    driver.get_screenshot_as_file(path)


def env_url():
    return "https://192.168.3.110:8080"
