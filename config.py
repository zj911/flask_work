# 为了能够处理 web 表单，我们将使用 Flask-WTF ，该扩展封装了 WTForms 并且恰当地集成进 Flask 中。
# 许多 Flask 扩展需要大量的配置

# CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
# SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'