import time
from selenium.webdriver.common.by import By
from base.basecation import Baseaction

class LB_action(Baseaction):


    no = By.XPATH,"//*[@text='否']"
    submit = By.XPATH,"//*[@text='提交']"
    confirm = By.XPATH,"//*[@text='确定']"
    affirm = By.XPATH,"//*[@text='确认']"
    not_sure = By.XPATH,"//android.view.View[@text='不确定']"
    sometimes = By.XPATH,"//*[@text='有时']"
    age = By.CLASS_NAME,"android.widget.EditText"
    occasionally = By.XPATH,"//*[@text='偶尔']"
    rob = By.XPATH,"//*[@text='抢劫罪']"
    disagree = By.XPATH,"//*[@text='不同意']"

    def click_no(self):
        self.click(self.no)

    def click_submit(self):
        self.click(self.submit)

    def click_confirm(self):
        self.click(self.confirm)

    def click_affirm(self):
        self.click(self.affirm)

    def click_not_sure(self):
        self.click(self.not_sure)

    def click_sometimes(self):
        self.click(self.sometimes)

    def click_disagree(self):
        self.click(self.disagree)

    def click_rob(self):
        self.click(self.rob)

    def click_occasionally(self):
        self.click(self.occasionally)

    def input_age(self,value):
        self.input_txt(self.age,value)


