# 简单的初始化脚本

from flask import Flask
app = Flask(__name__)
app.config.from_object("config")
# 读取以及使用配置文件

from app import views
# 创建应用对象，接着导入视图模块
# 视图是响应来自网页浏览器的请求的处理器。在 Flask 中，视图是编写成 Python 函数。每一个视图函数是映射到一个或多个请求的 URL。
