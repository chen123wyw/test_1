from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
class Test01(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://****")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        sleep(3)
        self.driver.quit()
    def test_login(self):
        driver=self.driver
        driver.find_element_by_css_selector('.form-control').send_keys("******")
        driver.find_element_by_css_selector('[id="password"]').send_keys("123456")
        driver.find_element_by_css_selector('[id="btn-form-submit"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="0c11758d-ca99-4d07-a4e5-cb7725df11c3"]/a/span[1]').click()
        # 点击用户切换
        driver.find_element_by_xpath('//*[@id="9e2036b8-9b2c-4018-8633-889b2e2ce5a4"]/a/span').click()
        # driver.find_element_by_css_selector(".col-lg-5").send_keys("mima")
        sleep(2)
        # 输入密码点击回车6666666
        driver.find_element_by_xpath('//*[@id="passWD"]').send_keys("mima")
        driver.find_element_by_xpath('//*[@id="passWD"]').send_keys(Keys.ENTER)
        sleep(2)
        # 隐藏元素的查找
        # js ='document.getElementById("userpy").removeAttribute("readonly")'#定位隐藏元素（放上面，放下面都可以）
        # driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="userpy"]').click()
        driver.find_element_by_xpath('//*[@id="userpy"]').send_keys("hzj")
        # 选择黄竹君--#定位隐藏元素
        js = 'document.getElementById("userpy").removeAttribute("readonly")'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="ui-id-3"]').click()
        # 点击确定按钮
        driver.find_element_by_xpath('/html/body/div/div/section/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/button').click()
        sleep(2)
        # 成功切换用户成功后，点击工作流
        driver.find_element_by_xpath('/html/body/div/aside/section/ul[1]/li[4]/a/span[1]').click()
        sleep(10)
        # 点击工作流（旧区）
        driver.find_element_by_xpath('/html/body/div/aside/section/ul[1]/li[4]/ul/li[3]/a/span').click()
        sleep(10)
        # 点击单号
        # 切换iframe
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to_frame(iframe)
        driver.switch_to_frame("fileFrame")
        driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr[1]/td/table/tbody/tr[5]/td[1]/a").click()
        # 点击发票类型
        driver.find_element_by_xpath('//*[@id="InvoiceType"]').click()
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[11]/td[2]/select/option[2]').click()
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

        if __name__ == '__main__':
            unittest.main()