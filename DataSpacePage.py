from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataSpacePage(object):
    def __init__(self, driver):
        self.driver = driver
        # 新增空间按钮
        self.create_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/button/span")
        # 新增空间姓名
        self.create_name_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[2]/div/div/div["
                                            "2]/div/div[1]/div/div[1]/div/input")
        # 新增空间备注
        self.create_note_textarea = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[2]/div/div/div["
                                               "2]/div/div[1]/div/div[2]/div/textarea")
        # 新增空间确认按钮
        self.create_confirm_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[2]/div/div/div["
                                             "3]/span/button[2]/span")
        # 列表第一项删除按钮
        self.delete_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[2]/div/div/div["
                                     "1]/div/div[1]/div[12]/button[3]/span")
        # 删除确认按钮
        self.delete_confirm_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[2]/div/div/div["
                                             "3]/span/button[2]/span")
        # 消息提示
        self.info_tip = (By.XPATH, "/html/body/div[3]/div/div[2]")

        # 列表第一项空间名称
        self.list_one_name = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[2]/div/div/div["
                                        "1]/div/div/div[2]/a")
        # 时间搜索-开始-input
        self.time_start_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                           "1]/div/div[1]/div/input")
        # 时间搜索-结束-input
        self.time_end_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                         "1]/div/div[2]/div/input")
        # 创建人div
        self.creator_div = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[2]/div["
                                      "1]/div")
        # 用户搜索框
        self.user_search_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                            "2]/div[2]/div/div/div/input")
        # 用户列表第一项
        self.user_list_one = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                        "2]/div[2]/ul/li[2]/div/span")
        # 数据上传状态div
        self.data_upload_status = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                             "3]/div[1]/div")
        # 全部
        self.status_all = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                     "3]/div[2]/ul/li[1]/div/span")
        # 未上传
        self.status_dis_upload = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                            "3]/div[2]/ul/li[2]/div/span")
        # 上传中
        self.status_in_upload = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                           "3]/div[2]/ul/li[3]/div/span")
        # 上传成功
        self.status_success = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                         "3]/div[2]/ul/li[4]/div/span")
        # 上传失败
        self.status_fail = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[3]/div["
                                      "2]/ul/li[5]/div/span")
        # 工作状态div
        self.work_status_div = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                          "4]/div[1]")
        # 工作状态-全部
        self.work_status_all = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                          "4]/div[2]/div/ul/li[1]/label/span[2]")
        # 待上传数据
        self.work_status_dis_upload = (By.XPATH, "")
        # 上传结果待确认
        self.work_status_upload_result_wait_confirm = (By.XPATH, "")
        # 待清洗
        self.work_status_wait_clean = (By.XPATH, "")
        # 清洗中
        self.work_status_in_clean = (By.XPATH, "")
        # 待发布
        self.work_status_wait_release = (By.XPATH, "")
        # 已发布
        self.work_status_release_after = (By.XPATH, "")
        # 暂缓处理
        self.work_status_stop_deal = (By.XPATH, "")
        # 数据空间列表-时间-第一项
        self.list_time_property_one = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                 "2]/div/div/div[1]/div/div[1]/div[10]")
        # 数据空间列表-时间-第三项
        self.list_time_property_three = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                   "2]/div/div/div[1]/div/div[3]/div[10]")
        # 数据空间列表-创建人-第一项
        self.list_creator_property_one = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                    "2]/div/div/div[1]/div/div[1]/div[11]")
        # 数据空间列表-创建人-第三项
        self.list_creator_property_three = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                      "2]/div/div/div[1]/div/div[3]/div[11]")
        # 数据空间列表-数据上传状态-第一项
        self.list_upload_property_one = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                   "2]/div/div/div[1]/div/div[1]/div[6]")
        # 数据空间列表-数据上传状态-第三项
        self.list_upload_property_three = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                     "2]/div/div/div[1]/div/div[3]/div[6]")
        # 数据空间列表-空间名称-第一项
        self.list_name_property_one = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                 "2]/div/div/div[1]/div/div[1]/div[2]/a")
        # 数据空间列表-空间名称-第三项
        self.list_name_property_three = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div["
                                                   "2]/div/div/div[1]/div/div[3]/div[2]/a")
        # 按数据空间名称搜索-input
        self.space_name_input = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                           "5]/input")
        # 搜索按钮
        self.search_btn = (By.XPATH, "//*[@id=\"main-app\"]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div["
                                     "5]/button/span")

    def create_data_space(self, name, note):
        self.driver.find_element(*self.create_btn).click()
        self.driver.find_element(*self.create_name_input).send_keys(name)
        self.driver.find_element(*self.create_note_textarea).send_keys(note)
        self.driver.find_element(*self.create_confirm_btn).click()

    def delete_data_space(self):
        self.driver.find_element(*self.delete_btn).click()
        sleep(1)
        self.driver.find_element(*self.delete_confirm_btn).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.info_tip))

    def tag_text(self, web_element):
        return self.driver.find_element(*web_element).text

    def time_choose(self, start_time, end_time):
        self.driver.find_element(*self.time_start_input).send_keys(start_time)
        self.driver.find_element(*self.time_end_input).send_keys(end_time)

    def creator_choose(self, username):
        self.driver.find_element(*self.creator_div).click()
        self.driver.find_element(*self.user_search_input).send_keys(username)
        sleep(2)
        self.driver.find_element(*self.user_list_one).click()

    def data_upload_status_choose(self, status_name):
        self.driver.find_element(*self.data_upload_status).click()
        if status_name == "全部":
            self.driver.find_element(*self.status_all).click()
        elif status_name == "未上传":
            self.driver.find_element(*self.status_dis_upload).click()
        elif status_name == "上传中":
            self.driver.find_element(*self.status_in_upload).click()
        elif status_name == "上传成功":
            self.driver.find_element(*self.status_success).click()
        elif status_name == "上传失败":
            self.driver.find_element(*self.status_fail).click()

    def data_space_name_choose(self, name):
        self.driver.find_element(*self.space_name_input).send_keys(name)
        self.driver.find_element(*self.search_btn).click()
