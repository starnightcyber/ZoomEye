# -*- coding: utf-8 -*-
# author  : evilclay
# datetime: 20160330
# http://www.cnblogs.com/anka9080/p/ZoomEyeAPI.html
# ------- Modified by -------
# starnight_cyber@foxmail.com
# Time : 2016.12.8/2017.7.17

import os
import requests
import json
import time

access_token = ''
ip_list = []
ip_port_list = []
query = ''

def login():
    # 输入用户名密码 进行登录操作
    user = raw_input('[-] input : username :')
    passwd = raw_input('[-] input : password :')
    data = {
        'username': user,
        'password': passwd
    }

    # dumps 将 python 对象转换成 json 字符串
    data_encoded = json.dumps(data)
    try:
        r = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded)
        # loads() 将 json 字符串转换成 python 对象
        r_decoded = json.loads(r.text)
        global access_token

        # 获取到账户的access_token
        access_token = r_decoded['access_token']
    except Exception, e:
        print '[-] info : username or password is wrong, please try again '
        exit()


def saveStrToFile(file, str):
    # 将access_token写如文件中
    with open(file, 'w') as output:
        output.write(str)


def saveListToFiles():
    # 将获取到的ip:port地址保存到文件中

    # 以当前运行脚本的时间创建文件,这样就可以保证脚本运行时创建的文件不会重名
    global query
    xtime = time.strftime("[%Y-%m-%d][%H.%M.%S]")
    ip_list_file = '{}{}-ip.txt'.format(xtime, query)
    ip_port_list_file = '{}{}-ip:port.txt'.format(xtime, query)

    # 将ip写入到文件中
    with open(ip_list_file, 'w') as fw:
        for line in ip_list:
            fw.write(line + '\n')

    #  将ip:port写入文件中
    with open(ip_port_list_file, 'w') as fw:
        for line in ip_port_list:
            fw.write(line + '\n')


def zoomeye():
    # 从ZoomEye获取地址ip:port

    page = 1        # 表示第几页
    num = 1         # 页数
    index = 0       # 循环下标
    global access_token, query
    with open('access_token.txt', 'r') as input:
        access_token = input.read()

    # 将 token 格式化并添加到 HTTP Header 中
    headers = {
        'Authorization': 'JWT ' + access_token,
    }

    # 要搜索的字符串  query = 'port:80 weblogic country:China'
    query = raw_input('[*] please input search string : ')

    # 设置获取结果的起始页面,对于量比较大的时候比较有用
    page = int(raw_input('[*] please input start page : '))

    # 设置获取的结果页数
    num = int(raw_input('[*] please input number of pages you want to retrieve : '))

    while (True):
        try:
            # 将查询字符串和页数结合在一起构造URL
            if index == num:
                break
            print 'index : ' + str(index) + ' - ' + 'page : ' + str(page)
            searchurl = 'https://api.zoomeye.org/host/search?query=' + query + '&page=' + str(page)
            # 用于获取下一页的结果
            page += 1
            index += 1

            r = requests.get(url=searchurl, headers=headers)
            print searchurl
            r_decoded = json.loads(r.text)
            # print r_decoded
            # print r_decoded['total']
            for x in r_decoded['matches']:
                print x['ip'],':',x['portinfo']['port']
                ip_list.append(x['ip'])
                ip_port_list.append(x['ip'] + ':' + str(x['portinfo']['port']))
        except Exception, e:
            # 若搜索请求超过 API 允许的最大条目限制 或者 全部搜索结束，则终止请求
            if str(e.message) == 'matches':
                print '[-] info : account was break, excceeding the max limitations'
                break
            else:
                print '[-] info : ' + str(e.message)


def main():
    # 访问口令文件不存在则进行登录操作
    if not os.path.isfile('access_token.txt'):
        print '[-] info : access_token file is not exist, please login'

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
