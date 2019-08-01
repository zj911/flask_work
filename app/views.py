from app import app
from flask import render_template
# render_template 调用了 Jinja2 模板引擎，Jinja2 模板引擎是 Flask 框架的一部分。Jinja2 会把模板参数提供的相应的值替换了 {{…}} 块。

# 两个 route 装饰器创建了从网址 / 以及 /index 到这个函数的映射。
@app.route('/')
@app.route('/index')
def index():
    # return("get world")
    user = { 'nickname': "migul" }

    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        "index.html",
        title = "Home",
        user = user,
        posts = posts
    )

from flask import flash, redirect
from .forms import LoginForm

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    return render_template(
        'login.html',
        title = 'Sign In',
        form = form
    )
# 导入 LoginForm 类，从这个类实例化一个对象，接着把它传入到模板中
