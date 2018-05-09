import re
import threading
import urllib.request
import http.cookiejar
from time import sleep
from urllib import parse
import json

import requests
from python_weibo import WeiBoLogin

proxy_addr = "117.36.103.170:8118"


# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
    # Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8', 'ignore')
    return data


host = 'https://m.weibo.cn/p/231219_2793_newartificial_1001?wm=3333_2001'
trueurl = 'https://m.weibo.cn/api/container/getIndex?wm=3333_2001&sudaref[]=login.sina.com.cn&sudaref[]=login.sina.com.cn&containerid=231219_2793_newartificial_1001'
data = use_proxy(trueurl, proxy_addr)
hosts = use_proxy(host, proxy_addr)

a = hosts.find('st: \'')
b = hosts.find('\'', a + len('st: ') + 1)
st = hosts[a + len('st: \''):b]
jsonData = json.loads(data)
scheme = jsonData['data']['cards'][34]['card_group'][1]['group'][1]['buttons'][0]['scheme']
print(scheme)
uid = scheme.find('uid%3D')
schemepro = scheme[:uid]
print(schemepro)
weibo_url = 'https://m.weibo.cn' + schemepro + 'uid%3D%26active_id%3D2793%26na_id%3D1001'

print(weibo_url)


def vote(url, posts, proxy_addr):
    # cookie = http.cookiejar.CookieJar()
    # # cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # nepo = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # urllib.request.install_opener(nepo)
    #
    # wlg = WeiBoLogin()
    # wlg.login('', '')


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    cookies = {
        'Cookie': ''}
    res = requests.post(url, headers=headers, cookies=cookies, data=posts)
    data = res.text

    # req = urllib.request.Request(url, data=posts)
    # req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    # proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    # opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler(nepo))
    # urllib.request.install_opener(opener)
    # data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


st = {'st': st}
# st = urllib.parse.urlencode({'st': st}).encode(encoding='UTF8')
req = vote(weibo_url, st, proxy_addr)
print(req)


# for i in range(10000):
#     t = threading.Thread(target=vote)
#     t.start()
#     sleep(1)
#     req = vote(weibo_url, 'st='+st, proxy_addr)
# print(req)
# content = json.loads(data)
# print(content)
# print(req[0])
def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址
    ipurl = "http://api.xicidaili.com/free2016.txt"
    r = requests.get(url=ipurl)
    all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
    with open("C:\\Users\\Desktop\\IP.txt", 'w') as f:
        for i in all_url:
            f.write(i)
            f.write('\n')
    return all_url


