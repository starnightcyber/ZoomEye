#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/7
# @Author  : starnight_cyber
# @Github  : https://github.com/starnightcyber
# @Software: PyCharm
# @File    : zoomeye_domain.py

import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import ssl
import time
from queue import Queue
from multiprocessing import Pool, cpu_count

# Do not support ssl and disable warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
timestamp = time.strftime("%Y-%m-%d", time.localtime(time.time()))


task_queue = Queue()
process_num = cpu_count()
domains = []


def zoomeye_domain_total(domain):
    print('[*][zoomeye_domain_total] ...')
    try:
        cmd = "zoomeye domain " + domain + " 1 | tail -1 | awk -F '/' '{print $2}'"
        print('[*] {}'.format(cmd))
        total = os.popen(cmd).read().strip()
        print('[*] total => {}'.format(total))
        return int(total)
    except Exception as e:
        print(str(e))
    finally:
        pass


def setcallback(msg):
    global domains
    for line in msg:
        domains.append(line.strip())


def worker(cmd, index):
    try:
        task_queue.put(cmd)
        print('[*][page.{}] => {}'.format(index, cmd))
        result = os.popen(cmd).read().split('\n')[:-1]
        return result
    except Exception as e:
        print(str(e))
    finally:
        pass


def zoomeye_domain(domain, index):
    print('[*][{}][zoomeye_domain] fetch subdomains for {} ...'.format(index, domain))
    print('-----------------------------------------------------')
    total = zoomeye_domain_total(domain)
    pages = total // 30 + 1
    last = total % 30
    print('[*] pages => {}'.format(pages))
    for index in range(1, pages+1):
        if index != pages:
            cmd = "zoomeye domain " + domain + " 1 -page {}".format(index) + " | sed -n '2,31p' | " + \
                  "awk -F ' ' '{print $1}'"
        else:
            cmd = "zoomeye domain " + domain + " 1 -page {}".format(pages) + \
                  " | sed -n '2,{}p' | ".format(last+1) + "awk -F ' ' '{print $1}'"
        task_queue.put(cmd)
        index += 1
    print('-----------------------------------------------------')
    pool = Pool(process_num)  # 创建进程池
    index = 0
    while not task_queue.empty():
        index += 1
        task = task_queue.get(timeout=1.0)
        pool.apply_async(worker, args=(task, index), callback=setcallback)
    pool.close()
    pool.join()


def save_2_file(domain):
    print('-----------------------------------------------------')
    outfile = '{}_{}.txt'.format(timestamp, domain)
    global domains
    with open(outfile, 'w', encoding='utf-8-sig') as fw:
        for line in domains:
            fw.write(line)
            fw.write('\n')
    print('Data saved to {} ... {} sub-domains in total.'.format(outfile, len(domains)))
    print()


def run_batch():
    print('[*][run_batch] ...')
    search_domains = ['qq.com', 'baidu.com']
    index = 0
    for domain in search_domains:
        index += 1
        global domains
        domains = []
        zoomeye_domain(domain, index)
        save_2_file(domain)


def main():
    run_batch()


if __name__ == '__main__':
    main()
