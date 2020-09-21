# -*- coding: utf-8 -*-
import click

from sayhello import app, db
from sayhello.models import Message


# 使用app.cli.command()装饰器注册自定义drop命令且,会在执行时自动推入应用上下文
@app.cli.command()
# 使用click.option()装饰器,指定命令行选项的名称，从命令行读取参数值，再将其传递给函数。
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


# 使用app.cli.command()装饰器注册自定义drop命令且,会在执行时自动推入应用上下文
@app.cli.command()
# 使用click提供的option装饰器为命令添加数量选项--count,使用default关键字设置默认值为20
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

# 创建用于生成虚拟数据的Faker实例
    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
