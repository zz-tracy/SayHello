# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


# 创建index视图函数,分别处理get和post请求
# 处理get请求:从数据库中查询所有的消息记录,返回渲染后的包含消息列表的主页模板index.html.
# 处理post请求: 问候表单提交后,验证表单数据,通过验证后将数据保存到数据库中,使用flash()函数显示一条提示,然后重定向到index视图,渲染页面.
# 使用route装饰器定义url
@app.route('/', methods=['GET', 'POST'])
def index():
    # 实例化HelloForm类,创建记录
    form = HelloForm()
    # 通过if语句验证提交的表单数据
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        # 将提交的数据存储到模型类中
        message = Message(body=body, name=name)
        # 将数据提交到数据库回话
        db.session.add(message)
        # 提交会话
        db.session.commit()
        # 使用flash()函数显示提示消息
        flash('Your message have been sent to the world!')
        # 使用redirect()函数,从定向到index视图
        return redirect(url_for('index'))

    # 加载所有的记录,并使用order_by()过滤器对数据库记录进行排序,参数即为排序的规则(以创建时间的倒序进行排序)
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)
