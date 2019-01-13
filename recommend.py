# -*- coding:utf-8 -*-
import sqlite3

def score_to_str(score):
    if score==0.0:
        return '无评分'
    else:
        return str(score)
def recommend(query):
    '''
    番剧推荐
    '''
    query = query.split(' ')
    ans=""

    ans+="2015年<br><br>"
    conn = sqlite3.connect('2015.db')
    c = conn.cursor()
    num=0
    for raw in c.execute("select * from Opera order by play desc"):
        count=0
        tags=raw[4]

        tags='|'+tags.replace(' ' , '|')
        for each in query:
            if each in tags:
                count+=1
        if count+1>=len(query) and count>0:

            ans+="%40s%40s%40s<br><br>" %(raw[0],tags,'评分：'+score_to_str(raw[5]))
            num+=1

        if num>=5:
            break

    ans += "2016年<br><br>"
    conn = sqlite3.connect('2016.db')
    c = conn.cursor()
    num=0
    for raw in c.execute("select * from Opera order by play desc"):
        count=0
        tags=raw[4]
        tags='|'+tags.replace(' ', '|')
        for each in query:
            if each in tags:
                count+=1
        if count+1>=len(query) and count>0:
            ans += "%40s%40s%40s<br><br>" % (raw[0],tags,'评分：' +score_to_str(raw[5]))
            num+=1

        if num>=5:
            break

    ans += "2017年<br><br>"
    conn = sqlite3.connect('2017.db')
    c = conn.cursor()
    num=0
    for raw in c.execute("select * from Opera order by play desc"):
        count = 0
        tags = raw[4]
        tags='|'+tags.replace(' ', '|')
        for each in query:
            if each in tags:
                count += 1
        if count + 1 >= len(query) and count>0:
            ans += "%40s%40s%40s<br><br>" % (raw[0],tags,'评分：' +score_to_str(raw[5]))
            num+=1

        if num>=5:
            break
    conn.commit()
    conn.close()
    return ans
