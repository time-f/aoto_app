from selenium.webdriver.common.by import By

from base.basecation import Baseaction

class Login_action(Baseaction):


    allow_use = By.XPATH, "//*[contains(@text,'仅在使用中允许')]"
    phone = By.XPATH,"//*[contains(@text,'手机号码')]"
    password = By.XPATH,"//*[contains(@text,'密码')]"
    online = By.XPATH,"//*[contains(@text,'在线')]"

    select_user = By.XPATH,"//*[contains(@text,'京二')]"

    def click_allow(self):
        self.click(self.allow_use)

    def input_phone(self,value):
        self.input_txt(self.phone,value)

    def input_password(self,value):
        self.input_txt(self.password,value)


    def click_online(self):
        self.click(self.online)

    def click_user(self):
        self.click(self.select_user)

