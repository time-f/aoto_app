# -*- coding=utf-8 -*-
from page.page_lb import LB_action
from page.page_login import Login_action
from page.page_select_lb import LB_page_action


class Page:
    # 我们希望将来这个 page 可以帮我们去找到它下面的 page_font  page_serach.......
    # 从而去调用对应模型里的动作

    def __init__(self,driver):
        self.driver = driver

    @property
    def initlbPage(self):
        return LB_page_action(self.driver)

    @property
    def initloginPage(self):
        return Login_action(self.driver)

    @property
    def initlbacPage(self):
        return LB_action(self.driver)
