from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from Tools.scripts.highlight import default_latex_document

driver=webdriver.Firefox()
driver.get("http://********")
# 最大浏览器
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("183*****")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
# 点击工作流
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span").click()
sleep(2)
# 点击工作流发起
driver.find_element_by_partial_link_text('工作流发起').click()
sleep(2)
# 点击出差申请
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/div[1]/div/div/div[5]/div/span/img').click()
# 选择开始时间
sleep(2)
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/form/div[1]/div[2]/div/div/div/input').click()
sleep(6)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/table[1]/tbody/tr[3]/td[3]/div/span').click()
sleep(2)
# 点击确认按钮
driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]/span').click()
sleep(2)
# 选择结束时间
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/form/div[1]/div[3]/div/div/div/input').click()
sleep(6)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[3]/td[4]/div/span').click()
sleep(2)
# 点击确认按钮
driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]/span').click()
sleep(2)
# 输入预算金额
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/form/div[6]/div/div/div/div/div[1]/input').send_keys(11)
sleep(2)
# 输入主要业务单位
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/form/div[8]/div[1]/div/div/div/input').send_keys("职能信息巴")
sleep(2)
# 输入联系人电话：
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/form/div[8]/div[2]/div/div/div/input').send_keys(18456051574)
sleep(2)
# 输入出入事由
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/form/div[8]/div[3]/div/div/div/input').send_keys("测试")
sleep(2)
# 输入出差地点及路线：
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/form/div[9]/div/div/input').send_keys("测试")
sleep(2)
# 点击提交按钮
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/div[3]/button[3]/span').click()
sleep(2)
# 点击提交按钮
# driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button/span').click()
# 点击依然创建
driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[2]/span').click()
sleep(10)
driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button/span').click()
# 上级领导登录
driver=webdriver.Firefox()
driver.get("http://******")
# 最大浏览器
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("1352****")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
# 点击工作流
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span").click()
sleep(2)
# 点击工作流处理
driver.find_element_by_partial_link_text('工作流处理').click()
sleep(2)
# 点击工作流处理第一个单据
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/div/div[2]/div/form/div/div[3]/table/tbody/tr[1]/td[2]/div/span').click()
# 点击通过按钮
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[2]/div/div[1]/div[2]/button[2]/span').click()
# 二次点击通过按钮
driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
# 申请人核销出差单据
driver=webdriver.Firefox()
driver.get("http://test*****")
# 最大浏览器
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("1835***")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button').click()
sleep(2)
# 点击工作流
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span").click()
sleep(2)
# 点击工作流处理
driver.find_element_by_partial_link_text('工作流处理').click()
sleep(2)
# 点击工作流处理第一个单据
driver.find_element_by_xpath('//*[@id="app-main"]/div[2]/div/div/div[2]/div/form/div/div[3]/table/tbody/tr[1]/td[2]/div/span').click()
# 点击通过按钮
sleep(3)
driver.find_element_by_xpath('/html/body/div/div/div[2]/section/div[2]/div/div[1]/div[2]/button[2]/span').click()
# 二次点击通过按钮
driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
