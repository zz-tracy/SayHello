# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# 创建程序实例app,传入__name__变量作为Flask类构造方法的import_name参数值,通过这个值来确认程序路径
app = Flask('sayhello')
# 使用config对象的from_pyfile()方法加载配置,同时传入配置模块的文件名作为参数
app.config.from_pyfile('settings.py')
# 通过设置jinjia2环境变量,去掉jinjia2语句占据的空白行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 创建SQLAlchemy实例,并传入程序实例app
db = SQLAlchemy(app)
# 实例化Bootstrap类,并传入程序实例app以完成Bootstrap-Flask扩展的初始化
# bootstrap对象的主要作用是用来快速方便地加载资源文件,和渲染表单,方便快速开发
bootstrap = Bootstrap(app)
# 实例化扩展提供的Moment类(用于处理时间和日期的开源JavaScript库),并传入程序实例app,完成扩展的初始化
moment = Moment(app)

# 为了让使用程序实例app注册的视图函数,错误处理函数,自定义命令函数等和程序实例关联起来,所以需要在构造文件中导入这些模块
# 因为这些模块也需要从构造文件中导入程序实例,为例避免循环依赖,这些导入语句在构造文件的末尾定义.
from sayhello import views, errors, commands
