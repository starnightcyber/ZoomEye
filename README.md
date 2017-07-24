# ZoomEye

A script used to get data from ZoomEye, a special search engine to search devices connected to network(https://www.zoomeye.org/)
just like Shodan(https://www.shodan.io/)
这个脚本用来从ZoomEye API获取相关查询的数据，ZoomEye和Shodan一样可以查询连网设备。</br>

## getZoomEyeIpList.py
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


### About This Script
author  : evilclay </br>
http://www.cnblogs.com/anka9080/p/ZoomEyeAPI.html</br>
------- Modified by -------</br>
starnight_cyber@foxmail.com</br>
Time : 2016.12.8/2017.7.17</br>
</br>

Last but not least, I should not provide this access_token file, it was create by my user account, it is just for your test. </br>
最后，我提供的一个access_token的文件仅用来测试,你可以用自己的账号生成。</br>
