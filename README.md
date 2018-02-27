# ZoomEye

A script used to get data from ZoomEye, a special search engine to search devices connected to network(https://www.zoomeye.org/)
just like Shodan(https://www.shodan.io/)</br>
这个脚本用来从ZoomEye API获取相关查询的数据，ZoomEye和Shodan一样可以查询连网设备。</br>

## zoomeyeserch.py (python 2.7)
zoomeye script update at 2018.1.8 to adapt to new version of zoomeye.

please use this script first, other scripts remained untested and may be outdated.

if you find the script not works fine, please try to use getZoomEyeIpList.py and tell me, your system version.

### Sample
    starnight:New_ZoomEye starnight$ python zoomeyeserch.py -t host -q weblogic -f weblogic-result.txt 

         _____                     _____
        |__  /___   ___  _ __ ___ | ____|   _  ___
          / // _ \ / _ \| '_ ` _ \|  _|| | | |/ _
         / /| (_) | (_) | | | | | | |__| |_| |  __/
        /____\___/ \___/|_| |_| |_|_____\__, |\___|
                                        |___/
            
    {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6InN0YXJuaWdodF9jeWJlckBmb3htYWlsLmNvbSIsImlhdCI6MTUxNTM4MDIyMywibmJmIjoxNTE1MzgwMjIzLCJleHAiOjE1MTU0MjM0MjN9.3uDMMEuVCWvL8GSB6ZmUxJk7sZaE7JgNXZL8YnB2D60"}
    There are 6148 pages to fetch
    [ 0 / 6148 ] ==> time elapse 0 s ...
    180.163.112.102:8002
    180.67.130.71:8002
    125.76.237.6:8080
    125.35.11.61:8080
    125.95.12.62:8080
    122.56.80.181:443
    122.216.209.69:443
    122.226.61.178:443
    122.13.163.116:443
    122.96.60.36:443
    122.224.69.189:443
    122.155.204.34:443
    122.112.15.3:443
    122.224.69.187:443
    122.224.251.239:443
    122.155.204.19:443
    122.155.204.18:443
    122.224.64.135:443
    122.144.168.84:443
    122.155.204.20:443



## getZoomEyeIpList.py(python 2.7)
This script gets 'ip and port'(default) that you search from ZoomEye, which needs to provide a access_token. So, the first time 
you run this script, your need to provide your account and password registered to ZoomEye to create such a access_token.</br>
这个脚本中默认只获取ip和port,可以通过简单的修改来获取想要的数据,访问ZoomEye API需要提供一个access_token, 在运行这个脚本需要使用在ZoomEye注册的用户名和密码，这样会自动生成这个access_token.</br>

Then, input your query(weblogic in this sample), and start page(1) till end page(3). You will get about 30 items save to file.<br>
然后输入你要想查询的东西，比如说例中的weblogic, 查询起始页和页数，程序会自动解析从ZoomEye返回的json数据，将ip和port保存在文本中。</br>
</br>

### Sample
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</br>
[-] info : access_token file is not exist, please login </br>
[-] input : username :[your email account]</br>
[-] input : password :[your password]</br>
[\*] please input search string : weblogic</br>
[\*] please input start page : 1</br>
[\*] please input number of pages you want to retrieve : 3</br>
https://api.zoomeye.org/host/search?query=weblogic&page=1</br>
115.112.99.254 8010</br>
115.85.207.196 8008</br>
110.249.133.214 79</br>
115.233.221.139 8007</br>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</br>
</br>

## extract_local_html.py
【更新:2018.1.8】

从ZoomEye API获取搜索结果是有限制的，只能获取到前百分之多少，但是如果我们在浏览器端细化查询语句，即更精确的匹配查找，其结果数量可能会少于2000条，而用浏览器最多可以看到100页查询结果，每页20条数据。通过手工保存页面再提取的方式，我们就能将这一细化后的查询结果全部收集起来。

### About This Script
author  : evilclay </br>
http://www.cnblogs.com/anka9080/p/ZoomEyeAPI.html</br>
------- Modified by -------</br>
starnight_cyber@foxmail.com</br>
Time : 2016.12.8/2017.7.17</br>
</br>

Last but not least, I should not provide this access_token file, it was create by my user account, it is just for your test. </br>
最后，我提供的一个access_token的文件仅用来测试,你可以用自己的账号生成。</br>
