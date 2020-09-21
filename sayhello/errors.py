# -*- coding: utf-8 -*-
from flask import render_template

from sayhello import app


# 使用errorhandler()装饰器注册404错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 使用errorhandler()装饰器注册500错误处理函数
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
