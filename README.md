# ZoomEye
A script used to get data from ZoomEye, moved to Python3.

Legacy for Python2, please refer [ZoomEye Python2 Version](https://github.com/starnightcyber/ZoomEye/releases/tag/ZoomEye_py2)

## Sample

```
python3 getZoomEyeIpList.py
[-] info : access_token file is not exist, please login first...
[-] input : username : xxxxxxx
[-] input : password : xxxxxxx
[*] please input search string : weblogic +after:"2020-01-01" +before:"2021-01-01" +country:"CN" +service:"http"
[*] please input start page : 5
[*] please input number of pages you want to retrieve : 2
[1/2] fetch page: 5
query==> weblogic +after:"2020-01-01" +before:"2021-01-01" +country:"CN" +service:"http"
59.83.200.19 : 7210
61.155.162.146 : 5269
61.155.162.146 : 8880
123.124.155.145 : 8001
103.232.86.147 : 80
118.213.241.254 : 8081
123.124.131.199 : 8887
36.97.143.91 : 6544
59.83.200.19 : 8129
211.157.184.224 : 8002
118.26.64.28 : 2002
124.250.88.180 : 80
124.205.79.80 : 80
123.124.131.199 : 591
124.127.181.121 : 80
124.219.98.75 : 80
124.205.126.239 : 80
124.47.22.62 : 80
124.172.232.88 : 80
124.127.181.110 : 80
[2/2] fetch page: 6
query==> weblogic +after:"2020-01-01" +before:"2021-01-01" +country:"CN" +service:"http"
124.250.89.145 : 80
124.172.232.89 : 80
124.42.41.20 : 80
124.172.232.87 : 80
124.172.232.86 : 80
124.239.182.43 : 80
124.118.200.7 : 80
124.127.181.111 : 80
124.219.98.84 : 80
124.204.70.48 : 80
124.238.151.66 : 80
124.219.98.85 : 80
124.205.109.53 : 80
124.47.2.116 : 80
124.115.170.234 : 80
124.163.215.82 : 80
124.238.151.70 : 80
124.115.212.254 : 80
124.47.2.119 : 80
124.88.82.8 : 80
```
