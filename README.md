# ZoomEye-python【推荐使用】
官方更新了 [ZoomEye-python](https://github.com/knownsec/ZoomEye-python)，相比之前，提供了更加方便的查找、导出功能，而且没有获取搜索结果前30%的限制，使用体验良好。

之前还为了能获取更多的数据，还有过一些挣扎。

一些使用示例，可参考官方文档或[ZoomEye-python 使用](https://www.cnblogs.com/Hi-blog/p/zoomeye-python.html)

## zoomeye search
### 过滤查询
```
# zoomeye search "country:\"United States\" +port:\"8090\" +app:\"Atlassian Confluence\""
ip:port                  service             country             app                           banner                        
173.248.141.144:8090     http                United States       Atlassian Confluence          HTTP/1.1 302 \r\nCache-...    
63.231.117.120:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.92:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.23:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.68:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.215:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.251:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.254:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.82:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.91:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.48:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.240:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.72:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.252:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.34:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.62:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.51:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.11:8090       http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.154:8090      http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    
63.231.117.0:8090        http                United States       Atlassian Confluence          HTTP/1.1 200 \nDate: Mo...    

total: 20/971
```
### 数据导出
```
-save：可以指定相关的字段；
-num：指定数量；
```
```
# zoomeye search "country:\"United States\" +port:\"8090\" +app:\"Atlassian Confluence\"" -save ip,port,app,version,device,city,country,service -num 971
save file to /root/country_United_States_port_8090_app_Atlassian_Confluence_971_1654584890.json successful!
# cat /root/country_United_States_port_8090_app_Atlassian_Confluence_971_1654584890.json | grep ip | wc -l
971
```


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
