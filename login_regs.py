
__author__ = 'Administrator'
#!/usr/bin/python3
# coding:utf-8

# import requests
import json
import re
import random
headers={
         "Host": "*****.com",
         "Connection":" keep-alive",
         "Content-Length": "129",
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
         "Origin":" https://sso-test.regs.com",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
         "Content-Type": "application/x-www-form-urlencoded",
         "Referer: https":"//******",
         "Accept-Encoding": "gzip, deflate",
         "Accept-Language": "zh-CN,zh;q=0.9",
         }
#定义登陆类
class regs_login():

   #用户登陆
   def huozhu_login(self):

      try:

         print ("----------------------------------------------------->>>>>>>>>")

         arg = {"username":"guoyy1","password":"123qwe"}

         r = requests.post("url",data=json.dumps(arg),headers=headers)

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