# -*- coding: utf-8 -*-
# author: starnight_cyber@foxmail.com
# Time : 2016.12.8

import time
import re
import os

# 保存url, ip, ip:port
url_list = []
ip_port_list = []
ip_list = []


def getIpFromLocalFile():
    # 输出提示: 输入保存要解析的文件夹
    dir = raw_input('[*] please input the directory name : ')
    # 依次枚举文件夹中的文件
    for html in os.listdir(dir):
        print '[-] reading data from file %s ... ' % html

        # 匹配文件中包含的ip地址
        all = re.findall('href="http://.*?" data-hint', open(dir + '/' + html, 'r').read())

        # 输出匹配到的数量
        print len(all)

        for line in all:
            # 截取url href="http://120.24.13.81:7001/" data-hint
            url_start = line.find('http')
            url_end = line.find('data') - 2
            url = line[url_start:url_end]
            url_list.append(url)
            print url

        print '----------------------------'

        for line in all:
            # 截取ip href="http://120.24.13.81:7001/" data-hint
            ip_start = line.find('http') + 7
            ip_end = line.rfind('/')
            ip = line[ip_start:ip_end]
            ip_port_list.append(ip)
            # 如果是80端口的话,默认是不显示端口的,需要进行一些简单的处理
            if ':' in ip:
                ip_list.append(ip[:ip.find(':')])
            else:
                ip_list.append(ip)
            print ip[:ip.find(':')]


def saveListToFiles():
    '''
    :param ip_list: 使用ZoomEye接口获得的ip列表
    : 会写入到多个文件,保存格式不同,仅ip和 http://ip/console/login/LoginForm.jsp
    : 如http://162.105.205.162/console/login/LoginForm.jsp
    :return:
    '''

    # 以当前运行脚本的时间创建文件,这样就可以保证脚本运行时创建的文件不会重名
    xtime = time.strftime("%Y-%m-%d[%H.%M.%S]")
    ip_list_file = open(xtime + 'ip.txt', 'w')
    ip_port_list_file = open(xtime + 'ip:port.txt', 'w')
    url_list_file = open(xtime + 'url.txt', 'w')

    # 将list以一定格式写入到文件中
    # 写入url
    for line in url_list:
        url_list_file.write(line + 'console/login/LoginForm.jsp' + '\n')

    # 写入ip
    for line in ip_list:
        ip_list_file.write(line + '\n')

    # 写入ip:port
    for line in ip_port_list:
        ip_port_list_file.write(line + '\n')

    # 关闭文件
    ip_list_file.close()
    ip_port_list_file.close()
    url_list_file.close()


def main():

    # 调用函数读取页面中包含的ip, url
    getIpFromLocalFile()

    # 写入到文件中
    saveListToFiles()


if __name__ == '__main__':
    main()
