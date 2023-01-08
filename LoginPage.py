from selenium.webdriver.common.by import By


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.account_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/input")
        self.password_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[2]/div[1]/div[2]/div[2]/div/input")
        self.submit_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[2]/div[1]/div[2]/div[3]/button/span")

    def login(self, username, password):
        self.driver.find_element(*self.account_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_btn).click()