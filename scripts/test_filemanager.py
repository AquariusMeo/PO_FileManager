import sys, os
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from pages.page_filemanager import PageFilemanager
import time


class TestFilemanager:

    def setup(self):
        self.driver = init_driver()
        self.page_filemanager = PageFilemanager(self.driver)

    def test_refresh(self):
        name = self.page_filemanager.get_first_file_name()
        self.page_filemanager.down_swipe()
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_refresh_button()
        assert name == self.page_filemanager.get_first_file_name()

    def test_set_home(self):
        self.page_filemanager.click_text("acct")
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_set_home_button()
        self.page_filemanager.click_navigate_button()
        assert self.page_filemanager.is_text_exist("/acct")

    def test_book_mark(self):
        self.page_filemanager.click_text("acct")
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_book_mark_button()
        self.page_filemanager.click_navigate_button()
        assert self.page_filemanager.is_text_exist("/acct")
