from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageFilemanager(BaseAction):

    operation_button = By.XPATH, ["content-desc,操作", "resource-id,com.cyanogenmod.filemanager:id/ab_actions"]
    refresh_button = By.XPATH, "text,刷新"
    set_home_button = By.XPATH, "text,设置为主页"
    navigate_button = By.XPATH, "content-desc,打开导航抽屉"
    book_mark_button = By.XPATH, "text,添加到书签"
    file_name_list = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click_text("确定")
        self.click_text("主页")

    def click_operation_button(self):
        self.click(self.operation_button)

    def click_refresh_button(self):
        self.click(self.refresh_button)

    def down_swipe(self):
        x = self.driver.get_window_size()["width"]*0.5
        y = self.driver.get_window_size()["height"]
        self.swipe(x, 0.75*y, x, 0.25*y, 5000)

    def get_first_file_name(self):
        return self.find_element(self.file_name_list).text

    def is_text_exist(self, text):
        try:
            self.find_element((By.XPATH, "text,"+text))
            return True
        except Exception:
            return False

    def click_text(self, text):
        self.find_element((By.XPATH, "text,"+text)).click()

    def click_set_home_button(self):
        self.click(self.set_home_button)

    def click_navigate_button(self):
        self.click(self.navigate_button)

    def click_book_mark_button(self):
        self.click(self.book_mark_button)
