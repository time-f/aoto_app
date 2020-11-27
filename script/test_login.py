import pytest
import time
from base import initDriver
from base.analysis import getData
from page.page import Page

class Testlb:

    def setup_class(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(("phone","password"), getData("test_login"))
    def test_login(self,phone,password):
        self.page.initloginPage.click_allow()
        self.page.initloginPage.click_allow()
        self.page.initloginPage.input_phone(phone)
        self.page.initloginPage.input_password(password)
        self.page.initloginPage.click_online()
        self.page.initloginPage.click_user()

    def start(self):
        self.page.initlbacPage.click_confirm()
        time.sleep(8)
        self.page.initlbacPage.swipe_left()

    def end(self):
        self.page.initlbacPage.click_submit()
        self.page.initlbacPage.click_affirm()
        self.page.initlbacPage.click_confirm()

    # @pytest.mark.skip("跳过问卷1")
    @pytest.mark.run(order=2)
    def test_q1(self):
        self.page.initlbPage.click_select_q1()
        self.start()
        for i in range(122):
            self.page.initlbacPage.click_no()
        self.end()

    # @pytest.mark.skip("跳过问卷2")
    @pytest.mark.run(order=3)
    def test_q2(self):
        self.page.initlbPage.click_select_q2()
        self.start()
        for i in range(28):
            self.page.initlbacPage.click_not_sure()
        self.end()

    # @pytest.mark.skip("跳过问卷4")
    @pytest.mark.run(order=4)
    def test_q4(self):
        self.page.initlbPage.click_select_q4()
        self.start()
        for i in range(28):
            self.page.initlbacPage.click_sometimes()
        self.page.initlbacPage.input_age("33")
        time.sleep(1)
        self.page.initlbacPage.swipe_left()
        time.sleep(2)
        self.end()

    # @pytest.mark.skip("跳过问卷5")
    @pytest.mark.run(order=5)
    def test_q5(self):
        self.page.initlbPage.click_select_q5()
        self.start()
        for i in range(26):
            self.page.initlbacPage.click_occasionally()
        self.end()

    # @pytest.mark.skip("跳过问卷6")
    @pytest.mark.run(order=6)
    def test_q6(self):
        self.page.initlbPage.click_select_q6()
        self.start()
        for i in range(45):
            time.sleep(1)
            self.page.initlbacPage.click_no()
        self.end()

    # @pytest.mark.skip("跳过问卷7")
    @pytest.mark.run(order=7)
    def test_q7(self):
        self.page.initlbPage.click_select_q7()
        self.start()
        for i in range(46):
            self.page.initlbacPage.click_disagree()
        self.end()

    # @pytest.mark.skip("跳过问卷8附加题")
    @pytest.mark.run(order=8)
    def test_q8(self):
        for i in range(3):
            self.page.initlbacPage.click_no()
        self.page.initlbacPage.click_rob()
        for i in range(2):
            self.page.initlbacPage.click_no()
        self.page.initlbacPage.click_confirm()

    # @pytest.mark.skip("跳过问卷9")
    @pytest.mark.run(order=9)
    def test_q9(self):
        self.page.initlbPage.click_select_q9()
        self.start()
        for i in range(13):
            self.page.initlbacPage.click_not_sure()
        self.end()


    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()


