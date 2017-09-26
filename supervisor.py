#coding:utf-8
import requests as req
import time
# 没办法,nova 老是宕机,只能用万能的 py 来监控一下, 5 分钟搞定,还有谁!!!!!!!!
# 自信满满的等待接收即可
while 1 :
    try:
        req.get("http://nova.shu.edu.cn:7000/MIP-FrontEnd/main.html?token=123456789",timeout=10000)
        time.sleep(60)
    except Exception, e :
        req.get("https://pushbear.ftqq.com/sub",params={"sendkey":"981-22aabe24d9c47d339102df259f85fa08","text":"NovaStatus","desp":"Nova离线中"})
        time.sleep(60*30)
