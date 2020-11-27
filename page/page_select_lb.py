from selenium.webdriver.common.by import By
from base.basecation import Baseaction

class LB_page_action(Baseaction):



    select_q1 = By.XPATH,"//*[contains(@text,'问卷一')]"
    select_q2 = By.XPATH,"//*[contains(@text,'问卷二')]"
    select_q4 = By.XPATH,"//*[contains(@text,'问卷四')]"
    select_q5 = By.XPATH,"//*[contains(@text,'问卷五')]"
    select_q6 = By.XPATH,"//*[contains(@text,'问卷六')]"
    select_q7 = By.XPATH,"//*[contains(@text,'问卷七')]"
    select_q9 = By.XPATH,"//*[contains(@text,'MVS')]"

    def click_select_q1(self):
        self.click(self.select_q1)
    def click_select_q2(self):
        self.click(self.select_q2)
    def click_select_q4(self):
        self.click(self.select_q4)
    def click_select_q5(self):
        self.click(self.select_q5)
    def click_select_q6(self):
        self.click(self.select_q6)
    def click_select_q7(self):
        self.click(self.select_q7)
    def click_select_q9(self):
        self.click(self.select_q9)
