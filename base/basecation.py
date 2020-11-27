import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Baseaction():


    def __init__(self,driver):
        self.driver = driver


    # 自定义一个用来获取元素的方法
    def find_element(self,feature):
        wait = WebDriverWait(self.driver, 10, 1)
        # (feature[0], feature[1]) == By.XPATH,"//*[@text='否']"
        return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    def click(self,feature):
        self.find_element(feature).click()

    def input_txt(self,feature,value):
        self.find_element(feature).send_keys(value)

    def swipe_left(self):
        # 向左滑动2次
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        self.driver.swipe(x * 0.9, y * 0.5, x * 0.5, y * 0.5)
        time.sleep(2)
        self.driver.swipe(x * 0.9, y * 0.5, x * 0.5, y * 0.5)

    # 自定义一个获取 toast内容的方法
    def get_toast_content(self, message):
        tmp_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        ele = self.find_element(tmp_feature)
        return ele.text