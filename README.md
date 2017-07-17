# ZoomEye
A script used to get data from ZoomEye, a special search engine to search devices connected to network(https://www.zoomeye.org/)
just like Shodan(https://www.shodan.io/)

## getZoomEyeIpList.py
This script gets 'ip and port'(default) that you search from ZoomEye, which needs to provide a access_token. So, the first time 
you run this script, your need to provide your account and password registered to ZoomEye to create such a access_token.

Then, input your query(weblogic in this sample), and start page(1) till end page(3). You will get about 30 items save to file.

Sample
-------------------------------------------------------
 [-] info : access_token file is not exist, please login
 [-] input : username :[your email account]
 [-] input : password :[your password]
 [*] please input search string : weblogic
 [*] please input start page : 1
 [*] please input number of pages you want to retrieve : 3
 https://api.zoomeye.org/host/search?query=weblogic&page=1
 115.112.99.254 8010
 115.85.207.196 8008
 110.249.133.214 79
 115.233.221.139 8007
-------------------------------------------------------


## getLocalZoomEyeIpList.py
This script exploits more 
