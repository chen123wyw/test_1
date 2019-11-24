from idlelib import browser
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# 实例化浏览器
driver = webdriver.Firefox()
# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(30)
# 定义url
url = "*******"
# 获取url
driver.get(url)

# __author__ = 'Administrator'
# # 导包
# from time import sleep
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
# # 实例化浏览器
# driver = webdriver.Firefox()
# driver.maximize_window()
# # driver.set_window_size(600,600)
# # 登录url
# driver.get("https://test-pc-oms.regs.com/#/login")
driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[1]/div/div[1]/input").send_keys("***")
# 定位密码框
driver.find_element_by_xpath('/html/body/div/div/div[3]/form/div[2]/div/div/input').send_keys("****")
# 定位登录
driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div[4]/div/button/span").click()
sleep(3)
# 点击订单管理
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[2]/ul/div[1]/li/div/span").click()
# 点击下单管理
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[2]/ul/div[1]/li/ul/div[1]/li/div/span").click()
# 点击点击贸易分单
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[2]/ul/div[1]/li/ul/div[1]/li/ul/a[2]/li/span").click()
sleep(3)
# 点击新建按钮
driver.find_element_by_xpath("html/body/div/div/div[3]/section/div/div/div[1]/div/div/div[2]/button[3]/span").click()
sleep(3)
# 选择航班号
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div/div/div/div/input").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li/span").click()
sleep(3)
# 输入运单号
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div/div/div/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[3]/div/div/div/input').send_keys("666")
sleep(1)
# 输入发票号
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div/div/div[1]/input').send_keys("666")
# 选择接单部门
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[4]/div/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
sleep(1)
# 选择客户
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/form/div[1]/div[4]/div[1]/div/div/div/div/input').click()
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span').click()
# 点击下一步按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/span/button').click()
sleep(3)
# 选择产品类型
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]/span').click()
sleep(3)
# 选择毛重
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div/div[1]/input').send_keys("3")
sleep(3)
# 选择配送方式
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/form/div[1]/div[3]/div/div/div[1]/div/input').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[2]/span').click()
sleep(3)
# 选择发货人
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/form/div[1]/div[4]/div/div/div/div/input').click()
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]/span').click()
sleep(6)
# 点击货物信息
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/button[2]/span').click()
sleep(3)
# 基本信息-商品名称
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/input').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[1]/ul/li/span').click()
sleep(3)
# 输入件数
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[1]/input').click()

driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[1]/input').send_keys("1")
sleep(1)
# 输入净重
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[1]/input').send_keys("1")
sleep(1)
# 每件净重
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/input').click()
sleep(1)
# 输入单价
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[3]/div[3]/div/div/div/div[1]/input').send_keys("2")
sleep(1)
# 点击总价
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input').send_keys("2")

sleep(2)
# 点击成交货币
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[1]/div[4]/div[2]/div/div/div/div/input').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/ul/li[4]/span').click()
sleep(2)
# 点击保存
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/button[2]/span').click()
sleep(2)
# 收货信息
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/input').click()
driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/ul/li[2]/span').click()
sleep(1)
# 点击保存按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/button[2]/span').click()
sleep(2)
# 点击下一步
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[2]/div/div[5]/div/div/div[2]/span/button[2]/span').click()
# 点击应收费用按钮
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div/div[2]/button').click()
sleep(5)
# 新增应收费用
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[1]/div[1]/div/div/div/div/input').click()
# 选择费用类型
driver.find_element_by_xpath("/html/body/div[12]/div[1]/div[1]/ul/li[1]/span").click()
sleep(5)
# 选择币种
# driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input").click()
# sleep(5)
# driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[4]/span").click()
sleep(5)
# 选择汇率
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[2]/div[2]/div/div/div/div[1]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[2]/div[2]/div/div/div/div[1]/input").send_keys("2")
sleep(5)
# 选择货币金额
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/div[1]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[2]/form/div[3]/div[1]/div/div/div[1]/div[1]/input").send_keys("10")
sleep(5)
# 点击保存按钮
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/div/div[3]/div/button[2]/span").click()
sleep(5)
# 拖到指定位置
#滚动到底部
target = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[3]/div/div')    # 聚焦元素
driver.execute_script("arguments[0].scrollIntoView();", target)

# 点击应付费用按钮
sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div/div[2]/button/span').click()
sleep(5)
# 点击费用名称
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[13]/div[1]/div[1]/ul/li[1]/span").click()
sleep(5)
# 选择币种
# driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[2]/div[1]/div/div/div/div[1]/input").click()
# driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]/span").click()
sleep(5)
# 选择汇率
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[2]/div[2]/div/div/div/div[1]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[1]/input").send_keys("2")
sleep(5)
# 选择货币金额
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[3]/div[1]/div/div/div/div[1]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[3]/div[1]/div/div/div/div[1]/input").send_keys("30")
sleep(5)
# 选择结算供应商
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[2]/form/div[4]/div[1]/div/div/div/div/input").click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[14]/div[1]/div[1]/ul/li[1]/span").click()
sleep(3)
# 点击保存按钮
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[3]/div[4]/div/div[3]/div/button[2]").click()
sleep(3)
# 点击下一步按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[3]/div/div[4]/div/div/div[2]/span/button[2]/span').click()
sleep(3)
# 点击保存按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/section/div/div/div[2]/div[4]/div/div[1]/div[16]/div/div/div[2]/button[3]/span').click()


driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()
driver.find_element_by_xpath('').click()