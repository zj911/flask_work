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

    # validate_on_submit 方法做了所有表单处理工作。当表单正在展示给用户的时候调用它，它会返回 False.
    # 定义表单时没写validators=[DataRequired()]，如果不写这句，form.validate_on_submit()就认为表单是空的，所以会false。
    # 如果 validate_on_submit 在表单提交请求中被调用，它将会收集所有的数据，对字段进行验证，
    # 如果所有的事情都通过的话，它将会返回 True，表示数据都是合法的。这就是说明数据是安全的，并且被应用程序给接受了。
    if form.validate_on_submit(): # true

        # flash 函数是一种快速的方式下呈现给用户的页面上显示一个消息。
        # 闪现的消息将不会自动地出现在我们的页面上，我们的模板需要加入展示消息的内容。
        # 我们将添加这些消息到我们的基础模板中，这样所有的模板都能继承这个函数,更新base.html
        flash('Login requested for Openid="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template(
        'login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS']
    )
# 导入 LoginForm 类，从这个类实例化一个对象，接着把它传入到模板中


