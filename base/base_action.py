import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 点击元素
    def click(self, button):
        self.find_element(button).click()

    # 输入文本
    def input_text(self, area, text):
        self.find_element(area).send_keys(text)

    # 寻找元素，返回当前页面首个匹配对象
    def find_element(self, loc, timeout=5, poll=1):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath(loc_value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc_by, loc_value))

    # 寻找元素，返回当前页面所有匹配对象
    def find_elements(self, loc, timeout=5, poll=1):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath(loc_value)
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(loc_by, loc_value))

    # 判断某toast内容是否存在
    def is_toast_exist(self, toast):
        try:
            self.find_element((By.XPATH, "text,"+toast), 5, 0.1)
            return True
        except Exception:
            return False

    def is_loc_exist(self, loc):
        try:
            self.find_element(loc)
            return True
        except Exception:
            return False

    # XPATH简写法解析函数
    @staticmethod
    def make_xpath_mid(expr):
        alist = expr.split(',')
        if len(alist) == 2:
            xpath_mid = "contains(@" + alist[0] + ",'" + alist[1] + "')"
        elif (len(alist) == 3) and alist[2] == '0':
            xpath_mid = "contains(@" + alist[0] + ",'" + alist[1] + "')"
        elif (len(alist) == 3) and alist[2] == '1':
            xpath_mid = "@" + alist[0] + "='" + alist[1] + "'"
        else:
            raise Exception("XPATH expression not correct.")
        return xpath_mid + 'and '

    # XPATH简写法解析函数
    def make_xpath(self, expr):
        xpath_start = '//*['
        xpath_end = ']'
        xpath_mid = ''
        if isinstance(expr, str):
            if expr.startswith("//*["):
                return expr
            xpath_mid = self.make_xpath_mid(expr).rstrip('and ')
        elif isinstance(expr, list):
            for i in expr:
                xpath_mid += self.make_xpath_mid(i)
            xpath_mid = xpath_mid.rstrip('and ')
        else:
            raise TypeError("XPATH expression must be a string or a list.")
        return xpath_start + xpath_mid + xpath_end

    # 按指定方向滑动一屏
    def swipe_one_screen(self, direction="down"):
        size = self.driver.get_window_size()
        height = size["height"]
        width = size["width"]
        if direction == "down":
            self.driver.swipe(0.5 * width, 0.75 * height, 0.5 * width, 0.25 * height, 3000)
        elif direction == "up":
            self.driver.swipe(0.5 * width, 0.25 * height, 0.5 * width, 0.75 * height, 3000)
        elif direction == "left":
            self.driver.swipe(0.25 * width, 0.5 * height, 0.75 * width, 0.5 * height, 3000)
        elif direction == "right":
            self.driver.swipe(0.75 * width, 0.5 * height, 0.25 * width, 0.5 * height, 3000)
        else:
            raise Exception("Wrong swipe direction. Please use 'down','up','left' or 'right'.")

    # 判断某app是否在桌面
    def is_app_in_desktop(self, app_name):
        time.sleep(2)
        self.driver.press_keycode("3")
        time.sleep(2)
        self.driver.press_keycode("3")
        screens = len(self.find_elements((By.ID, "com.vphone.launcher:id/inactive")))
        for i in range(screens+1):
            try:
                self.find_element((By.XPATH, "text," + app_name + ",1"))
                return True
            except Exception:
                self.swipe_one_screen("right")
        return False
