from appium import webdriver


def initDriver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '32b36e8e'
    # app信息
    desired_caps['appPackage'] = 'com.iotimc.answer'
    # 启动页
    desired_caps['appActivity'] = 'com.iotimc.answer.activity.login.LoginActivity'
    # 用于获取toast的插件
    # desired_caps[ 'automationName'] = 'Uiautomator2'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver