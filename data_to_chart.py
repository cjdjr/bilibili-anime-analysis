from pyecharts import Bar, Line, Overlap,Pie
import sqlite3

def total_number():
    '''
    对三年的番剧总数进行统计分析
    '''
    year=['2015','2016','2017']
    total=[]
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        c.execute('select count(name) from Opera')
        total.append(c.fetchone()[0])
        conn.close()
    #print(total)
    bar=Bar('bilibili年度番剧总数')
    bar.add('bar',year,total)
    line=Line()
    line.add('line',year,total)
    overlap=Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(r'D:\wmr\python\bilibili\图表\年度番剧总数.html')

def ave_play():
    '''
    对三年的番剧的平均播放量统计分析
    '''
    year=['2015','2016','2017']
    total=[]
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        c.execute('select avg(play) from Opera')
        total.append(c.fetchone()[0])
        conn.close()
    #print(total)
    bar=Bar('bilibili番剧平均播放量（单位：万）')
    bar.add('bar',year,total)
    line=Line()
    line.add('line',year,total)
    overlap=Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(r'D:\wmr\python\bilibili\图表\番剧平均播放量.html')

def ave_fans():
    '''
    对三年的番剧的平均追番人次统计分析
    '''
    year=['2015','2016','2017']
    total=[]
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        c.execute('select avg(fans) from Opera')
        total.append(c.fetchone()[0])
        conn.close()
    #print(total)
    bar=Bar('bilibili番剧平均追番人次（单位：万）')
    bar.add('bar',year,total)
    line=Line()
    line.add('line',year,total)
    overlap=Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(r'D:\wmr\python\bilibili\图表\番剧平均追番人次.html')

def ave_review():
    '''
    对三年的番剧的平均弹幕量统计分析
    '''
    year=['2015','2016','2017']
    total=[]
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        c.execute('select avg(review) from Opera')
        total.append(c.fetchone()[0])
        conn.close()
    #print(total)
    bar=Bar('bilibili番剧平均弹幕量（单位：万）')
    bar.add('bar',year,total)
    line=Line()
    line.add('line',year,total)
    overlap=Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(r'D:\wmr\python\bilibili\图表\番剧平均弹幕量.html')

def ave_score():
    '''
    对三年的番剧的平均评分统计分析
    '''
    year=['2015','2016','2017']
    total=[]
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        c.execute('select avg(score) from Opera where score>0.0')
        total.append(c.fetchone()[0])
        conn.close()
    #print(total)
    bar=Bar('bilibili番剧平均评分')
    bar.add('bar',year,total)
    line=Line()
    line.add('line',year,total)
    overlap=Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(r'D:\wmr\python\bilibili\图表\番剧平均评分.html')

def hottags():
    '''
    对三年的热门类型番剧的平均追番人数进行统计
    '''
    bar = Bar('''bilibili热门类型番剧平均追番人数
                （单位：万）''')
    tags=['热血','奇幻','战斗','搞笑','日常','科幻','治愈','泡面','恋爱','后宫','魔法','机战','运动','励志']
    year=['2015','2016','2017']
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        v=[]
        for tag in tags:
            c.execute("select avg(fans) from Opera where tags like '%{0}%'".format(tag))
            v.append(c.fetchone()[0])
        #print(len(v))
        conn.close()
        bar.add(y+'年',tags,v)
    #print(total)
    bar.render(r'D:\wmr\python\bilibili\图表\热门类型番剧平均追番人数.html')

def hottags_number():
    '''
    对三年的热门类型的番剧总数进行统计
    '''
    bar = Bar('bilibili热门类型番剧总数')
    tags=['热血','奇幻','战斗','搞笑','日常','科幻','治愈','泡面','恋爱','后宫','魔法','机战','运动','励志']
    year=['2015','2016','2017']
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        v=[]
        for tag in tags:
            c.execute("select count(*) from Opera where tags like '%{0}%'".format(tag))
            v.append(c.fetchone()[0])
        #print(len(v))
        conn.close()
        bar.add(y+'年',tags,v)
    #print(total)
    bar.render(r'D:\wmr\python\bilibili\图表\热门类型番剧总数.html')

def hottags_score():
    '''
    对三年的热门类型的番剧平均评分进行统计
    '''
    bar = Bar('bilibili热门类型番剧平均评分')
    tags=['热血','奇幻','战斗','搞笑','日常','科幻','治愈','泡面','恋爱','后宫','魔法','机战','运动','励志']
    year=['2015','2016','2017']
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        v=[]
        for tag in tags:
            c.execute("select avg(score) from Opera where score>0.0 and tags like '%{0}%'".format(tag))
            v.append(c.fetchone()[0])
        #print(len(v))
        conn.close()
        bar.add(y+'年',tags,v)
    #print(total)
    bar.render(r'D:\wmr\python\bilibili\图表\热门类型番剧平均评分.html')

def score_distribute():
    '''
    对评分的分布进行统计
    '''
    bar = Bar('bilibili番剧评分分布')
    pie=Pie('bilibili番剧评分分布')
    name=['0~1','1~2','2~3','3~4','4~5','5~6','6~7','7~8','8~9','9~10']
    down=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    up=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
    sum=[0,0,0,0,0,0,0,0,0,0]
    year=['2015','2016','2017']
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        v=[]
        for i in range(10):
            c.execute("select count(*) from Opera where score>{0} and score<={1}".format(down[i],up[i]))
            v.append(c.fetchone()[0])
            sum[i]+=v[i]
        print(v)
        #print(len(v))
        conn.close()
        bar.add(y+'年',name,v)
    #print(total)
    pie.add('',name,sum,is_label_show=True)
    bar.render(r'D:\wmr\python\bilibili\图表\番剧评分分布.html')
    pie.render(r'D:\wmr\python\bilibili\图表\番剧评分分布(饼图).html')

def score_low():
    '''
    对三年的热门类型的番剧中评分小于8.0分的比例进行统计
    '''
    bar = Bar('bilibili评分低于8.0分的比例统计')
    tags=['热血','奇幻','战斗','搞笑','日常','科幻','治愈','泡面','恋爱','后宫','魔法','机战','运动','励志']
    year=['2015','2016','2017']
    for y in year:
        conn = sqlite3.connect(y+'.db')
        c = conn.cursor()
        v=[]
        for tag in tags:
            c.execute("select count(*) from Opera where score<8.0 and tags like '%{0}%'".format(tag))
            num=c.fetchone()[0]
            c.execute("select count(*) from Opera where tags like '%{0}%'".format(tag))
            num=num/c.fetchone()[0]
            v.append(num)
        #print(len(v))
        conn.close()
        bar.add(y+'年',tags,v,is_stack=True)
    #print(total)
    bar.render(r'D:\wmr\python\bilibili\图表\评分低于8.0分的比例统计.html')

if __name__=='__main__':
    total_number()
    ave_play()
    ave_review()
    ave_fans()
    ave_score()
    hottags()
    hottags_number()
    hottags_score()
    score_distribute()
    score_low()