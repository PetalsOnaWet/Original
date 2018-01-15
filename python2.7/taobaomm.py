#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Lix'

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import requests
import os

class TBMM:
    def __init__(self):
        """淘女郎爬虫类初始化函数
        """

        self.site_url = 'https://mm.taobao.com/search_tstar_model.htm'
        self.driver = webdriver.PhantomJS()
        self.sleep_time = 1
        self.save_img_path = '/Users/Lix/Documents/www/htdocs/origin/tbmm/'

    def getPage(self):
        """获取淘女郎页面HTML内容
        
        Returns:
            <soup> -- <BeautifulSoup库解析的html数据>
        """

        self.driver.get(self.site_url)
        time.sleep(self.sleep_time)
        content = self.driver.page_source.encode('utf-8')
        self.driver.quit()
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    
    def getContent(self, soup):
        """ 获取淘女郎中，列表的数据，
            包括封面图，姓名，城市，身高体重
        
        Arguments:
            soup {bp4库解析出的默认格式} -- [html数据]
        """

        items = soup.find_all(class_='item')
        for item in items:
            # print item
            print u'----分割线---'
            page_code = str(item)
            name = item.find(class_='name').text
            city = item.find(class_='city').text
            img = ''
            pattern = re.compile(r'data-ks-lazyload="(.*?)"', re.S)
            result = re.search(pattern, page_code)
            if result:
                img = 'http:' + result.group(1).strip()
            else:
                if item.img['src'] is not None:
                    img = 'http:' + item.img['src']
                else:    
                    pass
            pattern = re.compile(r'<span>(.*?)</span>', re.S)
            result = re.search(pattern, page_code)
            if result:
                height_wight = result.group(1).strip()
            else:
                print u'身高体重未找到'
            print name
            print city
            print img
            print height_wight
            self.saveImg(img, name)
            print '----------------------------------'
    
    def saveImg(self, imageURL, fileName):
        """存储图片方法
        
        Arguments:
            imageURL <string> -- 图片的url
            fileName <string> -- 用于存储的文件名
        """

        with open(self.save_img_path + fileName + '.png', 'wb') as f:
            f.write(requests.get(imageURL).content)

    def mkdir(self, path):
        # 去除路径首尾空格
        path = path.strip()
        path = path.rstrip('\\')
        isExists = os.path.exists(path)

        if not isExists:
            print path + ' 创建成功'
            os.makedirs(path)
            return True
        else:
            print path + ' 目录已存在'
            return False

    def start(self):
        """ 淘女郎爬虫类执行函数0p-oo
        """

        soup = self.getPage()
        self.getContent(soup)

tbmm = TBMM()
tbmm.start()