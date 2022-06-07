# 【2022.6.7】ZoomEye-python【推荐使用】
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

# 【2022.6.7】zoomeye_domain_parallel.py
使用 ZoomEye domain 接口获取域名数据
```
# python3 zoomeye_domain_parallel.py 
[*][run_batch] ...
[*][1][zoomeye_domain] fetch subdomains for baidu.com ...
-----------------------------------------------------
[*][zoomeye_domain_total] ...
[*] zoomeye domain baidu.com 1 | tail -1 | awk -F '/' '{print $2}'
[*] total => 6536
[*] pages => 218
-----------------------------------------------------
[*][page.1] => zoomeye domain baidu.com 1 -page 1 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.2] => zoomeye domain baidu.com 1 -page 2 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.3] => zoomeye domain baidu.com 1 -page 3 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.4] => zoomeye domain baidu.com 1 -page 4 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.5] => zoomeye domain baidu.com 1 -page 5 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.6] => zoomeye domain baidu.com 1 -page 6 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.7] => zoomeye domain baidu.com 1 -page 7 | sed -n '2,31p' | awk -F ' ' '{print $1}'
[*][page.8] => zoomeye domain baidu.com 1 -page 8 | sed -n '2,31p' | awk -F ' ' '{print $1}'
... 略略略
[*][page.218] => zoomeye domain baidu.com 1 -page 218 | sed -n '2,27p' | awk -F ' ' '{print $1}'
-----------------------------------------------------
Data saved to 2022-06-07_baidu.com.txt ... 6536 sub-domains in total.
```
测试下来，最多只能获取前 10000 条数据，30条/page，即最多 333 pages。

```
# zoomeye domain qq.com 1 -page 333
name                                                   timestamp      ip                       
momi.qq.com                                            2021-03-26     ["61.129.7.122"]         
mogo.ke.qq.com                                         2021-03-26     ["203.205.235.71"]       
monitoring.qq.com                                      2021-03-26     ["0.0.0.1"]              
mmd.x5.qq.com                                          2021-03-26     ["0.0.0.1"]              
mgdairy.act.qq.com                                     2021-03-26     ["240e:e1:a900:10::41", "203.205.254.123"]
mobile2.qq.com                                         2021-03-26     ["0.0.0.1"]              
meizu.act.qq.com                                       2021-03-26     ["240e:e1:a900:10::41", "203.205.254.123"]
mobile.ent.qq.com                                      2021-03-26     ["0.0.0.1"]              
mjzl.qq.com                                            2021-03-26     ["0.0.0.1"]              
mock.inews.qq.com                                      2021-03-26     ["58.250.137.40"]        
mfhhk77.qzone.qq.com                                   2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
med0731.qzone.qq.com                                   2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
mmm.qq.com                                             2021-03-26     ["0.0.0.1"]              
meiliwenhua.qzone.qq.com                               2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
mmatest.qq.com                                         2021-03-26     ["0.0.0.1"]              
meishu.qzone.qq.com                                    2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
mmd.tgideas.qq.com                                     2021-03-26     ["0.0.0.1"]              
mjn.act.qq.com                                         2021-03-26     ["0.0.0.1"]              
mengwei1985.qzone.qq.com                               2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
mnzcn.qq.com                                           2021-03-26     ["0.0.0.1"]              
moa.qq.com                                             2021-03-26     ["0.0.0.1"]              
mmr.ke.qq.com                                          2021-03-26     ["203.205.235.71"]       
mchuise.qzone.qq.com                                   2021-03-26     ["240e:928:1400:10::49", "203.205.254.103"]
moe.tc.qq.com                                          2021-03-26     []                       
mobile1.map.qq.com                                     2021-03-26     []                       
mmgr.m.qq.com.cloud.tc.qq.com                          2021-03-26     []                       
mmbiz.qpic.tc.qq.com                                   2021-03-26     []                       
moc.qq.com                                             2021-03-26     []                       
mmgr.3g.qq.com                                         2021-03-26     []                       
mob.pop.exmail.qq.com                                  2021-03-26     []                       

total: 9990/32898
# zoomeye domain qq.com 1 -page 334
=> nothing returns
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
