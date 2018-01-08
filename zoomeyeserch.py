#!/usr/bin/python
# encoding: utf-8
import requests as req
import json
import optparse
import time
import sys
import os

class ZoomEye:

    def __init__(self):
        self.initParameter()
        username = 'your-email-address'
        password = 'your-password'
        self.account = {'username': username,'password': password}
        self.headers = {'Authorization': 'JWT ' + self.getToken()}

    def search(self):
        self.isFIle(self.options.file)
        queryType = self.options.type
        queryStr = self.options.query
        try:
            result = req.get('https://api.zoomeye.org/'+ queryType + '/search?query=' + queryStr + '&page=1', \
                    headers=self.headers, timeout = 15)
        except:
            print "Error exit..."
            sys.exit()
        if result.status_code != 200:
            print "error: ",
            print result.content
            print "exit..."
            sys.exit()
        resultDict = json.loads(result.content)
        # print result.content #获取第一页的所有结果
        pages = self.getPageNum(int(resultDict['total']))
        print 'There are %d pages to fetch' % pages

        userAgent = {'user-agent': 'Mozilla/5.0（iPad; U; CPU OS 3_2_1 like Mac OS X; en-us）AppleWebKit/\
            531.21.10（KHTML, like Gecko）Mobile/7B405'}
        self.headers['user-agent'] = userAgent

        start = time.time()
        starPage = 0
        for i in xrange(starPage, pages, 1):
            targetList = []
            try:
                result = req.get('https://api.zoomeye.org/' + queryType +'/search?query='+ queryStr +'&page='+\
                    str(i+1), headers=self.headers, timeout=15)
                # print "Get page " + str(i+1) + " info ..."
                now = time.time()
                print '[ %d / %d ] ==> time elapse %s s ...' % (i, pages, int(now - start))
            except:
                print "Page " + str(i) + " ,  Error exit..."
                # sys.exit()
                continue
            if result.status_code != 200:
                print "error: ",
                print result.content
                print "exit..."
                sys.exit()
                # print result.content #每页的结果
            self.getFileContent(targetList, result.content)
            self.writeTofile(self.options.file, targetList)
        print "The result in " + self.options.file

    def getFileContent(self, targetList, result):
        result = json.loads(result)
        # print result
        if self.options.type == 'web':
            for eachResult in result['matches']:
                # print eachResult
                # 获取目标站点
                targetList.append(eachResult['site'])
            print targetList
            return targetList
        for eachResult in result['matches']:
            # targetList.append(eachResult['ip'] + ':' + str(eachResult['portinfo']['port']))
            ip_port = eachResult['ip'] + ':' + str(eachResult['portinfo']['port'])
            print ip_port
            targetList.append(ip_port)
        return targetList

    def getPageNum(self, total):
        if total == 0:
            print "No result, exit.."
            sys.exit()
        page = total/10
        if total%10 == 0:
            return page
        return page + 1

    def getToken(self):
        token = req.post('https://api.zoomeye.org/user/login',json.dumps(self.account)).content
        print token
        return json.loads(token)['access_token']

    def writeTofile(self, filename, targetList):
        with open(filename, 'a') as f:
            for eachTarget in targetList:
                f.write(eachTarget + "\n")
                time.sleep(0.2)

    def isFIle(self,filename):
        if not os.path.isfile(filename):
            return
        print 'result file is exists, continue ?',
        choice = raw_input("(y/n): ")
        if choice.lower() == 'n':
            print 'Please rename filename, exit ...'
            sys.exit()
        if choice.lower() == 'y':
            return
        else:
            return self.isFIle(filename)

    def initParameter(self):
        usage = '''
         _____                     _____
        |__  /___   ___  _ __ ___ | ____|   _  ___
          / // _ \ / _ \| '_ ` _ \|  _|| | | |/ _
         / /| (_) | (_) | | | | | | |__| |_| |  __/
        /____\___/ \___/|_| |_| |_|_____\__, |\___|
                                        |___/
            '''
        parser = optparse.OptionParser(usage = usage)
        parser.add_option("-t", "--type",
                          default='web',
                          help='''Search type like host ,web  (e.g. "https://api.zoomeye.org/host/\
                                  search?query=port:21")''')

        parser.add_option("-q", "--query",
                          help="What you search is your need")

        parser.add_option("-f", "--file",
                          help="The file will save result's IP or domain")

        (self.options, args) = parser.parse_args()
        if self.options.query == None or self.options.file == None:
            print parser.print_help()
            print "Please Completed  parameters, you can show -h to get help"
            sys.exit()
        else:
            print usage


if __name__ == '__main__':
    ZE = ZoomEye()
    try:
        ZE.search()
    except KeyboardInterrupt:
        print "Ctrl + C exit..."
        sys.exit()
