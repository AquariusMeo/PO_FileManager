from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import random
import time


class PageFilemanager(BaseAction):

    operation_button = By.XPATH, ["content-desc,操作", "resource-id,com.cyanogenmod.filemanager:id/ab_actions"]
    refresh_button = By.XPATH, "text,刷新"
    set_home_button = By.XPATH, "text,设置为主页"
    navigate_button = By.XPATH, "content-desc,打开导航抽屉"
    book_mark_button = By.XPATH, "text,添加到书签"
    short_cut_button = By.XPATH, "text,添加快捷方式"
    file_name_list = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"
    new_folder_button = By.XPATH, "text,新建文件夹,1"
    text_input_area = By.CLASS_NAME, "android.widget.EditText"
    ok_button = By.XPATH, "text,确定,1"

    def click_operation_button(self):
        self.click(self.operation_button)

    def click_refresh_button(self):
        self.click(self.refresh_button)

    def click_set_home_button(self):
        self.click(self.set_home_button)

    def click_navigate_button(self):
        self.click(self.navigate_button)

    def click_book_mark_button(self):
        self.click(self.book_mark_button)

    def click_new_folder_button(self):
        self.click(self.new_folder_button)

    def click_short_cut_button(self):
        self.click(self.short_cut_button)

    def click_ok_button(self):
        self.click(self.ok_button)

    def get_first_file_name(self):
        return self.find_element(self.file_name_list).text

    def get_current_path(self):
        time.sleep(2)
        eles = self.find_elements((By.ID, "com.cyanogenmod.filemanager:id/breadcrumb_item"))
        path = ''
        for i in eles:
            path = path + "/" + i.text
        return path[2:]

    def get_book_mark_path_list(self):
        eles = self.find_elements((By.ID, "com.cyanogenmod.filemanager:id/bookmarks_item_path"))
        book_mark_path_list = []
        for i in eles:
            book_mark_path_list.append(i.text)
        return book_mark_path_list

    def set_root_path_as_home(self):
        self.driver.close_app()
        self.driver.start_activity('com.cyanogenmod.filemanager', '.activities.NavigationActivity')
        self.click_navigate_button()
        self.click((By.XPATH, "text,根目录,1"))
        self.click_operation_button()
        self.click_set_home_button()

    def create_random_folder_and_get_filename(self):
        self.click_operation_button()
        self.click_new_folder_button()
        self.find_element(self.text_input_area).clear()
        text = str(random.randint(0, 9))
        self.input_text(self.text_input_area, text)
        while 1:
            try:
                self.find_element((By.XPATH, "text,此名称已存在."), 2, 0.5)
                text = text + str(random.randint(0, 9))
                self.input_text(self.text_input_area, text[-1])
            except Exception:
                break
        self.click_ok_button()
        return text

    def find_and_enter_file(self, filename):
        first_filename = ""
        while 1:
            try:
                self.find_element((By.XPATH, ["text," + filename + ",1",
                                              "resource-id,com.cyanogenmod.filemanager:"
                                              "id/navigation_view_item_name,1"]), 2, 0.5).click()
                break
            except Exception:
                if first_filename != self.get_first_file_name():
                    first_filename = self.get_first_file_name()
                    self.swipe_one_screen("down")
                else:
                    raise Exception("Can not find file.")
