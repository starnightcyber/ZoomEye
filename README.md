# ZoomEye

A script used to get data from ZoomEye, a special search engine to search devices connected to network(https://www.zoomeye.org/)
just like Shodan(https://www.shodan.io/)</br>
这个脚本用来从ZoomEye API获取相关查询的数据，ZoomEye和Shodan一样可以查询连网设备。</br>


## getZoomEyeIpList.py(python 2.7)
【更新:2018.11.2】
ZoomEye新版本会检查是否是爬虫，主要是通过检查请求的信息是否携带User-Agent

已在请求的headers中添加User-Agent，经测试，可正常工作.

【更新:2018.4.11】
This script gets 'ip and port'(default) that you search from ZoomEye, which needs to provide a access_token. So, the first time
you run this script, your need to provide your account and password registered to ZoomEye to create such a access_token.</br>
这个脚本中默认只获取ip和port,可以通过简单的修改来获取想要的数据,访问ZoomEye API需要提供一个access_token, 在运行这个脚本需要使用在ZoomEye注册的用户名和密码，这样会自动生成这个access_token.</br>

Then, input your query(weblogic in this sample), and start page(1) till end page(3). You will get about 30 items save to file.<br>
然后输入你要想查询的东西，比如说例中的weblogic, 查询起始页和页数，程序会自动解析从ZoomEye返回的json数据，将ip和port保存在文本中。</br>
</br>

### Sample
    starnight:ZoomEye starnight$ python getZoomEyeIpList.py
    [-] info : access_token file is not exist, please login
    [-] input : username :your-email-address
    [-] input : password :your-password
    [*] please input search string : weblogic
    [*] please input start page : 10
    [*] please input number of pages you want to retrieve : 2
    index : 0 - page : 10
    https://api.zoomeye.org/host/search?query=weblogic&page=10
    113.200.157.206 : 80
    113.107.226.37 : 80
    113.108.173.185 : 80
    113.196.174.27 : 80
    113.140.88.172 : 80
    113.23.243.185 : 80
    113.140.88.174 : 80
    113.59.34.5 : 80
    113.108.8.186 : 80
    113.140.1.137 : 80
    113.140.1.140 : 80
    113.107.215.24 : 80
    113.161.131.53 : 80
    113.107.215.20 : 80
    113.200.157.199 : 80
    113.23.157.137 : 80
    113.185.0.51 : 80
    113.107.215.29 : 80
    113.107.226.38 : 80
    113.185.0.232 : 80
    index : 1 - page : 11
    https://api.zoomeye.org/host/search?query=weblogic&page=11
    113.200.157.210 : 80
    113.200.115.207 : 80
    113.108.173.47 : 80
    113.161.213.208 : 80
    113.108.8.198 : 80
    113.204.231.34 : 80
    113.204.231.39 : 80
    113.200.157.216 : 80
    113.23.157.147 : 80
    113.107.54.27 : 80
    113.204.206.21 : 80
    113.185.0.60 : 80
    113.204.231.35 : 80
    113.204.231.38 : 80
    113.52.45.85 : 80
    113.240.252.22 : 80
    113.185.0.94 : 80
    113.207.5.53 : 80
    113.196.174.87 : 80
    113.107.215.26 : 80

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
