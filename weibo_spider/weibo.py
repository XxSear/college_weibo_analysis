#!/usr/bin/env
# coding:utf-8
"""
Created on 2018/10/12 21:25

base Info
"""
__author__ = 'ker'
__version__ = '1.0'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import conf
import pickle
import time
import pandas as pd
import numpy as np

class Weibo():
    def __init__(self):
        self.location = ''
        self.sava_file_xpath = ''

        if conf.explorer_display:
            self.driver = webdriver.Chrome()
            self.driver.set_window_size(conf.window_size_width, conf.window_size_hight)
        else:

            #关闭图片加载
            service_args = []
            service_args.append('--load-images=no')  ##关闭图片加载
            service_args.append('--disk-cache=yes')  ##开启缓存
            service_args.append('--ignore-ssl-errors=true')  ##忽略https错误

            #设置user-agent
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap['phantomjs.page.settings.userAgent'] = (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            )
            dcap['browserName'] = 'chrome'
            self.driver = webdriver.PhantomJS(service_args=service_args, desired_capabilities=dcap)

    # 切换到新的窗口
    def switch_new_window(self, url):
        self.before_window_handles.append(self.driver.current_window_handle)
        js = 'window.open("' + url + '");'
        self.driver.execute_script(js)  # 使用js打开新窗口
        topic_handle = self.driver.window_handles[-1]
        self.driver.switch_to_window(topic_handle)  # 切换至最新的窗口
        print("window swtich to ", self.driver.current_window_handle.title())

    # 返回到之前的窗口
    def return_before_window(self):
        # 堆栈中的句柄存在 且 栈顶的句柄还在浏览器中
        if len(self.before_window_handles) == 0 or (self.driver.window_handles[-1] not in self.driver.window_handles):
            print("window handle worried,  cannot switch windows")
        else:
            # 返回栈顶所指的窗口，然后出栈
            self.driver.close()
            self.driver.switch_to_window(self.before_window_handles[-1])
            self.before_window_handles.pop()
            print("window return to", self.driver.current_window_handle.title())

    # 从xpath对应的dom元素中获取文字信息
    def get_text_by_xpath(self, xpath, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        text = None
        try:
            text = ori_dom.find_element_by_xpath(xpath).text
        except:
            print('error get text from ', xpath)
        return text

    # 从xpath对应的dom元素中获取src
    def get_src_by_xpath(self, xpath, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        src = None
        try:
            src = ori_dom.find_element_by_xpath(xpath).get_attribute('src')
        except:
            print('error get scr from ', xpath)
        return src

    def get_href_by_xpath(self, xpath, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        href = None
        try:
            href = ori_dom.find_element_by_xpath(xpath).get_attribute('href')
        except:
            print('error get href from ', xpath)
        return href

    def get_attr_by_xpath(self, xpath, attribute_name, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        attribute = None
        try:
            attribute = ori_dom.find_element_by_xpath(xpath).get_attribute(attribute_name)
        except:
            print('error get attribute from ', xpath, attribute_name)
        return attribute

    def get_doms_by_xpath(self, xpath, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        doms = None
        try:
            doms = ori_dom.find_elements_by_xpath(xpath)
        except:
            print("error get doms by ", xpath)
        return doms

    def get_dom_by_xpath(self, xpath, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        dom = None
        try:
            dom = ori_dom.find_element_by_xpath(xpath)
        except:
            print("error get doms by ", xpath)
        return dom

    def get_doms_by_class_name(self, classname, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        doms = None
        try:
            doms = ori_dom.find_elements_by_class_name(classname)
        except:
            print("error get doms by classname: ", classname)
        return doms

    def get_dom_by_class_name(self, classname, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        dom = None
        try:
            dom = ori_dom.find_element_by_class_name(classname)
        except:
            print("error get doms by classname: ", classname)
        return dom

    def get_text_by_class_name(self, classname, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        text = ''
        try:
            text = ori_dom.find_element_by_class_name(classname).text
        except:
            print("error get text by classname: ", classname)
        return text

        # def get_attr_by_xpath_from_dom(self, dom, xpath, attribute_name):

    #     attribute = None
    #     try:
    #         attribute = dom.find_elements_by_xpath(xpath).get_attribute(attribute_name)
    #     except:
    #         print("error get ",attribute_name," by ",xpath," from ",dom)
    #     return attribute

    def get_attr_by_class_name(self, class_name, attribute_name, ori_dom=None):
        if ori_dom == None:
            ori_dom = self.driver
        attribute = None
        try:
            attribute = ori_dom.find_element_by_class_name(class_name).get_property(attribute_name)
        except:
            print("error get attr by classname: ", class_name, "attr is ", attribute_name)
        return attribute

    # def get_all_attr(self, attribute_name, ori_dom=None):
    #     if ori_dom == None:
    #         ori_dom = self.driver
    #     attribute = []
    #     try:
    #
    #
    #     except:
    #         print("error get all attr : ", patter, "attr is ", attribute_name)
    #     return attribute

    def load_position_url(self, url, location):
        self.url = url
        self.location = location
        self.sava_file_xpath = 'data/'+str(time.time())+location+'.csv'

        self.driver.get('https://weibo.com')
        time.sleep(conf.intervals_time)
        cookies = pickle.load(open("cookies.ini", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(url)
        time.sleep(conf.intervals_time + np.random.randint(1,5,1)[0])
        self.crawl_data()

    def swipe_down(self):
        # js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # self.driver.execute_script(js)

    def crawl_data(self, page_num = 1):
        data_list_div_xpath = '//*[@id="Pl_Third_App__17"]/div/div/div[3]'
        #      //*[@id="Pl_Third_App__17"]/div/div/div[3]

        #     //*[@id="Pl_Third_App__17"]/div/div/div[3]

        # 往下滑动，将整个页面加载完全
        count = 0
        while count < 5:
            count += 1
            self.swipe_down()
            time.sleep(conf.intervals_time)

        # 检索出 所有发表的微博
        data_list_div = self.get_dom_by_xpath(data_list_div_xpath)
        select_xpath = ".//div[@action-type='feed_list_item']"
        list_item = self.get_doms_by_xpath(select_xpath, ori_dom=data_list_div)

        print("items = ", len(list_item))
        item_list = []
        for item in list_item:
            item_data = self.select_info_from_item(item)
            item_list.append(item_data)

        self.save_item_list_to_csv(item_list, page_num)
        # get next page
        # next page   //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[17]/div[16]/div/a[2]
        #             //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[15]/div[13]/div/a
        #             //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[17]/div[16]/div/a
        #w_page       //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[17]/div[16]/div
        #             //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[17]/div[16]/div/a
        #             //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[17]/div[16]/div/a[2]
        # w_page = self.get_dom_by_class_name('W_pages')
        # if page_num == 1:
        #     next_page_button = self.get_dom_by_xpath('.//a',ori_dom=w_page)
        # else:
        #     next_page_button = self.get_dom_by_xpath('.//a[2]', ori_dom=w_page)
        #
        # print('button', next_page_button.text, next_page_button.tag_name)
        #
        # actions = ActionChains(self.driver)
        # actions.move_to_element(next_page_button)
        # actions.click()
        # actions.perform()



        next_page_url = self.url + '?current_page='+ str(3 * page_num)+'&since_id=&page='+str(page_num+1)+'#feedtop'
        self.driver.get(next_page_url)
        time.sleep(conf.next_page_intervals)
        self.crawl_data(page_num=page_num+1)
        if page_num == 1:
            time.sleep(20) # 手动输入吧


    # 摘取信息 存入数据库
    def select_info_from_item(self, item):
        # ltem     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1]
        # comment  //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[2]/div/ul/li[3]/a/span/span
        # like     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[2]/div/ul/li[4]/a/span/span
        # name     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[1]/a[1]
        # title    //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[1]/a[2]
        # time     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[2]/a[1]
        # device   //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[2]/a[2]
        # text     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[4]
        # media    //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[1] /div[1]/div[4]/div[5]/div
        # link     //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[4] /div[1]/div[3]/div[4]/a[4]
        #          //*[@id="Pl_Third_App__17"]/div/div/div[3]/div[4] /div[1]/div[3]/div[4]/a[3]

        comment_num = self.get_text_by_xpath(".//span[@node-type='comment_btn_text']", ori_dom=item)
        like_num = self.get_text_by_xpath(".//span[@node-type='like_status']", ori_dom=item)

        name = self.get_text_by_class_name('WB_info', ori_dom=item)
        user_card = self.get_attr_by_xpath('.//a[@usercard]', attribute_name='usercard', ori_dom=item)
        wb_info_div = self.get_dom_by_class_name('WB_info', ori_dom=item)
        # wb_info_div 第一个<a>为名字  之后的为标签  title 可能存在于 a i 中
        titles = []
        for dom in self.get_doms_by_xpath('.//a|i[@title]', ori_dom=wb_info_div):
            titles.append( dom.get_attribute('title') )


        time = self.get_attr_by_xpath(".//a[@node-type='feed_list_item_date']", attribute_name='title', ori_dom=item)
        device = self.get_text_by_xpath(".//a[@action-type='app_source']", ori_dom=item)

        text = self.get_text_by_xpath('.//div[@node-type="feed_list_content"]', ori_dom=item)
        media_div = self.get_text_by_xpath('.//div[@node-type="feed_list_media_prev"]', ori_dom=item)

        pic_num = 0
        video = False
        if self.get_doms_by_xpath('.//li[@action-type="fl_pics"]',ori_dom=item):
            pic_num =  len(self.get_doms_by_xpath('.//li[@action-type="fl_pics"]',  ori_dom=item))
        elif self.get_doms_by_xpath('.//li[@action-type="feed_list_media_img"]', ori_dom=item):
            pic_num = 1

        if self.get_doms_by_xpath('.//video', ori_dom=item):
            video = True


        # print(comment_num, "  ",like_num,"  ", name,' ', titles, " ",user_card, ' ', time, ' ',device)
        # print('text = ',text, ' ',pic_num, " ", video, " ", self.location)
        item_data = [name, user_card, titles, comment_num, like_num, time, device, text, pic_num, video]
        return item_data
        # self.add_item_to_pd(item_data)

        # pass
    def save_item_list_to_csv(self, item_list, num):
        self.data_df = pd.DataFrame(
            columns=['name', 'user_card', 'titles', 'comment_num', 'comment_num', 'time', 'device', 'text', 'pic_num',
                     'video'])
        for i in range(len(item_list)):
            self.data_df.loc[i] = item_list[i]

        if num == 1:
            self.data_df.to_csv(self.sava_file_xpath,   header=True)
        else:
            self.data_df.to_csv(self.sava_file_xpath, mode='a', header=False)
        print('finish save item in page ', num, " in ",self.sava_file_xpath)


if __name__ == '__main__':
    weibo = Weibo()
    university = 'BTBU_jh'
    weibo.load_position_url(conf.dict_url[university], university)