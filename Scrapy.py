# Author: Betterman
# -*- coding = utf-8 -*-
# @Time : 2020/8/26 21:13
# @File : Scrapy.py
# @Software : PyCharm

import requests
import re
import time

url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}


def get_dsta(url):
    for page in range(1,10):
        params = {
            'timestamp': str(time.time()),
            'keyword': 'python',  # 岗位相关
            'pageIndex': page,  # 页码
            'pageSize': '10',  # 展示数据数目
            'language': 'zh-cn',
            'area': 'cn'
        }

        response = requests.get(url,params=params,headers=headers).json()
        # response = requests.get(url,params=params,headers=headers)
        # response = response.content.decode('utf-8')
        data = response['Data']['Posts']#json读取
        # print(response)

        #posts = map(data)
        for i in data:
            #岗位名称
            RecruitPostName = i['RecruitPostName']
            print(RecruitPostName)

if __name__ == '__main__':
    get_dsta(url)

