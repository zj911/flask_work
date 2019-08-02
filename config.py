# 为了能够处理 web 表单，我们将使用 Flask-WTF ，该扩展封装了 WTForms 并且恰当地集成进 Flask 中。
# 许多 Flask 扩展需要大量的配置

# CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
# SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


# 自定义Openid
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# 配置sqlite数据库
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# SQLALCHEMY_DATABASE_URI 是 Flask-SQLAlchemy 扩展需要的。这是我们数据库文件的路径。
# SQLALCHEMY_MIGRATE_REPO 是文件夹，我们将会把 SQLAlchemy-migrate 数据文件存储在这里。
# 在init.py中初始化