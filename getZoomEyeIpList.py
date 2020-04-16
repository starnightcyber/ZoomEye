# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : starnight_cyber
# Time: 2020-04-15
# Email: starnight_cyber@foxmail.com

import os
import requests
import json
import time
from random import randint

access_token = ''
ip_list = []
ip_port_list = []
query = ''

# Random UA since its required
def getRandomUserAgent():
    user_agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                   "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
                   "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    return user_agents[randint(0, len(user_agents) - 1)]

headers = getRandomUserAgent()


def login():
    """
    Prompt to input account name and password
    :return: None
    """
    user = input('[-] input : username :')
    passwd = input('[-] input : password :')
    data = {
        'username': user,
        'password': passwd
    }

    # dumps 将 python 对象转换成 json 字符串
    data_encoded = json.dumps(data)
    try:
        r = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded, headers=headers)
        # loads() 将 json 字符串转换成 python 对象
        r_decoded = json.loads(r.text)
        global access_token

        # 获取到账户的access_token
        access_token = r_decoded['access_token']
    except:
        print('[-] info : username or password is wrong, please try again ')
        exit()


def saveStrToFile(file, str):
    """
    将access_token写入文件中
    :param file: 文件名
    :param str: 将access_token写入文件中
    :return: None
    """
    with open(file, 'w') as fw:
        fw.write(str)


def saveListToFiles():
    """
    # 将获取到的ip:port地址保存到文件中
    :return: None
    """
    # 以当前运行脚本的时间创建文件,这样就可以保证脚本运行时创建的文件不会重名
    global query
    xtime = time.strftime("[%Y-%m-%d][%H.%M.%S]")
    ip_port_list_file = '{}.txt'.format(xtime)

    #  将ip:port写入文件中
    with open(ip_port_list_file, 'w') as fw:
        for line in ip_port_list:
            fw.write(line + '\n')


def zoomeye():
    """
    # 从ZoomEye获取地址ip:port
    :return: None
    """

    index = 1       # 循环下标
    global access_token, query
    with open('access_token.txt', 'r') as fr:
        access_token = fr.read()

    # 将 token 格式化并添加到 HTTP Header 中
    headers = {
        'Authorization': 'JWT ' + access_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    # 要搜索的字符串  query = 'port:80 weblogic country:China'
    query = input('[*] please input search string : ')

    # 设置获取结果的起始页面,对于量比较大的时候比较有用
    page = int(input('[*] please input start page : '))

    # 设置获取的结果页数
    num = int(input('[*] please input number of pages you want to retrieve : '))

    while True:
        try:
            # 将查询字符串和页数结合在一起构造URL
            if index == num:
                break
            msg = 'index: [{}/{}], page: {}'.format(index, num, page)
            print(msg)

            api = 'https://api.zoomeye.org/host/search'
            # searchurl = '{}{}&page={}'.format(api, query, page)
            print('query==>', query)

            # 用于获取下一页的结果
            page += 1
            index += 1

            resp = requests.get(api, headers=headers, params={"query": query, "page": page})
            r_decoded = json.loads(resp.text)
            # print r_decoded
            # print r_decoded['total']
            for x in r_decoded['matches']:
                print(x['ip'], ':', x['portinfo']['port'])
                ip_list.append(x['ip'])
                ip_port_list.append(x['ip'] + ':' + str(x['portinfo']['port']))
        except Exception as e:
            # 若搜索请求超过 API 允许的最大条目限制 或者 全部搜索结束，则终止请求
            if str(e) == 'matches':
                print('[-] info : account was break, excceeding the max limitations')
                break
            else:
                print('[-] info : ', str(e))


def main():
    # 访问口令文件不存在则进行登录操作
    if not os.path.isfile('access_token.txt'):
        print('[-] info : access_token file is not exist, please login')

        # 进行登录操作
        login()

        # 保存access_token到文件中
        saveStrToFile('access_token.txt', access_token)

    # 从ZoomEye API 获取IP地址列表
    zoomeye()

    # 将结果保存到文件中
    saveListToFiles()


if __name__ == '__main__':
    main()
