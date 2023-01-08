from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataSourcePage(object):
    def __init__(self, driver):
        self.driver = driver
        # 左侧导航-数据源管理
        self.navigation_data_source = (By.XPATH, "//*[@id=\"main-app\"]/div/nav/ul/li[6]/ul/li[1]/div/span")
        # 新建数据源按钮
        self.create_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div/div[1]/button/span")
        # 对话框中共享目录按钮
        self.type_SMB = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div["
                                   "1]/div[2]/ul/li")
        # 对话框中MySQL按钮
        self.type_MySQL = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                     "1]/div[1]/div[1]/ul/li[1]")
        # 对话框中SQLServer按钮
        self.type_SQLServer = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                         "1]/div[1]/div[1]/ul/li[2]")
        # 对话框中ORACLE按钮
        self.type_ORACLE = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                      "1]/div[1]/div[1]/ul/li[3]")
        # 对话框中PostgreSQL按钮
        self.type_PostgreSQL = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                          "1]/div[1]/div[1]/ul/li[4]")
        # 对话框中一次确定按钮
        self.create_one_confirm_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div["
                                                 "2]/div/div[1]/div[2]/button[2]/span")
        # 数据源名称输入框
        self.data_source_name = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div["
                                           "2]/div/div[2]/div[1]/div[1]/div/input")
        # 数据源ip地址输入框
        self.ip_address_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div["
                                           "2]/div/div[2]/div[1]/div[2]/div/input")
        # 用户名输入框
        self.username_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                         "2]/div[1]/div[3]/div/input")
        # 密码输入框
        self.password_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                         "2]/div[1]/div[4]/div/input")
        # 备注
        self.create_note_textarea = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div["
                                               "2]/div/div[2]/div[1]/div[5]/div/textarea")
        # 连接测试按钮
        self.connection_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div["
                                         "2]/div[1]/div[6]/div/button/span")
        # 连接结果文案
        self.connection_result = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div[2]/div/div[2]/div/div["
                                            "2]/div/div[2]/div[1]/div[6]/div/label")

    def into_page(self):
        self.driver.find_element(*self.navigation_data_source).click()

    def create_data_source(self, source_type: str, source_name: str, ip: str, username: str, password: str,
                           note: str = "") -> str:
        self.driver.find_element(*self.create_btn).click()
        if source_type == "mysql":
            self.driver.find_element(*self.type_MySQL).click()
        elif source_type == "sqlserver":
            self.driver.find_element(*self.type_SQLServer).click()
        elif source_type == "oracle":
            self.driver.find_element(*self.type_ORACLE).click()
        elif source_type == "postgresql":
            self.driver.find_element(*self.type_PostgreSQL).click()
        elif source_type == "smb":
            self.driver.find_element(*self.type_SMB).click()
        self.driver.find_element(*self.create_one_confirm_btn).click()
        self.driver.find_element(*self.data_source_name).send_keys(source_name)
        self.driver.find_element(*self.ip_address_input).send_keys(ip)
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.create_note_textarea).send_keys(note)
        sleep(1)
        self.driver.find_element(*self.connection_btn).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.connection_result))
        return self.driver.find_element(*self.connection_result).text
