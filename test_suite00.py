from time import sleep
import pytest
from config.driver_config import *
from pageObject.DataSourcePage import DataSourcePage
from pageObject.LoginPage import LoginPage
from pageObject.DataSpacePage import DataSpacePage
from hamcrest import *
from config.MakeData import f
from time import strftime, localtime


class TestSuite00(object):

    def setup_class(self):
        self.driver = driver_before()
        self.driver.get("https://192.168.5.61:8080/login")
        login_page = LoginPage(self.driver)
        login_page.login("raoyun", "baidu.123")
        sleep(2)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.login("raoyun", "123456")
        sleep(2)
        assert_that(self.driver.current_url, contains_string("dataSpace"))

    @pytest.mark.skip
    def test_login_fail(self):
        login_page = LoginPage(self.driver)
        login_page.login("raoyun", "123456789")
        sleep(2)
        assert_that(self.driver.current_url, contains_string("login"))

    @pytest.mark.skip
    def test_search_data_space_by_time(self):
        data_space_page = DataSpacePage(self.driver)
        search_time = data_space_page.tag_text(data_space_page.list_time_property_three).split(" ")[0]
        data_space_page.time_choose(search_time, search_time)
        text = data_space_page.tag_text(data_space_page.list_time_property_one)
        assert_that(text, contains_string(search_time))
        self.driver.refresh()

    @pytest.mark.skip
    def test_search_data_space_by_creator(self):
        data_space_page = DataSpacePage(self.driver)
        search_name = data_space_page.tag_text(data_space_page.list_creator_property_three)
        data_space_page.creator_choose(search_name)
        text = data_space_page.tag_text(data_space_page.list_creator_property_one)
        assert_that(text, contains_string(search_name))
        self.driver.refresh()

    @pytest.mark.skip
    def test_search_data_space_by_data_upload_status(self):
        data_space_page = DataSpacePage(self.driver)
        search_status_name = data_space_page.tag_text(data_space_page.list_upload_property_three)
        data_space_page.data_upload_status_choose(search_status_name)
        sleep(1)
        text = data_space_page.tag_text(data_space_page.list_upload_property_one)
        sleep(2)
        assert_that(text, contains_string(search_status_name))
        self.driver.refresh()

    @pytest.mark.skip
    def test_search_data_space_by_space_name(self):
        data_space_page = DataSpacePage(self.driver)
        search_space_name = data_space_page.tag_text(data_space_page.list_name_property_three)
        data_space_page.data_space_name_choose(search_space_name)
        sleep(2)
        result_name = data_space_page.tag_text(data_space_page.list_name_property_one)
        assert_that(result_name, contains_string(search_space_name))
        self.driver.refresh()

    @pytest.mark.skip
    # 新增一个数据空间
    def test_create_data_space(self):
        data_space_page = DataSpacePage(self.driver)
        data_space_page.create_data_space(f.sentence(), f.sentence())
        assert_that(data_space_page.tag_text(data_space_page.info_tip), contains_string("添加成功"))
        sleep(2)
        self.driver.refresh()

    @pytest.mark.skip
    # 删除列表第一个数据空间
    def test_delete_data_space(self):
        data_space_page = DataSpacePage(self.driver)
        data_space_page.delete_data_space()
        assert_that(data_space_page.tag_text(data_space_page.info_tip), contains_string("删除成功"))
        self.driver.refresh()

    # SMB连接测试
    def test_shared_directory_connection(self):
        source_page = DataSourcePage(self.driver)
        source_page.into_page()
        text = source_page.create_data_source("smb", source_name=f.sentence(), ip="192.168.11.127",
                                              username="raoyun", password="baidu.123")
        assert_that(text, contains_string("连接成功"))
