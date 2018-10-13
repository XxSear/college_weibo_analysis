#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/4/23 16:02

base Info
"""
__author__ = 'xx'
__version__ = '1.0'
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import requests

# from Graduation_Project import conf
# from Graduation_Project.spider.page import Page
# from Graduation_Project.spider.content import ContentItem
# from Graduation_Project.spider import tools

import pickle

##
#17326191733----asd11069
class COOKIE():
    def __init__(self):
        self.url = 'https://s.weibo.com'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def get_cookies(self):
        print("输入账号")
        time.sleep(120)  #输入账号密码
        print("get cookies")
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open("cookies.ini", "wb"))
        print(cookies)
        return cookies


if __name__ == '__main__':
    test = COOKIE()

    test.get_cookies()


    # cookie_list = [{'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'value': 'SSL', 'name': 'cross_origin_proto', 'path': '/'}, {'secure': False, 'domain': 'weibo.com', 'httpOnly': False, 'value': '968b70b7bcdc28ac97c8130dd353b55e', 'name': 'TC-Ugrow-G0', 'path': '/'}, {'secure': False, 'domain': 'weibo.com', 'httpOnly': False, 'value': '8dc78264df14e433a87ecb460ff08bfe', 'name': 'TC-Page-G0', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'value': '7791b283063212e8b8eb1b802bfceadd', 'name': 'login_sid_t', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'value': 'passport.weibo.com', 'name': '_s_tentry', 'path': '/'}, {'secure': False, 'domain': 'weibo.com', 'httpOnly': False, 'value': '1e4d14527a0d458a29b1435fb7d41cc3', 'name': 'TC-V5-G0', 'path': '/'}, {'secure': False, 'domain': 'weibo.com', 'httpOnly': False, 'expiry': 1524472205, 'value': '96e2695964e412de|undefined', 'name': 'WBStorage', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1839831606, 'value': '501422634432.03827.1524471606902', 'name': 'SINAGLOBAL', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'value': '501422634432.03827.1524471606902', 'name': 'Apache', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1555575606, 'value': '1524471606933:1:1:1:501422634432.03827.1524471606902:', 'name': 'ULV', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1556007627.3246, 'value': '0V5lwgvyrPUqaa', 'name': 'SUHB', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1556007627.324552, 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W54XuFJYmy7PZw_S8IIXLuv5JpX5K2hUgL.Foqfe05ce0z4Son2dJLoIEjLxKMLBoBLB-zLxK.L1-eL1--LxKBLB.zL1K.LxK-LB-BL1KWXqgSXIgS0', 'name': 'SUBP', 'path': '/'}, {'secure': False, 'domain': 'weibo.com', 'httpOnly': False, 'value': '2835f82aba1b9774', 'name': 'WBtopGlobal_register_version', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': True, 'expiry': 1839831627.324488, 'value': 'ApImlayncotR28oZY1cA4M20rstI9W2MrYbOkR-hRGuPQZKOy8vJEDqcIqgm8Q8YX5T6Yhsy1bnxV2TeYkAg6PI.', 'name': 'SCF', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': True, 'value': '_2A2532ecaDeRhGeBL6FIX8yzFzTSIHXVUr1_SrDV8PUNbmtAKLVCkkW9NRzM8nFveQTUYsICbj_L0mf--379FBQ0E', 'name': 'SUB', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1525076428.324687, 'value': '1525076427', 'name': 'ALF', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'value': '1524471626', 'name': 'SSOLoginState', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1525335627, 'value': '17326191733', 'name': 'un', 'path': '/'}, {'secure': False, 'domain': '.weibo.com', 'httpOnly': False, 'expiry': 1525076428.074537, 'value': '6', 'name': 'wvr', 'path': '/'}]
    #
    # cookie_dic = {}
    # for cookie in cookie_list:
    #     if cookie['name'] and cookie['value']:
    #         cookie_dic[cookie['name']] = cookie['value']
    #     # print(cookie['name'] ,"  ", cookie['value'])
    # print( cookie_dic )


    # driver = webdriver.Chrome()
    # cookies = pickle.load(open("cookies.ini", "rb"))
    #
    #
    # driver.get('https://weibo.com')
    # for cookie in cookies:
    #     driver.add_cookie(cookie)
    # driver.get('https://weibo.com')

    # driver.refresh()
    # for i in cookie_dic:
    #     print(i, cookie_dic[i])
    #     driver.add_cookie({i,cookie_dic[i]})
    # driver.add_cookie()

    # time.sleep(20)
    # driver.quit()