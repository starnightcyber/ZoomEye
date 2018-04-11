# ZoomEye

A script used to get data from ZoomEye, a special search engine to search devices connected to network(https://www.zoomeye.org/)
just like Shodan(https://www.shodan.io/)</br>
这个脚本用来从ZoomEye API获取相关查询的数据，ZoomEye和Shodan一样可以查询连网设备。</br>


## getZoomEyeIpList.py(python 2.7)
This script gets 'ip and port'(default) that you search from ZoomEye, which needs to provide a access_token. So, the first time
you run this script, your need to provide your account and password registered to ZoomEye to create such a access_token.</br>
这个脚本中默认只获取ip和port,可以通过简单的修改来获取想要的数据,访问ZoomEye API需要提供一个access_token, 在运行这个脚本需要使用在ZoomEye注册的用户名和密码，这样会自动生成这个access_token.</br>

Then, input your query(weblogic in this sample), and start page(1) till end page(3). You will get about 30 items save to file.<br>
然后输入你要想查询的东西，比如说例中的weblogic, 查询起始页和页数，程序会自动解析从ZoomEye返回的json数据，将ip和port保存在文本中。</br>
</br>

### Sample
      starnight:ZoomEye starnight$ python getZoomEyeIpList.py
      [-] info : access_token file is not exist, please login
      [-] input : username :zl15@foxmail.com
      [-] input : password :liu120808
      [*] please input search string : weblogic
      [*] please input start page : 1
      [*] please input number of pages you want to retrieve : 3
      https://api.zoomeye.org/host/search?query=weblogic&page=1
      73.248.137.190 : 7001
      122.115.55.11 : 8000
      85.133.173.4 : 9981
      85.133.173.4 : 33
      59.44.219.156 : 8088
      59.44.25.90 : 8088
      59.151.126.80 : 8088
      59.37.62.178 : 8088
      59.56.27.32 : 8088
      59.33.252.254 : 8088
      85.133.173.4 : 40000
      66.161.251.178 : 8081
      66.96.203.251 : 8081
      66.161.251.186 : 8081
      66.161.251.183 : 8081
      151.80.118.234 : 7002
      114.251.203.84 : 32770
      114.251.203.84 : 9981
      128.184.32.124 : 80
      128.136.195.242 : 80
      [-] info : count 10

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
