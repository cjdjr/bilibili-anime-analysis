# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
import random
import sqlite3


def get_first_page(baseurl,header,page):#分析动态加载后得到的json格式页面
    print('正在打开第' + str(page) + '页网站')
    url=baseurl+r'page={0}&page_size=20&version=0&is_finish=0&start_year=2015&tag_id=&index_type=1&index_sort=0&area=0&quarter=0'.format(page)
    #print(url)
    try:
        r = requests.get(url,headers = header[random.randint(0,1)])
        r.raise_for_status()
        r.encoding='utf-8'
        response=r.text
        html=json.loads(response)
        return html
    except:
        print('打开网页失败！')

def get_url(html):#从json页面中提取每一个番剧的url
    urllist = []
    urls = html['result']['list']
    for i in urls:
        url = i['url']
        if url!=r'http://bangumi.bilibili.com/anime/2795':
            urllist.append(url)
    return urllist

def get_each_page(url,header):#获取每一个番剧的页面
    print('正在打开网页:',url)
    try:
        r=requests.get(url, headers=header[random.randint(0,1)])
        #print(r.raise_for_status())
        r.encoding='utf-8'
        response=r.text
        return response
    except:
        print('打开网页失败！')

def string_to_float(s):
    n=len(s)
    ans=0.0
    if(s[n-1]=='万'):
        ans=float(s[:-1])
    elif s[n-1]=='亿':
        ans=float(s[:-1])*10000
    else:
        ans=float(s[:])/10000
    return ans

def get_info(response):#从番剧页面中提取信息
    print('正在获取数据...')
    soup=BeautifulSoup(response,"html.parser")
    #print(soup)
    name=soup.find('span',class_="media-info-title-t").string                                       # 获取番剧名字
    play=soup.find('span',class_="media-info-count-item media-info-count-item-play").em.string      # 获取播放总数
    play=string_to_float(play)
    fans=soup.find('span',class_="media-info-count-item media-info-count-item-fans").em.string      # 获取追番人数
    fans=string_to_float(fans)
    review=soup.find('span',class_="media-info-count-item media-info-count-item-review").em.string  # 获取弹幕总数
    review=string_to_float(review)
    score=0.0
    try:
        score=float(soup.find('div',class_="media-info-score-content").find('div').string)
    except AttributeError:
        pass
    tmp=soup.find_all('span', class_="media-tag")  # 获取标签
    tags=''
    for each in tmp:
        tags+=each.string+' '

    return name,play,fans,review,tags,score

def save_to_db(data):
    conn=sqlite3.connect('2015.db')
    c=conn.cursor()
    try:
        c.execute('insert into Opera values(?,?,?,?,?,?)',data)
    except:
        pass
    conn.commit()
    conn.close()

def spider():
    baseurl='https://bangumi.bilibili.com/web_api/season/index_global?'
    header=[{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'},{'User-Agent':'Mozilla/4.04[en](Win95;I;Nav)'}]
    page=1
    total=10
    while page<=total:
        html=get_first_page(baseurl, header, page)
        urllist=get_url(html)
        for url in urllist:
            response = get_each_page(url,header)
            result = get_info(response)
            #print(result)
            save_to_db(result)
            time.sleep(2)
        page+=1

if __name__=='__main__':
    conn=sqlite3.connect('2015.db')
    c=conn.cursor()
    try:
        c.execute('create table Opera(name valchar(20) primary key,play float,fans float,review float,tags valchar(20),score float)')
    except:
        pass
    conn.commit()
    conn.close()
    spider()
