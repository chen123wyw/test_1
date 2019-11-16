

__author__ = 'Administrator'
#!/usr/bin/python3
# coding:utf-8

# import requests
import json
import re
import random
headers={
         "Host": "****",
         "Connection":" keep-alive",
         "Content-Length": "129",
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
         "Origin":" https://sso-test.regs.com",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
         "Content-Type": "application/x-www-form-urlencoded",
         "Referer: https":"//******4.0.0/login?service=http%3A%2F%2Fo-cstar-test.regs.com%2F",
         "Accept-Encoding": "gzip, deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
         }
#定义登陆类
class regs_login():

   #用户登陆
   def huozhu_login(self):

      try:

         print ("----------------------------------------------------->>>>>>>>>")

         arg = {"username":"***","password":"12***"}

         r = requests.post("http://******com/api/login/user",data=json.dumps(arg),headers=headers)

         #print("测试结果：耗时",r.elapsed.microseconds/1000000,r.text)

         #将字符串转化为json格式
         s=json.loads(r.text)

         s1=s

         #print(s1["data"]["accessToken"])
         #获取Authorization验证码
         ccc="Bearer "+s1["data"]["accessToken"]

         print(ccc)
         return ccc

      except:
         return "用户登陆发生异常，请核实！"

   def fh_huozhu_login(self):

      return "用户登陆接口测试"

   def pd_huozhu_login(self):

      if(regs_login().huozhu_login()!="用户登陆发生异常，请核实！"):
         print ("Pass")
         return "Pass"
      else:
         print ("false")
         return "False"
****y
# 点击工作流发起
 def chen_login(self):
     headers={
         "Accept":" text/html, */*; q=0.01",
         "Accept-Encoding": "gzip, deflate, sdch",
         "Accept-Language":" zh-CN,zh;q=0.8",
         "User-Agent":" Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
         "X-Requested-With":" XMLHttpRequest",
         "Referer: http":"//o-cstar-test.regs.com/index",
         "Connection":" keep-alive",
         "Host": "o-cstar-test.regs.com",
         }
    try:

         print ("----------------------------------------------------->>>>>>>>>")

         arg = {"username":"***","password":"1234**","company_code":"LF002"}

         r = requests.post("http://***gfresh.com/api/login/user",data=json.dumps(arg),headers=headers)

         #print("测试结果：耗时",r.elapsed.microseconds/1000000,r.text)

         #将字符串转化为json格式
         s=json.loads(r.text)

         s1=s

         #print(s1["data"]["accessToken"])
         #获取Authorization验证码
         ccc="Bearer "+s1["data"]["accessToken"]

         print(ccc)
         return ccc

      except:

         return "点击工作流发起发生异常，请核实！"

   def fh_chengyunshang_login(self):

      return "工作流发起接口测试"

   def pd_chengyunshang_login(self):

      if(regs_login().pd_chengyunshang_login!="工作流发起发生异常，请核实！"):
         print ("Pass")
         return "Pass"
      else:
         print ("false")
         return "False"

if __name__=='__main__':

   regs_login().huozhu_login()
   regs_login().fh_huozhu_login()
   regs_login().pd_huozhu_login()
