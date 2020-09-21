# -*- coding: utf-8 -*-

from datetime import datetime

from sayhello import db


# 创建数据库模型
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    # timestamp字段用来存储每一条留言的发表时间,使用datetime.utcnow()方法生成当前的UTC(协调世界时间),并设置为timestrap字段的默认值.
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
