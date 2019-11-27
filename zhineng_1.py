#!/usr/bin/python3
# coding:utf-8

import requests
import json
import re
import random
headers={
         "Host": "10.1**",
         "Connection": "keep-alive",
         "Content-Length": "72",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "****",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
         "Referer": "http://t**",
         "Accept-Encoding": "gzip, deflate",
         "Accept-Language": "zh-CN,zh;q=0.9"
         }


# 定义登陆类
class zhineng_login():

    # 职能登陆
    def admin_zhineng_login(self):

        try:

            print("----------------------------------------------------->>>>>>>>>")

            url = "http://10.10.101.96:8080/sys/login"

            arg = {"loginName":"18352222222","password":"22223","code":"","rememberMe":0}

            r = requests.post(url, data=json.dumps(arg), headers=headers)

            #print("测试结果：耗时",r.elapsed.microseconds/1000000,r.text)
            # 将字符串转化为json格式
            s = json.loads(r.text)

            s1 = s
            token=r.headers['x-auth-token']
            print(token)

            #print(s["data"]["accessToken"])
            # 获取Authorization验证码
            #ccc = "Bearer " + s1["data"]["accessToken"]

            #print(ccc)
            return token

        except:
            return "用户登陆发生异常，请核实！"

    def zn_yonghu_login(self):

        return "用户登陆接口测试"

    def zn_yonghu_1_login(self):

        if (zhineng_login().admin_zhineng_login()!= "用户登陆发生异常，请核实！"):
            print("Pass")
            return "Pass"
        else:
            print("false")
            return "False"


if __name__ == '__main__':
    zhineng_login().admin_zhineng_login()
    zhineng_login().zn_yonghu_login()
    zhineng_login().zn_yonghu_1_login()
