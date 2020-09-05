import sys, os
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from pages.page_filemanager import PageFilemanager


class TestFilemanager:

    def setup(self):
        self.driver = init_driver()
        self.page_filemanager = PageFilemanager(self.driver)

    def test_refresh(self):
        name = self.page_filemanager.get_first_file_name()
        self.page_filemanager.swipe_one_screen()
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_refresh_button()
        assert name == self.page_filemanager.get_first_file_name()

    def test_set_home(self):
        filename = self.page_filemanager.create_random_folder_and_get_filename()
        self.page_filemanager.find_and_enter_file(filename)
        home_path = self.page_filemanager.get_current_path()
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_set_home_button()
        self.driver.close_app()
        self.driver.start_activity('com.cyanogenmod.filemanager', '.activities.NavigationActivity')
        current_path = self.page_filemanager.get_current_path()
        self.page_filemanager.set_root_path_as_home()
        assert current_path == home_path

    def test_book_mark(self):
        filename = self.page_filemanager.create_random_folder_and_get_filename()
        self.page_filemanager.find_and_enter_file(filename)
        current_path = self.page_filemanager.get_current_path()
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_book_mark_button()
        self.page_filemanager.click_navigate_button()
        assert current_path in self.page_filemanager.get_book_mark_path_list()

    def test_short_cut(self):
        filename = self.page_filemanager.create_random_folder_and_get_filename()
        self.page_filemanager.find_and_enter_file(filename)
        self.page_filemanager.click_operation_button()
        self.page_filemanager.click_short_cut_button()
        assert self.page_filemanager.is_app_in_desktop(filename)
