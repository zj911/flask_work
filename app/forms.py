# 在 Flask-WTF 中，表单是表示成对象，Form 类的子类。一个表单子类简单地把表单的域定义成类的变量。

# 我们将要创建一个登录表单，用户用于认证系统。在我们应用程序中支持的登录机制不是标准的用户名/密码类型，
# 我们将使用 OpenID。OpenIDs 的好处就是认证是由 OpenID 的提供者完成的，因此我们不需要验证密码，这会让我们的网站对用户而言更加安全。

# OpenID 登录仅仅需要一个字符串，被称为 OpenID。我们将在表单上提供一个 ‘remember me’ 的选择框，
# 以至于用户可以选择在他们的网页浏览器上种植 cookie ，当他们再次访问的时候，浏览器能够记住他们的登录。

from flask_wtf import FlaskForm #已经change
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid = StringField("openid", validators=[DataRequired()])
    remember_me = BooleanField("remember me", default=False)

# DataRequired 验证器只是简单地检查相应域提交的数据是否是空

