# -*- coding:utf-8 -*-

from flask import Flask,render_template,request
import recommend

app=Flask(__name__)

@app.route('/')         #装饰器把index函数绑定到url上，实现路由功能
def index():
    return render_template('index.html')

@app.route('/search/')  #装饰器把search函数绑定到url上，实现路由功能
def search():
    # request为全局变量，可得到用户输入信息
    #print('wmr')
    tag = request.args.get('user')
    # 调用推荐函数
    print(tag)
    ans = recommend.recommend(tag)
    #print(dic)
    # 用返回的结果渲染模板
    return render_template('search.html', Data=ans)

if __name__ == '__main__':
    app.run(debug=True)