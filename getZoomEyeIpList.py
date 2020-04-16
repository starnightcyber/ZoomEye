# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : starnight_cyber
# Time: 2020-04-15
# Email: starnight_cyber@foxmail.com
# Github: https://github.com/starnightcyber/
# Refer: https://github.com/Xyntax/POC-T/blob/2.0/lib/api/zoomeye/

import os
import requests
import json
import time


class ZoomEye(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        self.access_token = ''
        # self.zoomeye_login_api = "https://api.zoomeye.org/user/login"
        # self.zoomeye_dork_api = "https://api.zoomeye.org/{}/search"

        self.ip_port_list = []

        self.load_access_token()

    def load_access_token(self):
        if not os.path.isfile('access_token.txt'):
            print('[-] info : access_token file is not exist, please login first...')
            self.login()
        else:
            with open('access_token.txt', 'r') as fr:
                self.access_token = fr.read()

    def save_access_token(self):
        with open('access_token.txt', 'w') as fw:
            fw.write(self.access_token)

    def login(self):
        """
        Prompt to input account name and password
        :return: None
        """
        self.username = input('[-] input : username :').strip()
        self.password = input('[-] input : password :').strip()
        print('[*] try to login ...')
        data = {
            'username': self.username,
            'password': self.password
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

        # dumps 将 python 对象转换成 json 字符串
        data_encoded = json.dumps(data)
        try:
            resp = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded, headers=headers)
            # loads() 将 json 字符串转换成 python 对象
            r_decoded = json.loads(resp.text)

            # 获取到账户的access_token
            access_token = r_decoded['access_token']
            self.access_token = access_token
            self.save_access_token()
        except:
            print('[-] info : username or password is wrong, please try again ')
            exit()

    def search(self):

        if not self.access_token:
            self.login()

        # 将 token 格式化并添加到 HTTP Header 中
        headers = {
            'Authorization': 'JWT ' + self.access_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

        # 要搜索的字符串  query = 'port:80 weblogic country:China'
        query = input('[*] please input search string : ')

        # 设置获取结果的起始页面,对于量比较大的时候比较有用
        page = int(input('[*] please input start page : '))

        # 设置获取的结果页数
        num = int(input('[*] please input number of pages you want to retrieve : '))

        index = 0
        while True:
            try:
                # 将查询字符串和页数结合在一起构造URL
                if index == num:
                    break
                msg = '[{}/{}] fetch page: {}'.format(index+1, num, page)
                print(msg)

                api = 'https://api.zoomeye.org/host/search'
                # searchurl = '{}{}&page={}'.format(api, query, page)
                print('query==>', query)

                # 用于获取下一页的结果
                page += 1
                index += 1

                resp = requests.get(api, headers=headers, params={"query": query, "page": page})
                r_decoded = json.loads(resp.text)
                for x in r_decoded['matches']:
                    print(x['ip'], ':', x['portinfo']['port'])
                    self.ip_port_list.append(x['ip'] + ':' + str(x['portinfo']['port']))
            except Exception as e:
                # 若搜索请求超过 API 允许的最大条目限制 或者 全部搜索结束，则终止请求
                if str(e) == 'matches':
                    print('[-] info : account was break, excceeding the max limitations')
                    break
                else:
                    print('[-] info : ', str(e))
        self.save_result()
        pass

    def save_result(self):
        # 以当前运行脚本的时间创建文件,这样就可以保证脚本运行时创建的文件不会重名
        xtime = time.strftime("[%Y-%m-%d][%H.%M.%S]")
        ip_port_list_file = '{}.txt'.format(xtime)

        #  将ip:port写入文件中
        with open(ip_port_list_file, 'w') as fw:
            for line in self.ip_port_list:
                fw.write(line + '\n')
        pass


if __name__ == '__main__':
    zoomeye = ZoomEye()
    zoomeye.search()
    pass
