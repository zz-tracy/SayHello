# -*- coding: utf-8 -*-
import os
import sys

from sayhello import app

# 设置不同操作系统的前缀,已到达兼容的效果
# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 通过app.instance_path属性获取实例文件夹的路径
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

# 使用占位字符来配置存储在SECRET_KEY配置变量的秘钥
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 构建数据库URI
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
