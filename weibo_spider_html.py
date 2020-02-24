#-*-coding:utf-8-*-
import re
import requests
import urllib.request
import time
 
def spider(fp):
    qurl = r'https://s.weibo.com/top/summary'
    page = urllib.request.urlopen(qurl)
    html = page.read()
    tops = re.findall('target="_blank">(.*?)</a>',html.decode('utf-8'),re.S)
    del tops[-1]
    del tops[-1]
    urls = re.findall('<a href="/weibo(.*?)"',html.decode('utf-8'),re.S)
    lists = []
    for m in range(0,len(tops)):
        lists.append('<a href="https://s.weibo.com/weibo'+ urls[m]
           +'target="_blank">'+tops[m]+'</a>')
    i = 0
    for list_m in lists:
        if True:
            if i == 0:
                content = '<p>置顶</p>' + list_m +'\n'
                fp.write(content)
                i += 1
            else:
                content = '<p>'+str(i)+'</p>' + list_m +'\n'
                fp.write(content)
                i += 1

time_open = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Hello, my dear," +'now is '+time_open + 
  " I'm glad to help you keep an eye on the world.")
while True:
    time_now = time.strftime("%b %d %H:%M", time.localtime())
    fp = open(time_now + "'s weibo toplist.html" ,"w+")
    spider(fp)
    fp.close()
    print('*************************************************************')
    print("I've help you copy a list of events that people all seek for,\n" +
      "you can find them in this directory.\n" + 
      "Not to be expected,I'll meet you again an hour later.")
    print('\t\t\t\tLove from your Spider')
    print('*************************************************************\n')
    time.sleep(3600)
